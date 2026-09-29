# unary operator 

# left shift
num = 5
print(num<<1)

num = 14
print(num<<1)

#  right shift 
print(num>>1)

# identity operator 

x = 5
y = 5
print(x is y) # is refer to  identity operator which help us to find they pointing to same address or not

arr1 = [1,2,3]
arr2 = [1,2,3]

print (arr1 is arr2)
print (arr1 is not arr2)

# membership
my_list = [ 1,2,3,4,5]
print (5 in my_list)  # to check 5 is in the list or not it will check the number is present in list or not 
print (7 in my_list)
print (5 not in my_list) # reverse the result 