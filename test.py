import pandas as pd
df=pd.read_csv("market_fact.csv")

df_total = df.groupby('Prod_id').agg({'Sales': 'sum', 'Profit': 'mean'})


df_neg = df[df['Profit'] < 0]

print("Total sales and average profit :")
print(df_total)

print("\nRecords where profit is negative:")
print(df_neg)




#------------------------------2---------------------------


df_dis = df[(df['Discount'] > 0.05) & (df['Order_Quantity'] > 20) & (df['Shipping_Cost'] < 5)]


uniq_prod_ids = df['Prod_id'].unique()

print("\n records:")
print(df_dis)

print("\nunique product IDs:")
print(uniq_prod_ids)

#------------------------------3---------------------------


missing = df.isnull().sum()
print("\nMissing values in each column:")
print(missing)


dfna=df.fillna(0)
print ("values filled with 0\n",dfna )

stat = df.describe()
print("\n stat=")

print(stat)





























