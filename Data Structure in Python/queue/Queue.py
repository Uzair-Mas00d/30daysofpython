# queue using list
queue = []

def insert():
    n = input('enter number to insert into queue')
    queue.append(n)
    print(queue)

def remove():
    if not queue:
        print('empty queue ')
    else:
        queue.pop(0)
        print(queue)
def display():
    print(queue)

while True:
    choice = int(input('1 to insert 2 to remove 3 to display 4 to stop '))
    if choice == 1:
        insert()
    elif choice == 2:
        remove()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('wrong')

# queue using deque()
import collections
queue = collections.deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)

queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
print(queue)
queue.pop()
queue.pop()
queue.pop()
print(queue)

import queue
queue = queue.Queue()
queue.put(10)
queue.put(20)
queue.put(30)
print(queue)
queue.get()
queue.get()
queue.get()
queue.get(timeout=1) # or this queue.get_nowait() 
print(queue)