import threading
from queue import LifoQueue
import random
import time
from datetime import datetime, timedelta

# Constants for task priorities
PRIORITY_HIGH = "high"
PRIORITY_MEDIUM = "medium"
PRIORITY_LOW = "low"

# Shared LifoQueue
task_stack = LifoQueue(maxsize=50)

# Lock for synchronized console output
print_lock = threading.Lock()

# Metrics to track system performance
metrics = {
    "processed_tasks": 0,
    "expired_tasks": 0,
    "failed_tasks": 0,
}

# Graceful termination flag
terminate_system = threading.Event()


# Producer function
def producer(thread_id):
    while not terminate_system.is_set():
        if not task_stack.full():
            priority = random.choices(
                [PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW], weights=[0.5, 0.3, 0.2]
            )[0]
            ttl = datetime.now() + timedelta(seconds=random.randint(5, 15))  # Task expires in 5–15 seconds
            task = {
                "task_id": random.randint(1000, 9999),
                "priority": priority,
                "data": random.random(),
                "ttl": ttl,
            }
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
    while not terminate_system.is_set() or not task_stack.empty():
        try:
            task = task_stack.get(timeout=2)
            if datetime.now() > task["ttl"]:  # Check for expired tasks
                with print_lock:
                    print(f"[Consumer-{thread_id}] Task expired: {task}")
                with metrics_lock:
                    metrics["expired_tasks"] += 1
                continue

            success = random.random() > 0.2  # 80% chance of success
            with print_lock:
                print(f"[Consumer-{thread_id}] Processing task: {task}")
            time.sleep(random.uniform(0.3, 0.7))  # Simulate variable processing time

            if success:
                with metrics_lock:
                    metrics["processed_tasks"] += 1
            else:
                with print_lock:
                    print(f"[Consumer-{thread_id}] Task failed: {task}")
                with metrics_lock:
                    metrics["failed_tasks"] += 1

            task_stack.task_done()
        except Exception:  # Handle empty queue or timeout
            continue


# Task expiration monitoring thread
def expiration_monitor():
    while not terminate_system.is_set():
        current_time = datetime.now()
        expired_count = 0

        # Traverse stack and remove expired tasks
        with task_stack.mutex:
            for i in range(len(task_stack.queue)):
                task = task_stack.queue[i]
                if current_time > task["ttl"]:
                    task_stack.queue[i] = None
                    expired_count += 1

            task_stack.queue = [t for t in task_stack.queue if t is not None]

        with print_lock:
            if expired_count > 0:
                print(f"[ExpirationMonitor] Removed {expired_count} expired tasks.")

        time.sleep(2)  # Check every 2 seconds


# Logging thread for metrics reporting
def logger():
    while not terminate_system.is_set():
        with metrics_lock:
            with print_lock:
                print(f"[Logger] Metrics: {metrics}")
        time.sleep(5)  # Log every 5 seconds


# Main driver function
def main():
    global terminate_system
    global metrics_lock
    metrics_lock = threading.Lock()

    # Initialize producer threads
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]

    # Initialize consumer threads
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]

    # Expiration monitor thread
    expiration_thread = threading.Thread(target=expiration_monitor)

    # Logging thread
    logging_thread = threading.Thread(target=logger)

    # Start threads
    for p in producers:
        p.start()
    for c in consumers:
        c.start()
    expiration_thread.start()
    logging_thread.start()

    try:
        # Keep the system running until user signals termination
        while True:
            user_input = input("Enter 'stop' to terminate the system: ").strip().lower()
            if user_input == "stop":
                terminate_system.set()
                break
    except KeyboardInterrupt:
        terminate_system.set()

    # Wait for all threads to finish
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
    expiration_thread.join()
    logging_thread.join()

    # Print final metrics
    with print_lock:
        print(f"[Main] Final Metrics: {metrics}")
        print("[Main] System shutdown complete.")


if __name__ == "__main__":
    main()
