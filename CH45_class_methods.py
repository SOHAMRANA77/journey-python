class Employee:
    Company = "Sohyem"  # Default company name

    def show(self):
        # Display the company name
        print(f"This company name is {self.Company}")

    @classmethod
    def change(cls, new_company):
        # Class method to change the company name
        cls.Company = new_company

# Create an instance of Employee
e = Employee()
e.show()  # Display the initial company name

# Change the company name using the class method
e.change("Rana")
e.show()  # Display the updated company name for the instance

# Access the company name directly using the class variable
print(Employee.Company)

# Change the company name using the class method
e.change("Soham")
e.show()  # Display the updated company name for the instance

# Access the company name directly using the class variable
print(Employee.Company)

# Display the company name for the instance
e.show()
