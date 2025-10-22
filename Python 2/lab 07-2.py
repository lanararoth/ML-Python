import pandas as pd

data = pd.read_csv('tech_innovators.csv')

innovators = data[data["Year"] < 2000]


for name in innovators["Name"]:
    print(name)