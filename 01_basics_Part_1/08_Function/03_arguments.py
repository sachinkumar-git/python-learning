# default arguments

def greet(name, message = "Good Morning"): # default arguments → message = "Good Morning"
    print(name, message)

greet("Vishwa")

#  keyword arguments 

def gree(name, age, message): 
    print(message, name, "Your age is", age )

gree(age = 99 ,message="Hello", name="Vishwa" ) # keyword arguments advantage is can pass argument in any order 

# positional arguments 

def add_numbers(x,y):
    print("x",x)
    print("y", y)
    print(x+y)

add_numbers(5,6)


# one function for different arguments 
def sum_numbers(*args):
    print(type(args))
    print(args)

    sum = 0
    for num in args :
        sum += num 
    return sum 
print(sum_numbers(1,2,3,4,5))

#  for better understanding 

def fn(a,b, *args):

    print(a)
    print(b)
    print(args)
    print(*args)

fn(5,6,7,8,9)