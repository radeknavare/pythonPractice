# nested_list = [1, 2, [3, 4], 5, [6, [7, [8, 9], 10, 11], 12], 13]
nested_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

newList1 = []


def recursive_flatten(nested_list1):
    # if type(nested_list) == list:

    # recursive_flatten(nested_list)
    if len(nested_list) == 0:
        return 1
    else:
        newList1.append(nested_list.pop(0))
        return recursive_flatten(nested_list)


recursive_flatten(nested_list)
print(newList1)
