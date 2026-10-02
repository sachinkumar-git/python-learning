#  write a python to count the number of vowels in a given string 

str = input("Please provide the string")

count = 0

for ch in str :
    if ch.lower () in ['a','e','i','o','u'] :
        count +=1

print ("total count of vowel is ", count)