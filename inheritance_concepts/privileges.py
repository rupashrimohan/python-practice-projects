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


class Privileges:
    """This class contain info about privileges of each user"""

    def __init__(self):
        """Initializes the attributes"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Displays the admin previleges"""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """A Class that represets admin info"""

    def __init__(self, first_name, last_name, position="Admin"):
        "Initialize the attributes"
        super().__init__(first_name, last_name, position)
        self.privilege = Privileges()


admin_user = Admin("Rupashri", "Mohan")
admin_user.describe_user()
admin_user.privilege.show_privileges()
