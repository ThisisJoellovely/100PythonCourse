import time

current_time = time.time()
print(current_time) 

# Write your code below 👇
def speed_calc_decorator(function):
  
  def wrapper_function():
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'Function Name:{function.__name__}, run speeed: {end_time-start_time}s')
  
  return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function() 
slow_function()