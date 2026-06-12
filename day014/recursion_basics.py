# 1. Factorial
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

# 2. Fibonacci
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# 3. Sum of array
def array_sum(arr):
    if not arr: return 0
    return arr[0] + array_sum(arr[1:])

# 4. Power function
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp-1)

# 5. Reverse a string
def reverse_string(s):
    if len(s) <= 1: return s
    return reverse_string(s[1:]) + s[0]

# Test all
print(factorial(6))         
print(fib(10))                
print(array_sum([1,2,3,4,5])) 
print(power(2, 8))           
print(reverse_string("PARAKH")) 