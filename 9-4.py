class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
    
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open ")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, numb):
        self.number_served += numb

my_restaurant = Restaurant("Borsch", "Ukraina")
print(my_restaurant.number_served)
my_restaurant.number_served = 5
print(my_restaurant.number_served)
my_restaurant.set_number_served(8)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(10)
print(my_restaurant.number_served)

        

    