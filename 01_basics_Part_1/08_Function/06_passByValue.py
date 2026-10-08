#Pass by Value

num = 5

def modify_num(num):
  num +=1
  print(num)

modify_num(num)

print("Original num", num)

# Immutable datatypes : Numbers, String, tuple -- Passed by Value