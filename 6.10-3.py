class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str):
        # data = str.split('-')
        # return cls(data[0], data[1], data[2])
        first_name, last_name, salary = str.split('-')
        return cls(first_name, last_name, int(salary))


emp1 = Employee('dm', 'irl', 5000)
emp2 = Employee.from_string('sr-ersh-7000')

print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.salary)
