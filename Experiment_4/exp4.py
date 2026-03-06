"""
Aim: Write a program to demonstrate list & related functions in python.
"""

a = [10, 20, 30, 40]
print("Original list:", a)

a.append(50)
print("After append:", a)

a.extend([60, 70])
print("After extend:", a)

a.insert(1, 15)
print("After insert:", a)

a.remove(30)
print("After remove:", a)

print("Popped element:", a.pop())
print("After pop:", a)

print("Index of 40:", a.index(40))
print("Count of 20:", a.count(20))

a.sort()
print("After sort:", a)

a.reverse()
print("After reverse:", a)

b = a.copy()
print("Copied list:", b)

print("Length:", len(a))
print("Max:", max(a))
print("Min:", min(a))
print("Sum:", sum(a))

a.clear()
print("After clear:", a)