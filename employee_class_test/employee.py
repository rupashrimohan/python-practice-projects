class Employee:
    """An Employee class with some info"""

    def __init__(self, first, last, annual_salary):
        """Initalizes the employee class attributes"""
        self.first = first
        self.last = last
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_amount=None):
        """Calculate the annual_salary based on raise amount"""
        if raise_amount:
            self.updated_salary = self.annual_salary + raise_amount
        else:
            self.updated_salary = self.annual_salary + 5000
        print(f"The updated salary is {self.updated_salary}")
