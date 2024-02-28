0,1,1,2,3,5,8,13

def Fibonacci(count):
  n1, n2 = 0, 1
  print(n1, end=' ')
  print(n2, end=' ')
  count = count-2
  while(count>=0):
    n3 = n1+n2
    print(n3, end=' ')
    n1=n2
    n2=n3
    count = count-1
  


count = int(input("Enter number of count : "))
Fibonacci(count)

