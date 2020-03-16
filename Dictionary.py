dict_employee = {'id': 1, 'name': 'radek', 'designation': 'Developer'}
print(f'Original Dictionary : {dict_employee}')
dict_employee['salary'] = 1000
print(f'Dictionary after adding new field : {dict_employee}')
del dict_employee['salary']
print(f'Dictionary after deleting salary : {dict_employee}')

# Iterating through Key and Value pair

for key, value in dict_employee.items():
    print(f'Key is : {key} & Value is : {value}')

for key, value in enumerate(dict_employee):
    print(f'Key is : {key} & Value is : {value}')

dict_employee.update({'id': 2, 'name': dict_employee['name'][-1::-1]})
print(f'Dictionary Multiple Updates : {dict_employee}')

