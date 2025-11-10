#timing_decorator.py


import time


#what will do is that how much time it will take to do this function
def timing(func):
    
    def wrapper(*args, **kwargs):
        print("wrapper started")

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"function took: {end_time - start_time:.5f}s")

        print("wrapper finished")
        pass

    return wrapper


@timing
def do_something():
    print("starting..")
    time.sleep(5)
    print("finished")



do_something()
