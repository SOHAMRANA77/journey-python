import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Define a function that simulates some work
def function(s):
    print(f"sleeping for {s}sec")
    time.sleep(s)
    print(f"{s}sec done")
    """lots
        of
        code
    """
    return f"function({s})"


# Sequential execution using the function
def main():
    # Start time
    time1 = time.perf_counter()
    print("# normal zindagi")
    function(4)
    function(2)
    function(3)
    # end  time
    time11 = time.perf_counter()
    # calculate time to execute
    print(time11 - time1)


# Multithreading execution using threads
def multithreading_execution():
    time2 = time.perf_counter()
    print("\n# mentos Multithreading zindagi")
    #   this will execute the code and move ahead while running in background
    t1 = threading.Thread(target=function, args=[4])
    t2 = threading.Thread(target=function, args=[2])
    t3 = threading.Thread(target=function, args=[3])

    t1.start()
    t2.start()
    t3.start()
    time21 = time.perf_counter()
    print(time21 - time2)

    time3 = time.perf_counter()
    print("\n# mentos Multithreading zindagi")
    t1 = threading.Thread(target=function, args=[4])
    t2 = threading.Thread(target=function, args=[2])
    t3 = threading.Thread(target=function, args=[3])

    t1.start()
    t2.start()
    t3.start()
    # this code will make sure that all the thread complete their work
    t1.join()
    t2.join()
    t3.join()
    time31 = time.perf_counter()
    print(time31 - time3)


# with ThreadPoolExecutor(max_workers=1) as executor:
def pooling_demo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(function, 6)
        future2 = executor.submit(function, 5)
        future3 = executor.submit(function, 4)

        print(future1.result())
        print(future2.result())
        print(future3.result())
        print("\n")

        Tlist = [5, 2, 1, 9, 3, 1, 4]
        results = executor.map(function, Tlist)
        for result in results:
            print(result)


pooling_demo()
