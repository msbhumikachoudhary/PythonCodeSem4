def Factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact = fact * i
  print(fact)

n = int(input("Enter a number : "))
Factorial(n)
# Factorial(5)

