import pandas as pd
import numpy as np
from openpyxl import Workbook
from dotenv import load_dotenv
from openpyxl.styles import PatternFill
 
dftest1 = pd.read_excel('files/test1.xlsx')
 
dftest2 = pd.read_excel('files/test2.xlsx')
# print(dftest1.equals(dftest2))
comparevalues = dftest1.values == dftest2.values
print(comparevalues)
rows, cols = np.where(comparevalues == True)
for item in zip(rows, cols):
    dftest1.iloc[item[0], item[1]] = '{}  {}'.format(dftest1.iloc[item[0], item[1]], dftest2.iloc[item[0], item[1]])
    dftest1.to_excel('./files/output.xlsx', index=True, header=False)
    
    # format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                            #    'font_color': '#9C0006'})
    def view_result(request):
        def highlight_cells(val):
            pat=str(val)
            color = 'orange' if pat [0]== '*' else 'blue'
            return 'background-color: {}'.format(color)
        h = dftest1.style.applymap(highlight_cells)
