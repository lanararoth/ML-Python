import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

file_path = r'C:\Users\shalu\Desktop\ML\ML-Python\Python\iris2.csv'
iris = pd.read_csv(file_path)

plt.figure(figsize=(10,6))
sns.scatterplot(
    x='QUANTITYORDERED', 
    y='SALES', 
    hue='DEALSIZE', 
    data=iris,
    palette='tab10',   
    s=80,            
    alpha=0.7
)

plt.title("Sales vs Quantity Ordered (by Deal Size)")
plt.xlabel("Quantity Ordered")
plt.ylabel("Sales ($)")
plt.legend(title='Deal Size', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
