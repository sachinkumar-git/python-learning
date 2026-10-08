x = 101 # global Variable or global Scope 

def func() :
    x = 102 #local scope 
    print(x)

func()
print(x)