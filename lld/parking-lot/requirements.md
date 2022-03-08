# Parking Lot LLD

Entities -
1. Vehicle
   1. attrs
      1. registration_number
2. Ticket
   1. attrs
      1. id
      2. vehicle
      3. entry_time
      4. entry_point
      5. exit_time
      6. exit_point
   2. methods
      1. create - issue new ticket
      2. calculate_fare - based on vehicle and duration
      3. complete - close ticket post payment
3. Access Point
   1. attrs
      1. booth_id
      2. executive_id
4. Entry Point (Access Point) - singleton
   1. attrs
   2. methods
      1. issue_ticket
5. Exit Point (Access Point) - singleton
   1. attrs
   2. methods
      1. get_fare
      2. close_ticket
6. ParkingSimulator
   1. methods
      1. vehicle_entry
      2. vehicle_exit