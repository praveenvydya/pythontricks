#
q = []
q.append((2,'code'))
q.append((1,'eat'))
q.append((3,'sleep'))

q.sort(reverse=True)

while q:
    item = q.pop()
    print(item)

#-------------------------------
# heapq - binary heap implementation backed by plain list
import heapq
q2 = []
heapq.heappush(q2,(2,'brush'))
heapq.heappush(q2,(1,'get'))
heapq.heappush(q2,(3,'walk'))

while q2:
    item = heapq.heappop(q2)
    print(item)

#-----------------------------------
# PriorityQueue - Beautiful Priority queues - uses heapq internally
# Class based interface
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2,'two'))
pq.put((1,'one'))
pq.put((3,'three'))

while not pq.empty():
    item = pq.get()
    print(item)
