class Dog:
    """A simple attempt to model a Dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Represents the sit behavior of a dog"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Represents roll over behavior of a dog"""
        print(f"{self.name} is rolling over.")


# Instantiation
my_dog = Dog("Willie", 6)
print(f"My Dog's name is {my_dog.name}")
print(f"My Dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

# instance no.2
your_dog = Dog("Lucy", 9)
print(f"\nYour Dog's name is {your_dog.name}")
print(f"Your Dog's name is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()
