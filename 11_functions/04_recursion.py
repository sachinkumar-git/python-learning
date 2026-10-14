# ''' 
# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6.....

# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(0) + fib(1)
# fib(3) = fib(1) + fib(2)
# fib(4) = fib(2) + fib(3)
# fib(n) = fib(n-2) + fib(n-1)

# '''

# def fib(n):
#     # Base case of recursion
#     if(n == 0 or n == 1):
#         return n

#     return fib(n-2) + fib(n-1)

# print(fib(6))

# fib(4) + fib(5)
# fib(2) + fib(3) + fib(5)
# fib(0) + fib(1) + fib(3) + fib(5)
# 0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
# 0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2)+ fib(4)
# 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
# 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1


def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step: sum of previous two terms
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pehle n numbers print karne ke liye logic
n_terms = 10
print(f"First {n_terms} Fibonacci numbers:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")