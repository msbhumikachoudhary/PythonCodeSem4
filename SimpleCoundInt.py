# def calculate_interest(p, r, t):
#   simple_interest = (p * r * t) / 100
#   compound_interest = p * (1 + r / 100) ** t - 1
#   return simple_interest, compound_interest

p = int(input("Enter principal = "))
r = int(input("Enter rate = "))
t = int(input("Enter time = "))
simple_interest = (p * r * t) / 100
compound_interest = p * (1 + r / 100) ** t - p
print("Simple Interest: ", simple_interest)
print("Compound Interest: ", compound_interest)
