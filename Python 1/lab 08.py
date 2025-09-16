
import pandas as pd

data = pd.read_csv(r"C:\Users\shalu\Desktop\ML\ML-Python\Python\Salary_dataset.csv")

print("Head :\n", data.head())
print("\n")
print("Tail :\n", data.tail())
print("\n")

mean_sal=data['Salary'].mean()
median_sal=data['Salary'].median()
mode_sal=data['Salary'].mode()

print("Mean of Salary :\n",mean_sal)
print("\n")
print("Median of Salary :\n",median_sal)
print("\n")
print("Mode of Salary :\n",mode_sal)
print("\n")
