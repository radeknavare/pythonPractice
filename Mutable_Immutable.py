first_names = ['Fred', 'George', 'Bill']
last_names = ['Smith', 'Jones', 'Williams']
name_tuple = (first_names, last_names)
print("Before change in mutable list : " + str(name_tuple))

first_names.append('Igor')

print("After change in mutable list ir reflects in immutable tuple : " + str(name_tuple))


def foo(bar):
    """ This is docstring
        This is helpful for explaining the purpose function
    """
    bar = 'new value'
    print(bar)
    # >> 'new value'


answer_list = 'old value'
foo(answer_list)
print(answer_list)


def tuplemodify(tup1=(1, 2, 3), lis1=[1, 2, 3]):
    print(tup1)
    tup1 = (1, 2, 3)
    print(f"Function tuple : {tup1}")
    print(f"Function List : {lis1}")


tup = (4, 5, 6)
lis = [4, 5, 6]
tuplemodify(tup, lis)
print(f"Global tuple : {tup}")
print(f"Global list : {lis}")


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
