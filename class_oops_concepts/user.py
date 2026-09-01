class User:
    """A simple class for user"""

    def __init__(self, first_name, last_name, position):
        """Initializes the first_name, last_name and position attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.login_attempts = 0

    def describe_user(self):
        """Summary of the user information"""
        print(f"\nFirstName: {self.first_name}")
        print(f"LastName: {self.last_name}")
        print(f"Position: {self.position}")

    def greet_user(self):
        """Greet the user"""
        name = f"{self.first_name} {self.last_name}"
        print(f"\nHi {name}, Welcome to the User's profile.")

    def increment_login_attempts(self):
        """Increments the login attempts by 1"""
        self.login_attempts += 1
        print(f"The number of login attempts is {self.login_attempts}")

    def reset_login_attempts(self):
        """Resets the login attempt to 0"""
        self.login_attempts = 0
        print(f"The login attempts has been rest to {self.login_attempts}")


# Instantiation
user_1 = User("Rupashri", "Mohan", "App Developer")
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

user_2 = User("Alice", "Kohnu", "Quality Engineer")
user_2.describe_user()
user_2.greet_user()
user_2.increment_login_attempts()
user_2.reset_login_attempts()
