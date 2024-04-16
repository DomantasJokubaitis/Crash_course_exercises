class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
    
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open ")

my_restaurant = Restaurant("Borsch", "Slav")
print(my_restaurant.restaurant_name, my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("Familia", "Pizza")
your_restaurant.describe_restaurant()

her_restaurant = Restaurant("Johny", "Burger")
her_restaurant.describe_restaurant()