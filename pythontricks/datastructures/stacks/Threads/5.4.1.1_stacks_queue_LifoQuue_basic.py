


import threading
from asyncio import timeout
from queue import LifoQueue
import random
import time
from threading import Thread

## stack.qsize()
## stack.empty()
## stack.full()

# Create a shared LifoQueue
stack = LifoQueue()

def producer():
    for i in range(50):
        print(f'\nProducing product {i}')
        stack.put(i)
        #time.sleep(0.00001)

def consumer():
    for _ in range(5):
        item = stack.get()
        print(f'\nConsuming product {item}')

consumerThread = Thread(target=consumer)
producerThread = Thread(target=producer)

producerThread.start()
consumerThread.start()
producerThread.join()
consumerThread.join()
print("All producers and consumers have finished.")