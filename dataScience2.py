import seaborn as  sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

titanic=sns.load_dataset('titanic')

print(titanic.head())
print(titanic.info())
print(titanic.describe())
print(titanic.describe().T)#for transpose

print(titanic.isnull().sum())
print(titanic.isnull().sum().sum())



#data visualization: heatmap

plt.figure(figsize=(10,6))
sns.countpot(x='Survived',data=titanic,palette='coolwarm')
plt.title('Survied count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()
plt.figure(figsize=(10,6))
sns.heatmap(titanic.corr(numeric_only=True),annot=True,cmap='coolwarm',linewidhts=0.5)
plt.show()

#Q1 how does passengerd age distributuion look like?

plt.figure(figsize=(10,6))
plt.histplot(titanic['age'],bins=20,color='Skyblue',edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


#Q2 what is the survival rate across diffrent classes?(using barplot)
plt.figure(figsize=(10,6))
sns.barplot(x='class',y='survived',data=titanic,color='red',edgecolor='green')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

#Q3 how does the fare vary with passenger class?(using boxplot)
plt.figure(figsize=(10,6))
sns.boxplot(x='class',y='fare',data=titanic,hue='class')
plt.title('Fare Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

#Q4 what is the relationship between age and fare?

plt.figure(figsize=(10,6))
sns.scatterplot(x='age',y='fare',data=titanic,alpha=0.5)
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()