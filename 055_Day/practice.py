inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decoratir(function):
  
  def wrapper(*args):
    print(f'You called {function.__name__}({args[0]},{args[1]},{args[2]})')
    print(f'It returned: {a_function(args[0],args[1],args[2])}')
  return wrapper 
# TODO: Use the decorator 👇
@logging_decoratir
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])