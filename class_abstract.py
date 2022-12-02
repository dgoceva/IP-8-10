from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f'{self.fname} {self.lname}'

    @abstractmethod
    def salary(self):
        pass


class MontlyEmployee(Employee):
    def create(fname, lname, salary):
        return MontlyEmployee(fname, lname, salary)

    def __init__(self, fname, lname, salary):
        super(MontlyEmployee, self).__init__(fname, lname)
        self.salary = salary

    def salary(self):
        return self.salary

    def __str__(self):
        return f'{self.fname} {self.lname} {self.salary}'


class DayEmployee(Employee):
    def __init__(self, fname, lname, days, daysalary):
        super(DayEmployee, self).__init__(fname, lname)
        self.days = days
        self.daysalary = daysalary

    def salary(self):
        return round(self.daysalary * self.days)

    def __str__(self):
        return f'{super().__str__()} {self.salary()}'


# emp1 = Employee('Ivan', 'Ivanov')
emp1 = MontlyEmployee('Ivan', 'Ivanow', 2000)
print(emp1)
emp2 = DayEmployee('Petyr', 'Petrov', 20, 120)
print(emp2)
emp1 = MontlyEmployee.create('Ivan', 'Ivanow', 2500)
print(emp1)
