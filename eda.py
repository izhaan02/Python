import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
# Load the dataset
df = pd.read_csv('Unicorn_Companies.csv')
# Display the first few rows of the dataset
print(df.head())
#Get dataset information
df.info()
#Get sumary statistics of numerical columns

print(df.describe())
#check missing values

print("\nMissing Values:\n ",df.isnull().sum())
print("\nMissing Values :\n",df.isnull().sum().sum())

print("\nUnique values in Each Column:\n",df.nunique())

#---------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
correlation_matrix=df.corr(numeric_only=True)
#it tells you how strongly and in direction(positive or negative) two variables are related
sns.heatmap(correlation_matrix,annot=True,cmap="Blues",fmt=".2f",linewidht=0.8)
plt.title("Correlation Heatmap")
plt.show()


numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
Q1 = df[numerical_columns].quantile(0.25)
Q3 = df[numerical_columns].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df[numerical_columns] < lower_bound) | (df[numerical_columns] > upper_bound)]
print("outliers detected using IQR method",outliers_iqr)

df[numerical_columns].boxplot(rot=45)
plt.title("Box plot for Outlier Detection")
