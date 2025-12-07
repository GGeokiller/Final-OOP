"""
Create train class
with methods to:
- accelerate
- brake
- board passengers
- disembark passengers
- arrive at station

in __init_:
- name
- color
- speed
- passengers list
- max passengers
- destination
- max passengers
- current station

accelerate(amount=10): increase speed by amount

brake(amount=10): decrease speed by amount, not below 0

board_passenger(passenger_name=None): add passenger to list if not full

disembark_passenger(passenger_name): remove passenger from list if present

get_speed(): return current speed

get_passenger_count(): return number of passengers

get_destination(): return destination

get_current_station(): return current station

"""