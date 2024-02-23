def PerfectNumber(num):
  sum = 0
  for i in range(1, num):
    if(num%i==0):
      sum = sum + i
  if(sum == num):
    print("Perfect No")
  else:
    print("Not Perfect No")

PerfectNumber(25)