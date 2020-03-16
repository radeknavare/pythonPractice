originalList = []
for i in range(10):
    originalList.append(i)
print("Original List : " + str(originalList))
print("Stack representation of originalList")
while len(originalList) > 0:
    print(originalList.pop())
