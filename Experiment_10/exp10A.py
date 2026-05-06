import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\sameeksha\sameeksha\VSCODE\Python\Experiment_10\sales_data.csv')

print("--- First 5 rows of the dataset ---")
print(df.head())

print("\n--- Dataset Information (Columns and Data Types) ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

df = df.drop_duplicates()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df = df.dropna()