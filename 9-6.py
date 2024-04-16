class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
    
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open ")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def flavors(self):
        flavors = ["Banana", "Strawberry", "Chocolate", "Vanilla"]
        for flavor in flavors:
            print(flavor)

my_restaurant = IceCreamStand("Bidens ice", "Icecream")
my_restaurant.flavors()