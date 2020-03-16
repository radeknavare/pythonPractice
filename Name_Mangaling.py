class NameMangling:
    __class_variable = "This is class variable"

    def __init__(self):
        self.__fname = 'Kedar'


__global_variable = "global"
nm = NameMangling()
print(nm._NameMangling__fname)
print(dir(nm))
