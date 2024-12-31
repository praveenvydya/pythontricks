from multiprocessing import Process, Queue, Lock, Manager
import random
import time

# Define the producer function
def production(process_id,pr, stack, nums, lock):
    for _ in range(pr):  # Each producer will produce `production_range` items
        with lock:
            if nums:
                item = nums.pop(0)  # Safely remove the first element
                stack.put(item)  # Push to the stack
                print(f"Producer-{process_id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate varying production time

# Define the consumer function
def consuming(process_id, cr, stack, counter, lock):
    for _ in range(cr):  # Each consumer will consume `consumption_range` items
        with lock:
            if not stack.empty():
                item = stack.get()  # Pop from the stack
                counter.put(item)  # Add to counter queue
                print(f"Consumer-{process_id} consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate varying consumption time

if __name__ == "__main__":
    # Shared resources
    stack = Queue(maxsize=5)  # Shared stack (LifoQueue functionality)
    counter = Queue()  # For tracking consumed items
    lock = Lock()  # Lock for synchronizing access to shared resources

    # Number of producers and consumers
    producers_count = consumers_count = 3
    production_range = 6
    consumption_range = 5

    # Use Manager to share the nums list
    with Manager() as manager:
        nums = manager.list(range(1, production_range * producers_count + 1))
        random.shuffle(nums)  # Shuffle the list

        # Create and start producer processes
        producers = []
        for i in range(producers_count):
            process = Process(target=production, args=(i, production_range, stack, nums, lock))
            producers.append(process)
            process.start()

        # Create and start consumer processes
        consumers = []
        for i in range(consumers_count):
            process = Process(target=consuming, args=(i,consumption_range, stack, counter, lock))
            consumers.append(process)
            process.start()

        # Wait for all producer processes to finish
        for process in producers:
            process.join()

        # Wait for all consumer processes to finish
        for process in consumers:
            process.join()

        print(f"Count of consumed items: {counter.qsize()}")
        print(f"Is the stack empty? {stack.empty()} | Stack size: {stack.qsize()}")
        print("All producers and consumers have finished.")
