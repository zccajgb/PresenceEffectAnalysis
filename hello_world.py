import pandas as pd
import matplotlib.pyplot as plt
import pingouin as pg

data_table = pd.read_csv('data.csv') 

data_table.groupby('Age').size().plot.bar(color='Blue')	
plt.xlabel('Age')
plt.ylabel('Sample Size')
plt.tight_layout()
plt.show()
sample = data_table.groupby('Age').size()
print(sample.mean())
print(sample.std())
print(sample.min())
print(sample.max())
print(s)

data_table.boxplot(column='Age',by='Gender',showmeans=True)
plt.show()
print("hello world")

