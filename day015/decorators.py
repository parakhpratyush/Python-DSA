# With decorator — adds behavior
def make_loud(func):
    def wrapper():
        print("=" * 30)
        func()           # original function runs here
        print("=" * 30)
    return wrapper

@make_loud
def greet():
    print("Hello Parakh")

greet()

# ==============================

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

@timer
def fast_function(n):
    return sum(range(n))

slow_function()         
print(fast_function(1000000))  

# ==================================

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def multiply(a, b):
    return a * b

add(3, 4)
multiply(5, 6)