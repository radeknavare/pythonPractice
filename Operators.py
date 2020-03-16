# Floor division operator

print("Floor Division : 6.33 divided by 3 is " + str(6.33//3))
print("Floor Division : -6.33 divided by 3 is " + str(-6.33//3))

# Exponential Operator

print("\n5 ** 3 : " + str(5 ** 3))

# Escape Sequence

print(r"Escaping \n using raw strings")

# String repeat operator

print(5 * "Repeated 5 times\n")

# Concat string without + operator

print('Every ' 'word ' 'in ' 'this ' 'sentence ' 'is ' 'concatenated ' 'with ' 'single ' 'quotes ')
Str = "Good"
# print(Str 'Morning') not allowed

# Access String in reverse order using negative index

str = "reverse"
print("Last character of " + str + " is " + str[-1])

# String slicing

str = "Slice it"
print(str[0:2])
print(str[:2] + str[2:])

# Strings are immutable

str = "immutable"
# str[0] = 'r' # not allowed
# Traceback (most recent call last):
#   File "/home/kedarnavare/PycharmProjects/Practice/Operators.py", line 38, in <module>
#     str[0] = 'r'
# TypeError: 'str' object does not support item assignment


# String length

print(len(str))

