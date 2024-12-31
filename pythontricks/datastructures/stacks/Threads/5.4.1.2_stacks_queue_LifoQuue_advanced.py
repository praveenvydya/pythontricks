


import threading
from queue import LifoQueue
import random
import time

## stack.qsize()
## stack.empty()
## stack.full()

# Create a shared LifoQueue
stack = LifoQueue(maxsize=5)
counter = LifoQueue()
producers_count = consumers_count =3
production_range = 6
consumption_range = 5
nums = list(range(1,production_range*producers_count +1))


# item = random.sample(range(1, 18+1), 1)
# Define the producer function
def production(thread_id):
    for _ in range(production_range):  # Each producer will produce 5 items
        #item = random.randint(1, 18)  # Random data
        random.shuffle(nums)
        item =nums.pop()
        stack.put(item)  # Push to the stack
        print(f"Producer-{thread_id} produced: {item}")

        time.sleep(random.uniform(0.1, 0.5))  # Simulate varying production time

# Define the consumer function
def consuming(thread_id):
    for _ in range(consumption_range):  # Each consumer will consume 5 items
        item = stack.get()  # Pop from the stack
        print("")
        counter.put(item)
        print(f"Consumer-{thread_id} consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate varying consumption time

# Number of producers and consumers
num_producers = producers_count
num_consumers = consumers_count

# Create and start producer threads
producer_threads = []
for i in range(num_producers):
    thread = threading.Thread(target=production, args=(i,))
    producer_threads.append(thread)
    thread.start()

# Create and start consumer threads
consumer_threads = []
for i in range(num_consumers):
    thread = threading.Thread(target=consuming, args=(i,))
    consumer_threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in producer_threads:
    thread.join()

for thread in consumer_threads:
    thread.join()

print(f' Count: {counter.qsize()}')
print(f' Stack Empty: {stack.full()} size:{stack.qsize()}')
print("All producers and consumers have finished.")