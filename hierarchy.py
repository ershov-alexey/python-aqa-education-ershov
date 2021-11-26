class Transport:
    def __init__(self, type, weight, height):
            self.type = type
            self.weigth = weight
            self.height = height

class Aircraft(Transport):
    def __init__(self, type, weight, height, max_speed, carrying_capacity):
        super().__init__(type, weight, height)
        self.max_speed = max_speed
        self.carrying_capacity = carrying_capacity

class Car(Transport):
    def __init__(self, type, weight, height, top_speed, cargo_weight):
        super().__init__(type, weight, height)
        self.top_speed = top_speed
        self.cargo_weight = cargo_weight

class PassengerCar(Car):
    def __init__(self, passengers_weight, bodywork_type, height, top_speed, cargo_weight):
        Car.__init__(self, passengers_weight, bodywork_type, height, top_speed, cargo_weight)
        self.passengers_weight = passengers_weight
        self.bodywork_type = bodywork_type

    @staticmethod
    def full_weight(transport_weight, passenger_car_weight, car_cargo_weight):
        return transport_weight + passenger_car_weight + car_cargo_weight
        # нужно сложить weight, cargo_weight и passengers_weight"""

class WaterTtransport(Transport):
    def __init__(self, type, weight, height, cruising_range, number_of_passengers):
        super().__init__(type, weight, height)
        self.cruising_range = cruising_range
        self.number_of_passengers = number_of_passengers

class UnderWaterTransport(Transport):
    def __init__(self, type, weight, height, displacement, length):
        super().__init__(type, weight, height)
        self.displacement = displacement
        self.length = length


def main():
    transport1 = Transport('car', 1000, 10)
    print(transport1.type)
    print(transport1.weigth)
    print('=======\n')
    air1 = Aircraft('plane', 5000, 100, 400, 160)
    print(air1.type)
    print(air1.weigth)
    print('=======\n')
    passenger_car1 = PassengerCar(240, 2, 2, 320, 500)
    print(passenger_car1.full_weight(transport1.weigth, passenger_car1.passengers_weight, passenger_car1.cargo_weight))
    print('=======\n')
    watertransport1 = WaterTtransport("boat", 2000, 3, 125, 16)
    print(watertransport1.type)
    print(watertransport1.cruising_range)
    print('=======\n')
    underwatertransport1 = UnderWaterTransport("submarine", 5, 10, 25, 30)
    print(underwatertransport1.type)

if __name__ == '__main__':
    main()