from builtins import StopIteration


class EmployeeName:
    def __init__(self, names):
        self.names = names
        self.names_length = len(names)

    def __iter__(self):
        return self

    def __next__(self):
        if self.names_length == 0:
            raise StopIteration
        self.names_length -= 1
        return self.names[self.names_length]

    def reverse(self, sdata):
        for index in range(0, len(sdata)-1):
            yield sdata[index]

emp1 = EmployeeName(["Kedar", "Shashank"])
iter(emp1)
for emp in emp1:
    print(emp)

emp2 = EmployeeName(["Kedar", "Pradip"])
for emp in emp2.reverse(["Kedar", "Pradip"]):
    print(emp)