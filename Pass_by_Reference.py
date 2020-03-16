def create_list():
    namelist = [1, 2, 3, 4, 5]
    delete_list_element(namelist)
    print(namelist)


def delete_list_element(namelist):
    namelist.pop()


create_list()
