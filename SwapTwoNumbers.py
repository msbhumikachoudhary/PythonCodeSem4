def swapWithTemp(a, b):
  temp = a
  a = b
  b = temp
  print(f"After swapping with temp: a = {a}, b = {b}")

def swapWithoutTemp(a, b):
  a = a + b
  b = a - b 
  a = a - b 
  print(f"After swapping without temp: a = {a}, b = {b}")

x = 5
y = 10
swapWithTemp(x, y)
swapWithoutTemp(x, y)
