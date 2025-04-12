missing = df.isnull().sum()
print("\nMissing values in each column:")
print(missing)


df.fillna(df.mean(), inplace=True)