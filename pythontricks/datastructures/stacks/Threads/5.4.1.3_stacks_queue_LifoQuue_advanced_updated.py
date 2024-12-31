import threading
from queue import LifoQueue
import random
import time


# Producer function
def production(thread_id):
    while nums_q:
        if not stack.full() and nums_q:
            item = nums_q.pop()
            stack.put(item)
            print(f"Producer-{thread_id} produced: {item}")


# Consumer function
def consuming(thread_id):
    while True:
        if stack.empty():
            # Stop if all producers are done and stack is empty
            if not nums_q:
                break
        else:
            item = stack.get()
            counter.put(item)
            print(f"Consumer-{thread_id} consumed: {item}")

if __name__ == '__main__':
    # Create a shared LifoQueue
    time1 = time.time()
    stack = LifoQueue(maxsize=5)
    counter = LifoQueue()
    # Number of producers and consumers
    num_producers = 2
    num_consumers = 2

    # Items to be produced
    production_range = 6
    nums_q = list(range(1, production_range * num_producers * 2 + 1))
    random.shuffle(nums_q)



    # Create and start producer threads
    producer_threads = []
    for i in range(num_producers):
        thread = threading.Thread(target=production, args=(i,))
        producer_threads.append(thread)
        thread.start()

    # Create and start consumer threads
    consumer_threads = [threading.Thread(target=consuming, args=(i,)) for i in range(num_consumers)]
    for c in consumer_threads:
        c.start()

    # Wait for all producer threads to finish
    for thread in producer_threads:
        thread.join()
    # Wait for all consumer threads to finish
    for thread in consumer_threads:
        thread.join()

    print(f' -- Count: {counter.qsize()}')
    print(f' -- Stack Empty: {stack.empty()} size:{stack.qsize()}')
    print(f'All producers and consumers have finished in {time.time() - time1} sec')  #0.026001453399658203 sec
