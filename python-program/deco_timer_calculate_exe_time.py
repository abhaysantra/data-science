# https://realpython.com/primer-on-python-decorators/

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func) # used to preserve identity of waste_some_time()
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):  # here _ used as this variable will not be used in future
        return sum([i**2 for i in range(10000)])

ret_val = waste_some_time(1)
print(f"return value : {ret_val}")