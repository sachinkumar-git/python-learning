# Q-1

# def greet():
#     return "hello, python Learner"

# print(greet())


# Q-2

# def square (num):
#     return num**2

# print(square(2))

# Q-3

# def full_name (first, last):
#     return first + " " + last

# print(full_name("sachin","kumar"))

# def full_name (first, last):
#     return f" {first} {last}"

# print(full_name("sachin","kumar"))


# Q-4
# def  calculate_area (length , width=10):
#     return length * width

# print(calculate_area(5,6))


# Q-5
# addd = lambda a,b: a + b

# print(addd(4,5))

# Q-6

# square = lambda x: x*x
# list1 = [1,2,3,4,5]

# print(list(map(square,list1)))


def sum_of_digit(n) :
    if n==0:
        return 0
    return  n%10 + sum_of_digit(n//10)

print(sum_of_digit(123))


# def safe_divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     else:
#         return a / b

# # Testing the function
# print(safe_divide(10, 2))  # Output: 5.0
# print(safe_divide(10, 0))  # Output: Cannot divide by zero