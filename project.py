import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Performing some Preprocessing

df= pd.read_csv('netflix_titles.csv')
print(df.head())
#df.info()
# df['director'].fillna('Unknown Director', inplace=True)
# df['cast'].fillna('Unknown Cast', inplace=True)
# df['country'].fillna('Unknown Country', inplace=True)
