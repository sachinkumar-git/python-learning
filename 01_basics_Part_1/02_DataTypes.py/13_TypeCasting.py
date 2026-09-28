#  implicit typecasting

x = 5 # int 
y = 6.5
result = x+y # but here x changes to float
print(result)


# explicit typecasting

y = '10'
print(type(y))
int_y = int (y)
print(type(int_y))

''' method used for explicit type casting 
str()
int()
float()
'''