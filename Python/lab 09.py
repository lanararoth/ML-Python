import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\shalu\Desktop\ML\ML-Python\Python\Salary_Dataset.csv")

fig, (x1, x2, x3) = plt.subplots(1, 3, figsize=(12, 4))

#Simple Line graph: y = x²
x = np.linspace(-5, 5, 50)
x1.plot(x, x**2, 'b-')
x1.set_title('y = x²')
x1.set_xlabel("x")
x1.set_ylabel("y")
x1.grid(True)

#Bar chart: Number of Salaries Reported by Job Role
salaries_reported_by_role = data.groupby("Job Roles")["Salaries Reported"].sum().sort_values(ascending=False)
x2.bar(salaries_reported_by_role.index, salaries_reported_by_role.values, color="skyblue", edgecolor="black")
x2.set_title("Number of Salaries Reported by Job Role")
x2.set_xlabel("Job Role")
x2.set_ylabel("Number of Salaries Reported")
x2.tick_params(axis="x", rotation=45)

#Histogram: Salary distribution
x3.hist(data['Salary'], bins=15, alpha=0.7, color='purple', edgecolor="black")
x3.set_title('Salary Distribution')
x3.set_xlabel("Salary")
x3.set_ylabel("Frequency")
x3.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
