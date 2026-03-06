"""
Aim: Write a program to implement various string operations.
"""

s = input("Enter a string: ")

print("Position of 'a':", s.find('a'))
print("Replace 'a' with '@':", s.replace('a', '@'))
print("Split words:", s.split())
print("'z' not in string:", 'z' not in s)
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Capitalize:", s.capitalize())
print("Reverse string:", s[::-1])
print("First character:", s[0])
print("Last character:", s[-1])