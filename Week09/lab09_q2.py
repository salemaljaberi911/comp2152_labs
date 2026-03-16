# ============================================================
#  WEEK 09 LAB — Q2: SEQUENTIAL vs THREADED EXECUTION
#  COMP2152 — Salem Aljabri
# ============================================================

import threading
import time


def simulate_task(name, duration, lock):
    lock.acquire()
    print(f"[START] {name}")
    lock.release()

    time.sleep(duration)

    lock.acquire()
    print(f"[DONE]  {name} ({duration}s)")
    lock.release()


def run_sequential(tasks, lock):
    for name, duration in tasks:
        simulate_task(name, duration, lock)


def run_threaded(tasks, lock):
    threads = []

    for name, duration in tasks:
        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    print("=" * 60)
    print("  SEQUENTIAL vs THREADED EXECUTION")
    print("=" * 60)

    breakfast_tasks = [
        ("Brew Coffee", 3),
        ("Toast Bread", 2),
        ("Fry Eggs", 4)
    ]

    lock = threading.Lock()

    print("\n--- Running SEQUENTIALLY ---")
    start = time.time()
    run_sequential(breakfast_tasks, lock)
    sequential_time = time.time() - start
    print(f"Sequential time: {sequential_time:.2f} seconds")

    print("\n--- Running with THREADS ---")
    start = time.time()
    run_threaded(breakfast_tasks, lock)
    threaded_time = time.time() - start
    print(f"Threaded time: {threaded_time:.2f} seconds")

    if threaded_time > 0:
        print(f"\nSpeedup: {sequential_time / threaded_time:.2f}x faster with threads!")

    print("\n" + "=" * 60)