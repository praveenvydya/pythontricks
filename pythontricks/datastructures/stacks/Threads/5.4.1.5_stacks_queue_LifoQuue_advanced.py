import threading
from queue import LifoQueue
import random
import time

# Constants for task priorities
PRIORITY_HIGH = "high"
PRIORITY_MEDIUM = "medium"
PRIORITY_LOW = "low"

# Shared LifoQueue
task_stack = LifoQueue(maxsize=50)

# Lock for synchronized console output
print_lock = threading.Lock()

# Retry queue for failed tasks
retry_stack = LifoQueue(maxsize=20)

# Producer function
def producer(thread_id):
    while True:
        if not task_stack.full():
            priority = random.choices(
                [PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW], weights=[0.5, 0.3, 0.2]
            )[0]
            task = {"task_id": random.randint(1000, 9999), "priority": priority, "data": random.random()}
            task_stack.put(task)
            with print_lock:
                print(f"[Producer-{thread_id}] Created task: {task}")
            time.sleep(random.uniform(0.1, 0.4))  # Simulate task production time
        else:
            with print_lock:
                print(f"[Producer-{thread_id}] Queue full, pausing...")
            time.sleep(1)  # Wait before retrying

# Consumer function
def consumer(thread_id):
    while True:
        try:
            # Fetch a task from the stack
            task = task_stack.get(timeout=2)
            # Simulate task processing
            success = random.random() > 0.2  # 80% chance of success
            with print_lock:
                print(f"[Consumer-{thread_id}] Processing task: {task}")
            time.sleep(random.uniform(0.3, 0.7))  # Simulate variable processing time

            if not success:
                with print_lock:
                    print(f"[Consumer-{thread_id}] Task failed, retrying: {task}")
                retry_stack.put(task)  # Add failed task to retry queue
            task_stack.task_done()
        except Exception:  # Handle empty queue
            with print_lock:
                print(f"[Consumer-{thread_id}] No tasks to process, exiting...")
            break

# Retry consumer to handle failed tasks
def retry_consumer():
    while True:
        try:
            task = retry_stack.get(timeout=5)  # Timeout if no tasks are available
            with print_lock:
                print(f"[RetryConsumer] Retrying task: {task}")
            time.sleep(random.uniform(0.2, 0.5))  # Simulate retry processing
            retry_stack.task_done()
        except Exception:
            with print_lock:
                print("[RetryConsumer] No tasks to retry, exiting...")
            break

# Manager function to monitor queue and dynamically adjust consumers
def manager(consumers, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        queue_size = task_stack.qsize()
        retry_size = retry_stack.qsize()

        with print_lock:
            print(f"[Manager] Queue size: {queue_size}, Retry queue size: {retry_size}")

        # Dynamically add consumers if the queue is large
        if queue_size > 30 and len(consumers) < 6:
            new_consumer = threading.Thread(target=consumer, args=(len(consumers) + 1,))
            consumers.append(new_consumer)
            new_consumer.start()
            with print_lock:
                print("[Manager] Added new consumer.")

        # Remove extra consumers if the queue is small
        if queue_size < 5 and len(consumers) > 2:
            with print_lock:
                print("[Manager] Queue small, reducing consumer load.")
            break  # Stop manager early for simplicity in this demo

        time.sleep(2)  # Monitor every 2 seconds

# Logging thread to track and log queue state
def logger():
    while True:
        with print_lock:
            print(f"[Logger] Queue size: {task_stack.qsize()}, Retry size: {retry_stack.qsize()}")
        time.sleep(3)  # Log every 3 seconds

# Main driver function
def main():
    # Initialize producer threads
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]

    # Initialize consumer threads
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

    # Retry consumer
    retry_thread = threading.Thread(target=retry_consumer)

    # Logging thread
    logging_thread = threading.Thread(target=logger)

    # Start threads
    for p in producers:
        p.start()
    for c in consumers:
        c.start()
    retry_thread.start()
    logging_thread.start()

    # Start manager to dynamically adjust system
    manager_thread = threading.Thread(target=manager, args=(consumers, 20))  # 20-second runtime for manager
    manager_thread.start()

    # Wait for threads to finish
    manager_thread.join()
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
    retry_thread.join()

    with print_lock:
        print("[Main] All tasks completed. System shutting down.")

if __name__ == "__main__":
    main()
