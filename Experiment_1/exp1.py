"""
Aim: Demonstrate Various Data Types and Operators in Python.
"""

a = 208
b = 600

print("\nEquation Assignment Operators :\n")
print((a+b)**2 == a**2 + 2*(a*b) + b**2)
print((a-b)**2 == a**2 - 2*(a*b) + b**2)
print((a+b)*(a+b) == 2*(a**2 - b**2)) # Note: Based on your notes, this evaluates to False
print((a+b)*(a-b) == a**2 - b**2)
print(a**3 + b**3 == (a+b)*(a**2 - a*b + b**2))

print("\nBitwise Operations:\n")
print(a|b == (a^b) + (a&b))
print(a^(a&b) == (a|b)^b)
print(b^(a&b) == (a|b)^a)
print((a&b)^(a|b) == a^b)

print("\nAddition:\n")
print((a+b) == (a|b) + (a&b))
print((a+b) == (a^b) + 2*(a&b))

print("\nSubtraction:\n")
print(a-b == (a^(a&b)) - ((a|b)^a))
print(a-b == ((a|b)^b) - ((a|b)^a))
print(a-b == (a^(a&b)) - (b^(a&b)))
print(a-b == ((a|b)^b) - (b^(a&b)))