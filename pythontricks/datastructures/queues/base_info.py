# list - Terribly slooooow queues
"""
It is possible to use a regular list a queue but not ideal from performance perspective
-Slow because inserting and deleting an element at the begining requires shifting all other elements by one , requiring O(n) time




"""

lq = [i for i in range(1,20)]

print(lq)
# careful: this is slow!
el = lq.pop(0)
print(el)
print(lq)

#----------------------------------------------
# collections.deque  - Fase and Robust Queues
""" deque implements Double ended queue that supports adding and removing elements from either end in O(1) time.

This surves as both stack and queue

"""

from collections import deque
dq= deque()
dq.append('eat')
dq.append('sleep')
dq.append('code')

print(dq)
print(dq.popleft())
print(dq.pop())
#------------------------------------------------

# queue.Queue Locking semantics for parallel computing.
from queue import Queue
q= Queue()
q.put('getup')
q.put('run')
q.put('reach')

print(q.get()) # getup
print(q.get_nowait())

#----------------------------------
# multiprocessing.queue  - Shared Job Queues





