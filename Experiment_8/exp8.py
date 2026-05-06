import re


text1 = "Hello World"
pattern1 = r"Hello"
result1 = re.match(pattern1, text1)
print("match():", result1.group())


text2 = "I love Python programming"
pattern2 = r"Python"
result2 = re.search(pattern2, text2)
print("search():", result2.group() if result2 else "Not found")


text3 = "Numbers are 12, 45, and 78"
pattern3 = r"\d+"
result3 = re.findall(pattern3, text3)
print("findall():", result3)

text4 = "Age: 20, 30, 40"
pattern4 = r"\d+"
print("finditer():")
for match in re.finditer(pattern4, text4):
    print(match.group(), "at position", match.start())

text5 = "My number is 12345"
pattern5 = r"\d"
result5 = re.sub(pattern5, "*", text5)
print("sub():", result5)

text6 = "Split this sentence into words"
pattern6 = r"\s"
result6 = re.split(pattern6, text6)
print("split():", result6)

date=input("enter a date (dd/mm/yyyy):")
pattern=r'^\d{2}/\d{2}/\d{4}$'
if re.fullmatch(pattern,date):
    print("vaild date format")
else:
    print("invald")