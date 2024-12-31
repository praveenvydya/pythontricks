


import threading
from asyncio import timeout
from multiprocessing import Process,Queue
import random
import time
from threading import Thread

## stack.qsize()
## stack.empty()
## stack.full()



def producer(q):
    for i in range(5):
        print(f'\nProducing product {i}')
        q.put(i)
        #time.sleep(0.1)

def consumer(q):
    for _ in range(5):
        item = q.get()
        print(f'\nConsuming product {item}')
        #time.sleep(0.1)

# using fork start

if __name__=='__main__':
    queue = Queue()
    consumerThread = Process(target=consumer,args=(queue,))
    producerThread = Process(target=producer,args=(queue,))

    producerThread.start()
    consumerThread.start()
    producerThread.join()
    consumerThread.join()
    print("All producers and consumers have finished.")