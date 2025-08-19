import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

# Load the iris dataset
iris = pd.read_csv('ML/iris.csv')  # Make sure the path and extension are correct

# Scatter plot: sepal_length vs sepal_width with color by species
sns.scatterplot(
    x='sepal_length', 
    y='sepal_width', 
    hue='species', 
    data=iris,
    palette='Set1'
)

plt.title("Iris Dataset Scatter Plot")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend(title='Species')
plt.show()
