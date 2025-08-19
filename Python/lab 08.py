
import pandas as pd

data=pd.read_csv("ML/Salary_dataset.csv")

print("Head :\n", data.head())
print("\n")
print("Tail :\n", data.tail())
print("\n")

print("Mean of Salary :\n",data['Salary'].mean())
print("\n")
print("Median of Salary :\n",data['Salary'].median())
print("\n")
print("Median of Salary :\n",data['Salary'].median())