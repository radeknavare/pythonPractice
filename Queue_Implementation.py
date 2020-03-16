from collections import deque

queue = deque()


for i in range(10):
    queue.append(i)
print("Original Queue : " + str(queue))

print("Queue Elements POP : ")
while len(queue) > 0:
    print(queue.popleft())
