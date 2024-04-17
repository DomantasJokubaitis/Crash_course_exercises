from userclass import User

class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can freeze account"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)