import seaborn as  sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(11)
data=pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=100),
    'Value1': np.random.randn(100),
    'Value2':np.random.randn(100),
    'Time':pd.date_range(start='2023-01-01',periods=100,freq='W')
})
print(data)

#set the style

sns.set(Style="whitegrid")
#line plot
plt.figure(figsize=(8,4))
sns.lineplot(data=data,x='Time',y='Value1')
sns.lineplot(data=data,x='Time',y='Value2',color='r')
plt.title('Line Plot Example')
plt.show()

#bar plot

plt.figure(figsize=(8,4))
sns.barplot(data=data,x='Category',y='Value1',errerbar=None)
plt.title('Bar Plot Example')
plt.show()

#Scatter plot
plt.figure(figsize=(8,4))
sns.scatterplot(data=data,x='Value1',y='Value2',hue='Category',style='Category',s=100)
plt.title('Scatter Plot Example')
plt.show()
palette={'A':'red','B':'blue','C':'green','D':'yellow'}
markers={'A':'H','B':'P','C':'D','D':'*'}
sns.scatterplot(data=data,x='Value1',y='Value2',hue='Category',style='Category',palette=palette,markers=markers,s=100)
#s=100 controls the size fo thr marker in the scatter plot
plt.title('SCatter plot Example')
plt.xlabel('Value1 (X-axis)')
plt.ylabel('Value2 (Y-axis)')
plt.show()

#heat map

plt.figure(figsize=(8,4))
corr=data[['Value1':'Value2']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm',cbar=True,fmt='.2f')