# import pandas as pd

# data={
#     "Department":["HR","IT","IT","HR","Finance","Marketing","IT"],
#     "employee": ['John','jas','karan','preet','aryan','sid','ross'],
#     "salary":[60000,80000,100000,90000,95000,50000,100000]
    
# }
# df=pd.DataFrame(data)
# result=df.groupby('Department')['salary'].sum()
# print(result)
import pandas as pd
df=pd.DataFrame({
    'name':['aman','bhumika','deep'],
    'marks':[85,90,78]
})
df.to_csv("output.csv",index=False)

#df.to_excel("output.xlsx",index=False)
print("hello")