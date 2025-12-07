from classes.trainClass import *
from utils.utils import *

def main():
    # TODO: Implement main logic here 
    title("Welcome to Train Management System")
    # TODO: Create a train instance with user inputs
    train1 = TrainClass()
    train1.name = input("Enter name for your train: ")
    train1.color = input(f"Enter color for {train1.name}: ")
    train1.set_destination(input(f"Enter destination for {train1.name}: "))
    # TODO: Display train details from user inputs
    print(title(f"Train {train1.name} Details"))
    print(f"Name: {train1.get_name()}")
    print(f"Color: {train1.get_color()}")
    print(f"Destination: {train1.get_destination()}")
    loop(train1)

# TODO: Implement loop function to handle user commands
def loop(train1: TrainClass):
    # TODO: Initialize statistics variables
    totalPassengers = 0
    totalDistance = 0
    totalCommands = 0
    maxSpeed = 0
    # TODO: Command loop
    while True:
        # TODO: Get the meters per second, divide by 3600 to get per second
        metersPerCommand = getMetersPerSecond(train1.get_speed())
        # TODO: Get user command, accelerate, brake, board, disembark, arrive
        input_command = input("Enter command ([a]ccelerate, [b]rake, b[o]ard, [d]isembark, a[r]rive,): ").strip().lower()
        totalCommands += 1
        totalDistance += metersPerCommand
        # TODO: Process user command

        
        if input_command == 'a':
            # ----------- ACCELERATE -----------
            train1.accelerate()
            print(f"{train1.get_name()} accelerated to {train1.get_speed()} km/h")
            if train1.get_speed() > maxSpeed:
                maxSpeed = train1.get_speed()


        elif input_command == 'b':
            # ----------- BRAKE -----------
            train1.brake()
            print(f"{train1.get_name()} slowed down to {train1.get_speed()} km/h")

            
        elif input_command == 'o':
            # ----------- BOARD -----------
            randomAmout = randint(5, 20)
            totalPassengers += randomAmout
            for _ in range(randomAmout):
                passenger_name = RANDOM_PASSENGER_NAMES[randint(0, len(RANDOM_PASSENGER_NAMES)-1)]
                train1.board_passenger(passenger_name)
            print(f"{randomAmout} passengers boarded {train1.get_name()}. Total passengers: {train1.get_passenger_count()}")


        elif input_command == 'd':
            # ----------- DISEMBARK -----------
            if train1.get_passenger_count() > 0:
                randomAmout = randint(1, train1.get_passenger_count())
                for _ in range(randomAmout):    
                    passenger_name = train1.passengers[0]
                    train1.disembark_passenger(passenger_name)
                print(f"{randomAmout} passengers disembarked from {train1.get_name()}. Total passengers: {train1.get_passenger_count()}")
            else:
                print("No passengers to disembark!")


        elif input_command == 'r':
            # ----------- ARRIVE -----------
            train1.arrive_at_station("Station " + train1.get_destination())
            print(f"{train1.get_name()} has arrived at {train1.get_current_station()}.")
            printStats(totalCommands, totalDistance, maxSpeed, totalPassengers)
            break


        else:
            # ----------- INVALID COMMAND -----------
            print("Invalid command. Please try again.")
    pass

# TODO: Implement printStats function to display journey summary
def printStats(totalCommands, totalDistance, maxSpeed, totalPassengers):
    print(title("Train Journey Summary"))
    print(f"Total commands executed: {totalCommands}")
    print(f"Total distance traveled: {totalDistance:,.2f} meters")
    print(f"Maximum speed reached: {maxSpeed} km/h")
    print(f"Total passengers boarded: {totalPassengers}")
    pass

if __name__ == "__main__":
    main()