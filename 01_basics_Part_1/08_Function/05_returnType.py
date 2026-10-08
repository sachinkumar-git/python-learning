def add_numbers(a : int,b : int)-> int : # type of return 
  return a+b

print(add_numbers(5.5,7.7))


# function nesting 
def outer():
  print("Hello from the outer")
# nested function 
  def inner():
    print("Hello from the inner") 

  return inner

fn = outer()
fn()
outer()()