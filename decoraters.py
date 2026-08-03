import time
from functools import wraps

def exc_time(fnx):
    @wraps(fnx)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fnx(*args,**kwargs)
        end_time = time.time()
        final_time = end_time-start_time
        print(f"Final Execution time is: {final_time * 1000:.2f} ms")
        return result
    return wrapper
    