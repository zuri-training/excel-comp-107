from django.shortcuts import render
from django import pandas as pd
from django import numpy as np

# Create your views here.

df1=pd.read_excel('sheet1.xlsx')
df2=pd.read_excel('sheet2.xlsx')
df1.equals(df2)
comparison_values = df1.values == df2.values
print (comparison_values)

rows,cols=np.where(comparison_values==False)
for item in zip(rows,cols):
     df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
     df1.to_excel('./Excel_diff.xlsx',index=False,header=True)


    
