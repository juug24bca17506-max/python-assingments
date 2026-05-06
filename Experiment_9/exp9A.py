import pandas as pd
import numpy as np

usn_array = np.arange(101, 111)

name_array = np.array([
    "Ranga", "Vaibhav", "Prabhakar", "Anusha", "Yashwanth", 
    "Sai", "Aditi", "Pooja", "Vikram", "Neha"
])

sub1_marks = np.array([85, 78, 92, 65, 88, 74, 90, 82, 95, 70])
sub2_marks = np.array([80, 82, 89, 70, 85, 76, 91, 84, 96, 75])

total_marks = np.add(sub1_marks, sub2_marks)

percentage_array = (total_marks / 200) * 100

data = {
    "USN": usn_array,
    "Student_Name": name_array,
    "Python_Marks": sub1_marks,
    "DBMS_Marks": sub2_marks,
    "Total_Marks": total_marks,
    "Percentage": percentage_array
}

df = pd.DataFrame(data)

df["Result_Status"] = np.where(df["Percentage"] >= 40, "Pass", "Fail")

df["Bonus_Total"] = df["Total_Marks"] + 5

print("Student Academic Data:")
print(df)

print("\nClass Average Data:")
print(df[["Python_Marks", "DBMS_Marks", "Total_Marks", "Percentage"]].mean())