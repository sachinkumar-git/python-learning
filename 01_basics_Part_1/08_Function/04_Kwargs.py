def display_info(**kwargs):
  print(kwargs)
  print(type(kwargs))

  for key, value in kwargs.items():
    print(key ," -> " ,value)

display_info(name="Vishwa", age=99, city = "Bangalore")


def func (a, b, *args, **kwargs):
  print(a)
  print(b)
  print(args)
  print(kwargs)


func(5,6,7,8,9,name="Vishwa", age=99)