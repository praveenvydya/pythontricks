import threading
from queue import LifoQueue
import random
import time

# Shared LifoQueue for tasks
task_stack = LifoQueue(maxsize=20)

# Lock for safe print operations (optional for cleaner output)
print_lock = threading.Lock()


# Producer function
def producer(thread_id, task_limit):
    for _ in range(task_limit):
        if not task_stack.full():  # Check if the queue is full
            task = {"task_id": random.randint(1000, 9999), "data": random.random()}
            task_stack.put(task)  # Push task onto the stack
            with print_lock:
                print(f"Producer-{thread_id} created task: {task}")
            time.sleep(random.uniform(0.1, 0.3))  # Simulate variable task creation time
        else:
            with print_lock:
                print(f"Producer-{thread_id} waiting (queue full)...")
            time.sleep(0.5)  # Backoff when the queue is full


# Consumer function
def consumer(thread_id):
    while True:
        try:
            task = task_stack.get(timeout=2)  # Timeout if no tasks are available
            with print_lock:
                print(f"Consumer-{thread_id} processing task: {task}")
            time.sleep(random.uniform(0.2, 0.6))  # Simulate variable task processing time
            task_stack.task_done()
        except Exception:
            with print_lock:
                print(f"Consumer-{thread_id} no tasks to process, exiting...")
            break  # Exit when no tasks are available


# Manager function to adjust producers and consumers dynamically
def manager(producers, consumers, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        with print_lock:
            print(f"Manager monitoring... Queue size: {task_stack.qsize()}")

        if task_stack.qsize() > 15 and len(consumers) < 5:
            # Spawn an additional consumer if the queue is too full
            new_consumer = threading.Thread(target=consumer, args=(len(consumers) + 1,))
            consumers.append(new_consumer)
            new_consumer.start()
            with print_lock:
                print("Manager added a new consumer.")

        if task_stack.qsize() < 5 and len(producers) < 3:
            # Spawn an additional producer if the queue is too empty
            new_producer = threading.Thread(target=producer, args=(len(producers) + 1, 10))
            producers.append(new_producer)
            new_producer.start()
            with print_lock:
                print("Manager added a new producer.")

        time.sleep(2)  # Manager monitors every 2 seconds

    with print_lock:
        print("Manager stopping all threads...")


# Main driver function
def main():
    # Initial producers and consumers
    producers = [threading.Thread(target=producer, args=(i, 10)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

    # Start producers and consumers
    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    # Start manager to dynamically adjust threads
    manager_thread = threading.Thread(target=manager, args=(producers, consumers, 15))  # Run manager for 15 seconds
    manager_thread.start()

    # Wait for manager to finish
    manager_thread.join()

    # Wait for all producers to finish
    for p in producers:
        p.join()

    # Wait for all consumers to finish
    for c in consumers:
        c.join()

    with print_lock:
        print("All tasks completed. System shutting down.")


# Run the advanced example
if __name__ == "__main__":
    main()
