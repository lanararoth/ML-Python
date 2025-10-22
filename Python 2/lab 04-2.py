import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = [
    {'month_number': 1, 'facecream': 2500, 'facewash': 1500, 'toothpaste': 5200, 'bathingsoap': 9200, 'shampoo': 1200, 'moisturizer': 1500, 'total_units': 20100, 'total_profit': 15000},
    {'month_number': 2, 'facecream': 2630, 'facewash': 1200, 'toothpaste': 5100, 'bathingsoap': 6100, 'shampoo': 2100, 'moisturizer': 1200, 'total_units': 18330, 'total_profit': 14000},
    {'month_number': 3, 'facecream': 2140, 'facewash': 1340, 'toothpaste': 4550, 'bathingsoap': 9550, 'shampoo': 2200, 'moisturizer': 1100, 'total_units': 20880, 'total_profit': 16000},
    {'month_number': 4, 'facecream': 3400, 'facewash': 1130, 'toothpaste': 5870, 'bathingsoap': 8900, 'shampoo': 1800, 'moisturizer': 1400, 'total_units': 22500, 'total_profit': 17500},
    {'month_number': 5, 'facecream': 3600, 'facewash': 1450, 'toothpaste': 6100, 'bathingsoap': 9200, 'shampoo': 2500, 'moisturizer': 1300, 'total_units': 24150, 'total_profit': 18000},
    {'month_number': 6, 'facecream': 2760, 'facewash': 1150, 'toothpaste': 5400, 'bathingsoap': 9100, 'shampoo': 1500, 'moisturizer': 1200, 'total_units': 21110, 'total_profit': 16000},
    {'month_number': 7, 'facecream': 2980, 'facewash': 1420, 'toothpaste': 4900, 'bathingsoap': 8000, 'shampoo': 2000, 'moisturizer': 1350, 'total_units': 20650, 'total_profit': 17000},
    {'month_number': 8, 'facecream': 3700, 'facewash': 1700, 'toothpaste': 6200, 'bathingsoap': 8500, 'shampoo': 2300, 'moisturizer': 1400, 'total_units': 24800, 'total_profit': 18500},
    {'month_number': 9, 'facecream': 3100, 'facewash': 1600, 'toothpaste': 5400, 'bathingsoap': 9200, 'shampoo': 2200, 'moisturizer': 1100, 'total_units': 23600, 'total_profit': 17500},
    {'month_number': 10, 'facecream': 2750, 'facewash': 1400, 'toothpaste': 5700, 'bathingsoap': 9000, 'shampoo': 1900, 'moisturizer': 1250, 'total_units': 22000, 'total_profit': 16500},
    {'month_number': 11, 'facecream': 2900, 'facewash': 1500, 'toothpaste': 6100, 'bathingsoap': 8500, 'shampoo': 2100, 'moisturizer': 1300, 'total_units': 22400, 'total_profit': 17000},
    {'month_number': 12, 'facecream': 3200, 'facewash': 1600, 'toothpaste': 6000, 'bathingsoap': 8900, 'shampoo': 2000, 'moisturizer': 1400, 'total_units': 23100, 'total_profit': 18000}
]

# Create DataFrame and save CSV
df = pd.DataFrame(data)
df.to_csv('comp.csv', index=False)
print("csv2 created")

# Read CSV back (optional, as df is ready)
df = pd.read_csv('comp.csv')

# Calculate total sales for pie chart
total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

# Prepare x-axis for bar chart
months = np.arange(len(df['month_number']))

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# a) Toothpaste scatter plot
axs[0, 0].scatter(df['month_number'], df['toothpaste'], color='blue')
axs[0, 0].set_title('Toothpaste Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales')
axs[0, 0].grid(True)

# b) Face cream & face wash bar chart
bar_width = 0.35
axs[0, 1].bar(months - bar_width/2, df['facecream'], width=bar_width, label='Face Cream', color='green')
axs[0, 1].bar(months + bar_width/2, df['facewash'], width=bar_width, label='Face Wash', color='orange')
axs[0, 1].set_title('Face Cream & Face Wash Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales')
axs[0, 1].set_xticks(months)
axs[0, 1].set_xticklabels(df['month_number'])
axs[0, 1].legend()

# c) Pie chart of total sales per product
axs[1, 0].pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Total Sales Distribution')

# Turn off unused subplot
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
