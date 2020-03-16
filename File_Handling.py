# def count_special_chars():
#     spaces = 0
#     tabs = 0
#     i = 0
#     file = open('file_count_spaces.txt', 'r')
#     for i, line in enumerate(file):
#         tabs += line.count('\t')
#         spaces += line.count(' ')
#     file.close()
#
#     print(f'Lines = {i}')
#     print(f'Spaces = {spaces}')
#     print(f'Tabs = {tabs}')
#
#
# count_special_chars()


def file_replace(oldstring, newstring):
    fileread = open('file_count_spaces.txt', 'r')
    data = []
    data = fileread.read()
    data = data.replace(oldstring,newstring)
    fileread.close()
    filewrite = open('file_count_spaces.txt', 'w')
    filewrite.write(data.replace(oldstring, newstring))
    filewrite.close()


file_replace('yet', 'but')
