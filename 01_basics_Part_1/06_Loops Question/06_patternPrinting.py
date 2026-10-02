'''
python program to print pattern 

*
**
***
****
*****
'''

for row in range(5) :
    for j in range (row+1):
        print("*",end="")
    print()