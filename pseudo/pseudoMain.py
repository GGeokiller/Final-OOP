"""
Start program

Show title

Create a train instance with user inputs

Display train details from user inputs

Implement loop function to handle user commands
from utils import title, getMetersPerSecond, RANDOM_PASSENGER_NAMES
    Initialize statistics variables

    While the program is running:
        Get the meters per second, divide by 3600 to get per second
        Get user command, accelerate, brake, board, disembark, arrive
        Process user command

        If command is accelerate:
            Accelerate the train using train method
            Update max speed if current speed is higher
        
        If command is brake:
            Brake the train using train method
        
        If command is board:
            Board a random number of passengers using train method
        
        If command is disembark:
            Disembark a random number of passengers using train method
        
        If command is arrive:
            Arrive at the next station using train method
        
        Print statistics
"""