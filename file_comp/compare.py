import pandas as pd
import numpy as np
# pd is just a short name for referencing pandas
# dftest1/2 means dataframe with the excel name in my folder

dftest1=pd.read_excel('files/test1.xlsx'
)

dftest2=pd.read_excel('files/test2.xlsx')

# print(dftest1.equals(dftest2))

comparevalues = dftest1.values == dftest2.values
print(comparevalues)

rows,cols=np.where(comparevalues==True)
for item in zip(rows,cols):
     dftest1.iloc[item[0], item[1]] = '{} --> {}'.format(dftest1.iloc[item[0], item[1]],dftest2.iloc[item[0], item[1]])
     dftest1.to_excel('./files/output.xlsx',index=False,header=True)





