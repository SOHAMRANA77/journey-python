class Employee:
    # Class variables
    company_name = "Apple"  # Default company name
    num_of_emp = 0  # Total number of employees in the company

    def __init__(self, name):
        # Instance variables
        self.name = name
        self.raise_amount = 500  # Default raise amount
        Employee.num_of_emp += 1  # Increment total number of employees

    def show(self):
        # Display employee details
        print(f"The name of the employee is {self.name}")
        print(f"Company: {self.company_name}")
        print(f"Raise amount: {self.raise_amount}%")

# Create an instance of Employee
a = Employee("Soham")

# Change the company name for this employee
a.company_name = "Rana Inc"

# Display employee details
a.show()

# Change the default company name
Employee.company_name = "INFO-SYS"

# Display the updated default company name
print(Employee.company_name)

# Create another instance of Employee
b = Employee("Sohyem")

# Change the raise amount for this employee
b.raise_amount = 10000

# Display employee details
b.show()

# Create one more instance of Employee
c = Employee("Soham")

# Change the company name for this employee
c.company_name = "Rana Inc"

# Display employee details
c.show()
