students_details = {'name': 'vishwa','age':21, 'city':"Bangalore"}

print(students_details)
print(type(students_details))

#  in python one is consider as true value
dict1 = {1: "Vishwa", 2:"Mohan", True : "Love"}
print(dict1)
# output → {1: 'Love', 2: 'Mohan'}

dict1 = {3: "Vishwa", 2:"Mohan", True : "Love"}
print(dict1)
# output → {3: 'Vishwa', 2: 'Mohan', True: 'Love'}

# another method then {} curly bracket to create dictonary construction methods
dict1 = dict(name ="Vishwa", age = "Mohan")

# access the element of dictionary
students_details = {'name': 'vishwa','age':21, 'city':"Bangalore"}
print(students_details['name'])
print(students_details['city'])

# to get the list of all the keys and values
print(students_details.keys() )
print(students_details.values())
print(students_details.items())

#  how to add element in dictionary
students_details = {'name': 'vishwa','age':21, 'city':"Bangalore"}
students_details['country'] = 'India'
print(students_details)

# to add one dictionary to other
marks_details = {'English': 100, 'Maths':78, 'Science':92}
students_details.update(marks_details)
print(students_details)

# remove element from the dictionary
print(students_details.pop('city'))
print(students_details)

# it will  remove the last element form the dictionary 
print(students_details.popitem())
print(students_details)

#  use delete keyword to remove  from dictionary
del students_details['age']
print(students_details)

# clear method to clear the entire dictionary
students_details.clear()
print(students_details)