#  print 1 to 10 as soon as I get number which is divisible by 4 stop

# break 
for num in range(1,13):
    if (num%4 == 0) :
        break
    print (num)
print (" ")
# continue 
# print only if number is even 
for num in range(1,13):
    if (num%2 != 0) :
        continue
    print (num)

