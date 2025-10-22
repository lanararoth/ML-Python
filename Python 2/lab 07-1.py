import pandas as pnd

data=[
    {'SN':1, 'Name':'Geoffrey Hinton', 'Country':'Canada', 'Innovation':'Deep Learning', 'Year':1986},
    {'SN':2, 'Name':'Yann LeCun', 'Country':'France', 'Innovation':'Convolutional Neural Nets', 'Year':1989},
    {'SN':3, 'Name':'Andrew Ng', 'Country':'USA', 'Innovation':'Online ML Courses', 'Year':2011},
    {'SN':4, 'Name':'Phila Suoni ', 'Country':'UK', 'Innovation':'Artificial Intelligence', 'Year':2023},
    {'SN':5, 'Name':'Yemehi Yathi', 'Country':'France', 'Innovation':'Data Analytics', 'Year':2025},
]
dataframe = pnd.DataFrame(data)

dataframe.to_csv('tech_innovators.csv', index=False)
print("CSV created\n")