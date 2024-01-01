# priority queue using list
queue = [10,40,30,20,60]
queue.sort()
print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)

q = [(1, 'alex'),(4, 'asda'), (2, 'asdsad')]
q.sort(reverse=True)
print(q)
print(q.pop(0))

# priorrity queue using queue pacakage
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())