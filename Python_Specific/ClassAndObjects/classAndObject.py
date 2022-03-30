# Python Object-Oriented Programming

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}@gmail.com".lower()

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Anagh', 'Kumar')
emp_2 = Employee('Abhishek', 'Tripathi')

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())  # Same as line Below
print(Employee.fullname(emp_1))  # Same as line above
# emp_1.firstName = 'Anagh'
# emp_1.lastName = 'Kumar'


print()
