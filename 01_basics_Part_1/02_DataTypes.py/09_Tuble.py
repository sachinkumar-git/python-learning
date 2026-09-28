# tuple

tup1 = (3,6,1,9,10)
print(tup1)
print(type(tup1))

# construct tuple from any list/string/tuple
t1 = tuple([1,2,4])
print(t1)

# string
t2 = tuple("Vishwa")
t3 = tuple(tup1)

print(t2,t3)

# to make tuple with , used
t = (35,)
print(type(t))

# to count element in tuple

fruits =('apple', 'mango','apple')
print(fruits.count('apple'))

# to find the index
print(fruits.index('mango'))