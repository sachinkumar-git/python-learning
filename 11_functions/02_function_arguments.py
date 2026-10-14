# default arguments 

def add(a, b, plus=0):  # parameters
    x = a + b + plus
    return x


c = add(3, 5, 2) # NOTE arguments
print(c)

# keyword arguments

c1 = add(b=5, a=3)