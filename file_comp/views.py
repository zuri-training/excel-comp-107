from django.shortcuts import render
import pandas as pd
import numpy as np

# Create your views here.
# this code is to be continued 
# add comments here
df1=pd.read_excel('test1.xlsx')
df2=pd.read_excel('test2.xlsx')
df1.equals(df2)
comparison_values = df1.values == df2.values
print (comparison_values)

rows,cols=np.where(comparison_values==False)
for item in zip(rows,cols):
     df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
     df1.to_excel('./Excel_diff.xlsx',index=False,header=True)


    
