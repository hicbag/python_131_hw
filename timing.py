import time 

def calculate_time(f):
    '''Creates wrapper to start a timer before the function starts and end it after the function is finished to get the time elapsed''' 
    def exectime(*args, **kwargs):
        start = time.time()
        value = f(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f"Total time {total:.0f}")
    return exectime
