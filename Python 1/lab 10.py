import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

file_path = r'C:\Users\shalu\Desktop\ML\ML-Python\Python 1\iris.csv'
iris = pd.read_csv(file_path)

plt.figure(figsize=(10,6))
sns.scatterplot(
    x='sepal_length', 
    y='sepal_width', 
    hue='species', 
    data=iris,
    palette='tab10',   
    s=80,            
    alpha=0.7
)

plt.title("Sepal Length vs Sepal Width (by Species)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
