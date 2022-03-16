# Tic Tac Toe

from typing import Optional, Tuple
import uuid
import random

Move = Tuple[int, int]


class Stats:
    def __init__(self) -> None:
        self.win = 0
        self.lose = 0
        self.draw = 0


class StatsReadOnlyView:
    ...


class StatsManager:
    """Read and Write access to Stats objects (player.user.stats)"""
    @classmethod    
    def register_win(cls, player: 'Player') -> None:
        ...
    
    def register_loss(cls, player: 'Player') -> None:
        ...

    def register_draw(cls, player: 'Player') -> None:
        ...


class User:
    """
    Has -
    - user details
    - game history details
        - wins
        - losses
        - draws
    - request to play new game
    - receive notifications
    """
    def __init__(self, username: str) -> None:
        self.id = uuid.uuid4()
        self.username = username
        self.current_player = None
        self.stats = StatsReadOnlyView
        
    def start_new_game(self) -> 'Player':
        match_maker = MatchMaker.get_instance()
        player = match_maker.request_new_game(user=self)
        return player


class Player:
    """
    Has game playing capabilities
    - make a move
    - receive notifications
    """
    def __init__(self, user: User) -> None:
        self.id = uuid.uuid4()
        self.user = user
        self.game = None

    @ property
    def username(self):
        return self.user.username

    def join_game(self, game: 'Game'):
        """game has players and players have a game"""
        self.game = game

    def event_receiver(self, event: str):
        """receives events from game notifier and act on it"""
        ...
    
    def get_game_state(self) -> 'BoardReadOnly':
        ...
    
    def make_move(self, move: Move):
        """make a move if game has started and it is your turn"""
        if not self.game:
            raise RuntimeError('Game hasn\'t started yet')
        if self is not self.game.get_next_turn_player():
            raise RuntimeError('Not your turn')
        
        valid, message = self.game.register_move(player=self, move=move)
        if not valid:
            print(f'invalid move - {message}')
        
    
class Board:
    def __init__(self) -> None:
        self.id = uuid.uuid4()


class BoardReadOnly:
    ...


class Game:
    """ Acts as a mediator b/w players and board """
    def __init__(self, player_x: Player, player_o: Player, stats_manager=StatsManager) -> None:
        self.id = uuid.uuid4()
        self.player_x = player_x
        self.player_o = player_o 
        self.board = Board()
        self.notifier = Notifier(game=self)
        self.stats_manager = stats_manager
    
    def get_next_turn_player(self):
        """returns player who has to make a move now"""
        ...
    
    def get_current_state(self):
        """returns current state of the game"""
        ...
    
    def start(self):
        """take initial steps to start the game"""    
        # notify players that game has started
        self.notifier.notify_all_players(event='players joined')
        self.notifier.notify_all_players(event='game started')
        self.request_next_move()
    
    def request_next_move(self):
        """send notification to next player for making a move"""
        next_turn_player = self.get_next_turn_player()
        self.notifier.notify_player(event='make move', player=next_turn_player)
    
    def register_move(self, player: Player, move: Move) -> bool:
        """register a move requested by the player post validation"""
        is_valid, message = self.is_valid_move(player, move)
        if not is_valid:
            # is_valid is False
            return is_valid, message
        
        self.mark_move(player, move)
        # analyze state
        ended, draw, winner, loser = self.analyze_state()
        if ended:
            self.notifier.notify_all_players(event='game ended')
            if draw:
                self.notifier.notify_all_players(event='game draw')
                # update player stats
                self.stats_manager.register_draw(player=player_1)
                self.stats_manager.register_draw(player=player_2)

            else:
                self.notifier.notify_player(event='you won', player=winner)                
                self.notifier.notify_player(event='you lost', player=loser)

                # update player stats
                self.stats_manager.register_win(player=winner)
                self.stats_manager.register_loss(player=loser)
        
        else:
            self.request_next_move()
        return True

    def mark_move(self, player: Player, move: Move):
        """identify player_x/o and mark the move on board and update next turn player"""
        ...
    
    def is_valid_move(self, player: Player, move: Move) -> Tuple[bool, str]:
        """validate is move request by pllayer is valid"""
        ...
    
    def analyze_state(self) -> Tuple[bool, Optional[bool], Optional[Player], Optional[Player]]:
        """
        analyze the state of the game
        return:
            - ended: bool - game ended
            - draw: bool - game draw
            - winner: Player - if ended and not draw, winner of the game
            - loser: Player - if ended and not draw, loser of the game
        """
        ...

class MatchMaker:
    __singleton_instance = None
    waiting_player: Optional[Player] = None

    @classmethod
    def get_instance(cls):
        if not cls.__singleton_instance:
            cls.__singleton_instance = MatchMaker()
        return cls.__singleton_instance

    def request_new_game(self, user: User) -> Tuple[Player, Optional[Game]]:
        player = Player(user)
        game = None
        print(f'player {player.username} requesting a new game')

        if self.waiting_player:
            players = (player, self.waiting_player)
            game = self._create_new_game(players=players)
            game.start()

        else:
            self.waiting_player = player
            print(f'player {player.username} is in queue')
        
        return player
    
    def _toss(self, players: Tuple[Player]) -> Tuple[Player]:
        """player_x will have the chance to make the first move"""
        player_x = random.choice(players)
        player_o = players[(players.index(player_x) + 1) % 2]
        print(f'Toss results\nx: {player_x.username}\no: {player_o.username}')
        return player_x, player_o
    
    def _create_new_game(self, players: Tuple[Player]) -> Game:
        player_x, player_o = self._toss(players)
        game = Game(player_x=player_x, player_o=player_o)
        player_x.join_game(game=game)
        player_o.join_game(game=game)
        print(f'new game {game.id}')
        print(f'{player_x.username} joined')
        print(f'{player_o.username} joined')
        return game


class Notifier:
    """
    event notifications from game to players
    event: 
        - player joined game
        - player made a move
        - game resuesting player's move
        - game started
        - game ended
        - game results
    """
    def __init__(self, game) -> None:
        self.game = game
    
    def notify_player(self, event: str, player: Player) -> None:
        ...
    
    def notify_all_players(self, event: str) -> None:
        ...


if __name__ == '__main__':
    # create users
    user_1 = User(username='ragnar')
    user_2 = User(username='floki')

    player_1 = user_1.start_new_game()
    player_2 = user_2.start_new_game()

