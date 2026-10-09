#Lambda functions

func = lambda x : x+10

print(func(5))


add = lambda a , b : a+b

print(add(5,6))

def myFunc() :
  #return a new function
  return lambda msg : print(msg)

myFunc()("Hello World")