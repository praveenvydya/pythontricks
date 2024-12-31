import multiprocessing
from queue import LifoQueue
import random
import time

counter = LifoQueue()
# Producer function
def producer(queue, num_items):
    for _ in range(num_items):
        item = random.randint(1, 100)
        print(f"Produced: {item}")
        queue.put(item)
        #time.sleep(random.uniform(0.1, 0.5))  # Simulate variable production time

# Consumer function
def consumer(queue, stop_event):
    while not stop_event.is_set() or not queue.empty():
        try:
            item = queue.get(timeout=1)  # Wait for item or timeout
            print(f"Consumed: {item}")
            counter.put(item)
        except multiprocessing.queues.Empty:
            continue

if __name__ == '__main__':
    num_items = 20
    queue = multiprocessing.Queue()
    stop_event = multiprocessing.Event()

    # Start producer process
    producer_process = multiprocessing.Process(target=producer, args=(queue, num_items))
    producer_process.start()

    # Start consumer process
    consumer_process = multiprocessing.Process(target=consumer, args=(queue, stop_event))
    consumer_process.start()

    # Wait for producer to finish
    producer_process.join()

    # Stop consumer if producer has finished
    stop_event.set()

    # Wait for consumer to finish
    consumer_process.join()
    print(f' Count: {counter.qsize()}')
    print(f' -- Queue Empty: {queue.empty()} Size: {queue.qsize()}')
    print("All producers and consumers have finished.")