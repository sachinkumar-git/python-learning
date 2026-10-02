#  write a python program to find the sum of all even number between 1 to 20

sum = 0
for i in range (1,21) :
    if (i%2==0) :
      sum = sum + i
print ("Sum of even numbers are ",sum)

