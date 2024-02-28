myList = [1, 2, 3, 4, 5]

temp = myList[0]
myList[0] = myList[-1]
myList[-1] = temp

print(myList)