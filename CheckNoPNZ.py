def checkNo(num):
  if num > 0:
    print("Positive Number")
  elif num < 0:
    print("Negative Number")
  else: 
    print("Zero")

num = int(input("Enter Number: "))
checkNo(num)