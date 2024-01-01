import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappop(heap)
heapq.heappop(heap)

print(heap)

list1 = [1,3,5,2,4,6]
heapq.heapify(list1)
heapq.heappushpop(list1, 89)
heapq.heapreplace(list1, 100)
print(heapq.nsmallest(2, list1))
print(heapq.nlargest(2, list1))

print(list1)

list2 = [(1,'ria'),(4,'sia'),(3,'gia')]
heapq.heapify(list2)

print(list2)

for i in range(len(list2)):
    print(heapq.heappop(list2))