import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Experiment_10\sales_data.csv')

df = df.drop_duplicates()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df = df.dropna()

plt.figure(figsize=(8, 4))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue')
plt.title('Monthly Sales (Line Chart)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Category (Bar Chart)')
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(df['Sales'], bins=10, color='green')
plt.title('Distribution of Sales (Histogram)')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()