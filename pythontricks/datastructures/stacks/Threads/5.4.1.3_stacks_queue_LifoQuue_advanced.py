import threading
from queue import LifoQueue
import random
import time


# Producer function
def production(thread_id):
    #global nums # to declare variable is being referred from global scope. To avoid this you can pass nums to production method line @53
    while nums:
        stack_lock.acquire()
        try:
            if not stack.full() and nums:
                item = nums.pop()
                stack.put(item)
                print(f"Producer-{thread_id} produced: {item}")
        finally:
            stack_lock.release()
       # time.sleep(random.uniform(0.1, 0.5))  # Simulate varying production time

# Consumer function
def consuming(thread_id,ns):
    while True:
        stack_lock.acquire()
        try:
            if stack.empty():
                # Stop if all producers are done and stack is empty
                if not nums:
                    break
            else:
                item = stack.get()
                counter.put(item)
                print(f"Consumer-{thread_id} consumed: {item}")
        finally:
            stack_lock.release()
        #time.sleep(random.uniform(0.1, 0.5))  # Simulate varying consumption time


if __name__=='__main__':
    time1 = time.time()
    # Create a shared LifoQueue
    stack = LifoQueue(maxsize=5)
    stack_lock = threading.Lock()  # Lock for synchronizing stack operations
    counter = LifoQueue()
    # Number of producers and consumers
    num_producers = 2
    num_consumers = 2

    # Items to be produced
    production_range = 6
    nums = list(range(1, production_range * num_producers * 2 + 1))
    random.shuffle(nums)

    # Create and start producer threads
    producer_threads = []
    for i in range(num_producers):
        thread = threading.Thread(target=production, args=(i,))
        producer_threads.append(thread)
        thread.start()

    # Create and start consumer threads
    consumer_threads = [threading.Thread(target=consuming, args=(i,nums,)) for i in range(num_consumers)]
    for c in consumer_threads:
        c.start()
    # for i in range(num_consumers):
    #     thread = threading.Thread(target=consuming, args=(i,))
    #     consumer_threads.append(thread)
    #     thread.start()

    # Wait for all producer threads to finish
    for thread in producer_threads:
        thread.join()
    # Wait for all consumer threads to finish
    for thread in consumer_threads:
        thread.join()

    print(f' -- Count: {counter.qsize()}')
    print(f' -- Stack Empty: {stack.empty()} size:{stack.qsize()}')
    print(f'All producers and consumers have finished in {time.time() - time1} sec')  #0.026001453399658203 sec

