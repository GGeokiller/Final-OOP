from random import randint

class TrainClass:
    def __init__(self, name="Unnamed Train", color="Red", max_passengers=100):
        # Basic train attributes
        self.speed = 0
        self.name = name
        self.color = color
        self.distance = 0
        
        # Passenger system
        self.passengers = []
        self.max_passengers = max_passengers

        self.destination = "Unknown"
        self.current_station = 0

    def accelerate(self, amount=10):
        self.speed += amount

    def brake(self, amount=10):
        self.speed = max(0, self.speed - amount)

    def board_passenger(self, passenger_name=None):
        if passenger_name is None:
            passenger_name = f"Passenger[{randint(1, 1000)}]"

        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger_name)

    def disembark_passenger(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
        else:
            print(f"{passenger_name} is not on the train!")

    def set_destination(self, destination):
        self.destination = destination

    def arrive_at_station(self, station_name):
        self.current_station = station_name

    # -------------------------
    # Getters
    # -------------------------
    def get_speed(self):
        return self.speed

    def get_passenger_count(self):
        return len(self.passengers)

    def get_destination(self):
        return self.destination

    def get_current_station(self):
        return self.current_station

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
