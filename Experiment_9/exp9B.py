import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student_Name": ["Ranga", "Vaibhav", "Prabhakar", "Anusha", "Yashwanth", 
                     "Sai", "Aditi", "Pooja", "Vikram", "Neha"],
    "Total_Marks": [165, 160, 181, 135, 173, 150, 181, 166, 191, 145]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df["Student_Name"], df["Total_Marks"], color='skyblue', edgecolor='black')

plt.title("Student Total Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()