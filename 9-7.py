class User:

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age}, {self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you're finally verified! ")

class Admin(User):

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        


    def show_privileges(self):
        privileges = ["can add post", "can delete post", "can ban user", "can freeze account"]
        for privilege in privileges:
            print(privilege)

my_user = Admin("Domantas", "Jokubaitis", 18, "M")
my_user.show_privileges()