import time


def logging_time(func):
    def wrapper(*args, **argkw):
        start = time.time()
        func(*args)
        end = time.time()
        print("waste time %f" %(end-start))
    return wrapper
