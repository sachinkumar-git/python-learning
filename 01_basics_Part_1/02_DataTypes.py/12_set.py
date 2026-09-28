my_set = {1,2,3,5}
print(my_set)
print(type(my_set))

# set ensure no dublicate elements in set
s1 = {1,4,5,2,1,9,7,4,1}
print(s1)

#  another method to create set is set constructor method 
s2 = set()
print(s2)

s3 = set ({5,6,7})
print(s3)

# how to add element to set
s = set()
s.add(5)
s.add(13)
s.add(5) # dublicate element will not add 
s.add(12)
print(s)

# {13, 12, 5} it is unorder in which order we add it will not createb in that order so its an unorder set 

#  remove from set 
s1 = {3,9,7,4}
print(s1.discard(7))
print(s1)


# FrozenSet : Immutable set
fs = frozenset([1,2,3])
print(fs)
print(type(fs))

fs2 = frozenset({1,2,3})
print(fs2)