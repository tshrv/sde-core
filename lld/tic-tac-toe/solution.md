# Tic Tac Toe

## Solution - Low Level Design

1. User
   1. Request new game
      1. Provide a target user to play with
2. MatchMaker
   1. StartGame
      1. Receives two users and creates player instances
      2. Creates a new game instance with the two players
      3. Control forwared to Game
3. Player
   1. Make a move
      1. Get current state of game
      2. Decide your move
      3. Instruct GameController to register your move
4. Game
   1. Initialise
      1. Assign X and O to players but don't share it with them
   2. Return current state of game - requested by player
      1. Requesting player's marked cells
      2. Competing player's marked cells
      3. Empty cells
   3. Register a move - requested by player
      1. Register the move
      2. Check if any player won the match
         1. Finalize game instance
            1. Mark the winner and loser
            2. Update game instance in db
         2. Instruct players to finalize themselves
            1. Make any updates
            2. Save to db
      3. Otherwise, request next move
   4. Request next move
      1. Decide which player's turn it is
      2. Intruct the player to make a move


## ERD

1. User - Player [1:N]
2. Game - Player [1:1], Player 1
3. Game - Player [1:1], Player 2

## OOD

1. User
   1. request_new_game(self, target_user_id)
      1. MatchMaker.start_new_game
2. MatchMaker
   1. start_new_game(cls, user_id_1, user_id_2)
      1. Player
      2. Game
3. Player(User)
   1. make_move(self)
      1. Game.get_current_state
   2. finalize_game(self)
4. Game
   1. pre_game_init(self)
   2. get_current_state(self)
   3. get_next_turn_player(self)
   4. request_next_move(self)
      1. Game.get_next_turn_player
      2. Game.register_move
      3. Game.analyze_state
   5. register_move(self, player)
      1. Player.make_move
   6. analyze_state(self)
      1. Game.finalize_game
      2. Game.request_next_move
   7. finalize_game(self)
      1. Player.finalize_game