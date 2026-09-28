# remove element from the list

arr = [3,5,2,1,9]
arr.remove(1) # element that has to remove should be in the bracket
print(arr)

# in case of dublicate element

arr = [3,5,2,1,9,1,8,1]
arr.remove(1) # it will remove the first occurance of one not all the other 1's
print(arr)

# pop method

arr = [3,1,7,9,11,23,45]
print(arr.pop()) #it will remove the last element from the list
print(arr)
print(arr.pop(2)) #it will remove the element at index 