

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('worldBank.csv')
print(df.head())

plt.figure(figsize=(10,5))
country="Ireland"
df_country=df[df["Country Name"]==country]
plt.plot(df_country["Year"],df_country["GDP (USD)"],marker='o',linrstyle='dashdot',color='red')
plt.xlabel("Year") 
plt.ylabel("GDP (USD)")
plt.title(f"GDP trend for {country}")
plt.legend()
plt.grid()
plt.show()

#Histogram
plt.figure(figsize=(10,5))
sns.histplot(df["GDP (USD)"].dropna(),bins=30,kde=True,color="yellow",edgecolor="greeen")
#kde = Kernel Density Estimation
#provides smoother curve that estimate underlying distribution of continuous variable
plt.title("GDP distribution(Seaborn)")
plt.xlabel("GDP (USD)")
plt.ylabel("Frequency")
plt.show()


#scatter plot
sns.scatterplot(x=df["GDP (USD)",y=df["Life expectancy at birth(years)"],hue=df["Region"],aplha=0.7,legend=True)




#heatmap: corelation matrix

plt.figure(flagsize=(8,5))
corr_matrix=df.select_dtypes(include=['number'].corr())
sns.heatmap(corr_matrix,annot=True,linewidths=0.5)
plt.title("Correlatoin heatmao (seaborn)")
plt.show()
