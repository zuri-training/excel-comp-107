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
allDuplicates = excl_merged[excl_merged.duplicated(keep='first')]
print("Duplicates from dataset")
print(allDuplicates)

excl_merged.to_excel('./files/output.xlsx', index=False, header=True)
path = r"./files/output.xlsx"

with xw.App(visible=False) as app:
    wb = xw.Book(path)
    ws = wb.sheets[0]

    for a_cell in ws["A2:A100"].expand("down"):
        if type(a_cell.value) in [float, int]:
            if a_cell.value in allDuplicates.values:
                a_cell.color = (169, 208, 142)
            elif a_cell.value in allDuplicates.values:
                a_cell.color = (192, 0, 0)
    wb.save(path)
    wb.close()

