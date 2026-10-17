t = (10, 20)
print(t) # Extra space here

list1 = list(t)
print(list1, type(list1))
list1[0] = 50
print(list1)

tup =tuple(list1)
print(tup, type(tup))