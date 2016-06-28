class Vehicle():

    FUEL_TYPES = ["diesel", "gasoline"]

    @classmethod
    def list_fuel_types(cls):
        return cls.FUEL_TYPES

    def __init__(self, max_speed, passenger_num, fuel_type):
        print("Vehicle __init__ has been called!")

        super().__init__()

        self.max_speed = max_speed
        self.passenger_num = passenger_num
        if fuel_type not in self.FUEL_TYPES:
            raise ValueError("invalid fuel type")
        else:
            self.fuel_type = fuel_type

    def horn(self):
        raise(NotImplementedError)


class TransmissionMixin():

    def __init__(self, *args, **kwargs):
        print("TransmissionMixin __init__ has been called!")
        super().__init__(*args, **kwargs)
        self.current_gear = 1

    def shift_up(self):
        self.current_gear += 1

    def shift_down(self):
        self.current_gear -= 1


class Car(Vehicle, TransmissionMixin):

    CAR_TYPES = ["limousine", "station wagon", "coupe"]

    @classmethod
    def check_if_car_type_exists(cls, car_type):
        return car_type in cls.CAR_TYPES

    def __init__(self, car_type, *args, **kwargs):
        print("Car __init__ has been called!")
        super().__init__(*args, **kwargs)
        self.car_type = car_type
        if self.check_if_car_type_exists:
            self.car_type = car_type
        else:
            raise ValueError("invalid car type")

    def horn(self):
        print("tuuuuuuu")


class Truck(Vehicle, TransmissionMixin):

    def __init__(self, max_capacity, *args, **kwargs):
        print("Truck __init__ has been called!")
        super().__init__(*args, **kwargs)
        self.max_capacity = max_capacity

    def horn(self):
        print("duuuuuu")


class JetPlain(Vehicle):

    FUEL_TYPES = ["kerosene", "nitro"]

    def __init__(self, max_altitude, *args, **kwargs):
        print("JetPlain __init__ has been called!")
        super().__init__(*args, **kwargs)
        self.max_altitude = max_altitude
