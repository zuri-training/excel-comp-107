import pandas as pd
import xlwings as xw

dftest1 = pd.read_excel('files/test1.xlsx')
dftest2 = pd.read_excel('files/test2.xlsx')

excl_merged = pd.DataFrame()
excl_merged = excl_merged.append(
    dftest1, ignore_index=True)
excl_merged = excl_merged.append(
    dftest2, ignore_index=True)

print("Dataset with duplicates")
print(excl_merged)
allDuplicates = excl_merged[excl_merged.duplicated(keep='last')]
duplicateValues = allDuplicates.drop_duplicates(keep='first')
print("Duplicates from dataset")
print(duplicateValues)
noDuplicates = excl_merged.drop_duplicates(keep='first')
print("Dataset without duplicates")
print(noDuplicates)

noDuplicates.to_excel('./files/output.xlsx', index=False, header=True)
path = r"./files/output.xlsx"

with xw.App(visible=False) as app:
    wb = xw.Book(path)
    ws = wb.sheets[0]

    for a_cell in ws["A2:A5"].expand("down"):
        if type(a_cell.value) in [float, int]:
            if a_cell.value in duplicateValues.values:
                a_cell.color = (169, 208, 142)
            elif a_cell.value in duplicateValues.values:
                a_cell.color = (192, 0, 0)
    wb.save(path)
    wb.close()

#noDuplicates.to_excel('./files/output.xlsx', index=False, header=True)


#duplicate = excl_merged[excl_merged.duplicated(keep='first')]
# Print the resultant Dataframe
#print(duplicate)

# exports the dataframe into excel file with
# specified name.
#excl_merged.to_excel('./files/output.xlsx', index=False)

# duplicates = excl_merged.duplicated(keep=False)
# df = pd.DataFrame()
# duplicate = df[duplicates]
#print(duplicate)
#comparevalues = dftest1.values == dftest2.values
#print(comparevalues)

#dftest1['diff'] = np.where(dftest1['file_1'] == dftest2['file_2'] , '0', '1')

#comparevalues = dftest1. == dftest2.values
#print(comparevalues)
#rows = np.where(comparevalues == True)
#for item in zip(rows):
 #   dftest1.iloc[item[0], item[1]] = '{}  {}'.format(dftest1.iloc[item[0], item[1]], dftest2.iloc[item[0], item[1]])
  #  dftest1.to_excel('./files/output.xlsx', index=True, header=False)