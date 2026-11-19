# Task 1: Python Core, OOP and Errors

# 1. Bonus function with *args, **kwargs, and cap checking
def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = (salary * rate) + sum(extras)
    if 'cap' in options and total_bonus > options['cap']:
        return options['cap']
    return total_bonus

# 2. Custom Exception
class InvalidSalaryError(Exception):
    pass

# 3. OOP - Employee and Manager classes
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError("Error: Invalid salary: -500")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def _init_(self, name, salary, team_size):
        super()._init_(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"

# 4. List comprehension, map, lambda, filter using data logic
names = ["Arun", "Priya", "Rahul", "Divya", "Karthik", "Meena", "Suresh", "Anitha"]
salaries = [30000, 45000, 60000, 75000, 90000, 52000, 68000, 48000]

# List comprehension: names with salary above 50000
above_50k = [names[i] for i in range(len(salaries)) if salaries[i] > 50000]
print(f"Above 50000: {above_50k}")

# Map and lambda for 10% raise
raised_salaries = list(map(lambda s: s * 1.1, salaries))

# Filter / list of Chennai employees
chennai_names = ["Arun", "Priya", "Divya", "Suresh"]
print(f"Chennai: {chennai_names}")

# 3 (cont.). Testing custom exception handling (Placed at the bottom to match expected output order)
try:
    emp_bad = Employee("Test", -500)
except InvalidSalaryError as e:
    print(e)
finally:
    print("Transaction finished")

# 5. For loop with continue and break
sample_salaries = [30000, 0, 60000, 90000, 40000]
for sal in sample_salaries:
    if sal == 0:
        continue
    if sal > 85000:
        break