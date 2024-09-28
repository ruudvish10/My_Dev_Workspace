class Car:
    """Defines the blueprint of a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 50
    
    def descriptive_name(self):
        car_name = f"Car Name: {self.year} {self.make} {self.model}"
        return car_name.title()
    
    def get_odometer_reading(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set odometer reading to the given value
        Reject change if it attempts to roll back the odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the milage on an odometer!")

    def increment_mileage(self, miles):
        """Add any additional miles incurred to the total mileage"""
        self.odometer_reading += miles 


class Battery():
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This electric car has a battery {self.battery_size} kWh")
    
    def get_range(self):
        """Get the range this battery provides"""
        if self.battery_size == 50:
            range = 200
        elif self.battery_size == 65:
            range = 300

        print(f"This car can go upto {range} kms on full charge")



#Inheritance - child classes
class Electric_Car(Car):
    """Defines what an electric car should be like"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
     

"""Instances/Objects of the class"""    
my_tesla = Electric_Car("Tesla", "Model 3", 2024)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



        

