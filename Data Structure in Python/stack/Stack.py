# Stack using list
stack = []

def push():
    n = input("enter element into stack ")
    stack.append(n)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)

while True:
    a = input("Press 1 to insert 2 to remove data from stack 3 to stop ")
    if a == "1":
        push()
    elif a == '2':
        pop()
    elif a == '3':
        break
    else:
        print("wrong input")

# implement stack using modules
import collections

stack = collections.deque()
stack.append(10)
stack.append(10)
stack.append(30)
print(stack)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)
stack.get()
stack.get()
stack.get()
stack.get(timeout=1)
    