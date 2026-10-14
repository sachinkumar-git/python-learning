# def even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
    
# print(even(2))

# def prime(n):
#     if n < 2:
#         return False
#     else:
#         is_prime = True  
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         # Yeh return loop se bahar hona chahiye
#         return is_prime

# n = prime(2)

# if n: # Direct check (n == True likhne ki zarurat nahi)
#     print("is prime")
# else:
#     print("is not prime")


# def findMax (a,b,c):
#     if a>= b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else :
#         return c
    
# print(findMax(6,9,1))

# def sum (n):
#     total = 0

#     for i in n:
#         total = total + i
#     return total

# my_list= [2,3,4,5]

# print(sum(my_list))


# def largest (n) :
#     max = 0
#     for i in n :
#         if i >= max :
#             max = i
        
#     return max

# my_list= [2,9,4,5]

# print(largest(my_list))
        


def reverse_string(s):
    return s[::-1] # [start:stop:step] -1 step matlab piche se chalna

print(reverse_string("Sachin")) # Output: nihcaS


def is_palindrome(s):
    # Case sensitivity handle karne ke liye lower() use karein
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Madam")) # Output: True