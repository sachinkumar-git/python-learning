# string single line 
name = 'vishwa'
city = "Bangalore"

# string multiline 
country = '''India'''
country = '''India is my country
i leave in india '''

#  indexing from left to right [0 to length of dtring -1]
name = "Vishwa Mohan"
print(name[3])

#  indexing from right to left [-1 to length of dtring -1]
print(name[-1]) 


#  immutable string
# str = "Vishwa Mohan"
# str[0] = 'X' # it will not change the string 

# string concatination 
first_name = "sachin "
last_name = "kumar"

complete_name = first_name + last_name
print(complete_name)

#  length of the string 
print (len(complete_name)) 


# string slicing
str = 'Vishwa Mohan'
print(str[2:5])

#  start from index to till end
print(str[2: ])

# start from 0 till index 
print(str[ :7])

# print complete strings 
print(str[ : ])

# to convert into upper and lower case
str = "Vishwa"
print(str.upper())
print(str.lower())

# capitalize (means first letter capital)
print(str.capitalize())

# replace method
str = "Hello dear, I am very good, I am very nice, I am wow"
print(str.replace("I am", "We are"))
print(str.replace("I am", "We are", 2))


# string Escape Character

print("hello \n world")
print("hello\tWorld")
print("hello \"World\"")