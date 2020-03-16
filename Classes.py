class Employee:

    company_name = 'Zensoft'
    _private_variable = 'this is private variable'

    def __init__(self, fname, lname, ctc):
        self.fname = fname
        self.lname = lname
        self.ctc = ctc
        self.email = fname + '.' + lname + '@instazen.com'

    def get_full_name(self):
        return f'{self.fname} {self.lname}'

    def get_ctc(self):
        return f'{self.ctc}'

    def apply_raise(self):
        self.ctc = self.ctc + (self.ctc * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        cls.company_name = "Instazen"

    @staticmethod
    def sample_static_method():
        print("In static method")

    def __private_method(self):
        print("This private method is not accessible in derived classes")


class Developer(Employee):
    def get_full_name(self):
        return self.fname

    def __init__(self,fname, lname, ctc, skills):
        super().__init__(fname, lname, ctc)
        self.skills = skills


class Manager(Employee):

    def __init__(self, fname,  lname, ctc, employees=None):
        super().__init__(fname, lname, ctc)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def _view_employees(self):
        for emp in self.employees:
            print(emp.get_full_name())


emp1 = Employee('Kedar', 'Navare', 100000)
Employee.set_raise_amount(0.1)
emp1.apply_raise()
print(emp1.get_ctc())

emp2 = Employee('Shashank', 'Bharadiya', 200000)
Employee.set_raise_amount(.8)
emp2.apply_raise()
print(emp2.get_ctc())
emp2.company_name = "Zensoft"
print(f'Salary of {emp1.get_full_name()} is {emp1.get_ctc()}.\nHe works in {emp1.company_name}')
print(emp1.sample_static_method())

print(help(Developer))

dev1 = Developer('Pradip','Jadhav', 50000, 'Python')
print(f'Derived class developer name : {dev1.get_full_name()}')
print(f'Developer Skills : {dev1.skills}')
# print(dev1.__private_method())

manager1 = Manager('Sue', 'Smith', 90000, [dev1])
print(f'View employees in classes file : {manager1._view_employees()}')
manager1.add_employees(emp1)
manager1.get_full_name()

