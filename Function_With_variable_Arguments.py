def add_numbers(*args, **kwargs):
    print(args)
    print(kwargs)


person_employee = {"name": "Radek", "age": 23}
number_list = [1, 2, 3, 4, 5]
add_numbers('1', '2', '3', '4', name="Radek", age=23)
add_numbers(*number_list, **person_employee)
