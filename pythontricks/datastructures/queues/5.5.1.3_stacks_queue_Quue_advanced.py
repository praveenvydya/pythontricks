from asyncio import timeout
from multiprocessing import Queue, Process, Event
import random
import time
import threading

""" NO WORKING """
# Producer function
def production(proc_id,q,ns,q_l):
    while ns:
        q_l.acquire()
        try:
            if not q.full() and ns:
                item = ns.pop()
                q.put(item)
                print(f"Producer-{proc_id} produced: {item}")
                time.sleep(random.uniform(0.1,0.5))
        finally:
            q_l.release_lock()


# Consumer function
def consuming(cons_id,q,st_event):
    while not st_event.is_set() or not q.empty():
        try:
            item = q.get()
            print(f"Consumer-{cons_id} consumed: {item}")
        except multiprocessing.queues.Empty:
            continue



if __name__ == '__main__':
    # Create a shared multiprocessing Queue
    queue = Queue(maxsize=5)
    stop_event = Event()

    q_lock = threading.Lock()
    # Number of producers and consumers
    num_producers = 2
    num_consumers = 2

    # Items to be produced
    production_range = 6
    nums = list(range(1, production_range * num_producers * 2 + 1))
    random.shuffle(nums)
    # Create and start producer processes
    producer_processes = []
    for i in range(num_producers):
        p = Process(target=production, args=(i,queue,nums,q_lock))
        producer_processes.append(p)
        p.start()

    # Create and start consumer processes
    consumer_processes = [Process(target=consuming, args=(i,queue,stop_event)) for i in range(num_consumers)]
    for c in consumer_processes:
        c.start()

    # Wait for all producer processes to finish
    for p in producer_processes:
        p.join()

    stop_event.set()
    # Wait for all consumer processes to finish
    for c in consumer_processes:
        c.join()

    print(f' -- Queue Empty: {queue.empty()} Size: {queue.qsize()}')
    print("All producers and consumers have finished.")
