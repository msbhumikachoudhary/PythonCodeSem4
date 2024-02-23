def Armstrong(num):
  lengthOfNum = len(str(num))
  sum = 0
  temp = num
  while(temp > 0):
    digit = temp % 10 
    sum = sum + digit ** lengthOfNum
    temp = temp // 10

  if(num == sum):
    print("Armstrong")
  else:
    print("Not Armstrong")

Armstrong(407)
Armstrong(663)

# 407 / 40 / 4
# 7 = 0+7**3 = 343
# 0 = 343 + 0**3 = 343+0 = 343
# 4 = 343 + 4**3 = 343 + 64 = 407

# 663 / 66 / 6
# 3 = 0+3**3 = 0+27 = 27
# 6 = 27 + 6**3= 27+216 = 243
# 6 = 243 + 6**3 = 243 + 216 = 459