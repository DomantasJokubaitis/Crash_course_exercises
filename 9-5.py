class User:

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age}, {self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, you're finally verified! ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Domantas", "Jokubaitis", 18, "M")
user1.describe_user()
user1.greet_user()

user2 = User("John", "Smith", 26, "M")
user2.describe_user()
user2.greet_user()

user3 = User("Nancy", "Brown", 44, "F")
user3.describe_user()
user3.greet_user()

user3.increment_login_attempts()
print(user3.login_attempts)
user3.increment_login_attempts()
print(user3.login_attempts)
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)