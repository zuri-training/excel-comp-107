# -*- coding: utf_8 -*-
#!/usr/bin/python



import xlrd
import glob


import sqlite3

ExcelComp_db = sqlite3.connect('ExcelComp.db')
ExcelComp_db.text_factory = str
cursor = ExcelComp_db.cursor()

# 
cursor.execute('DROP TABLE IF EXISTS ExcelComp')
cursor.execute('DROP TABLE IF EXISTS ExcelTempData')
cursor.execute('CREATE TABLE ExcelComp (id INTEGER PRIMARY KEY, file_name varchar(128),company_name varchar(256),odds_win varchar(16),odds_equal varchar(16),odds_lose varchar(16))')
cursor.execute('CREATE TABLE ExcelTempData (id INTEGER PRIMARY KEY, file_name varchar(256),company_name varchar(256),odds_win varchar(16),odds_equal varchar(16),odds_lose varchar(16))')

# device Excel 

for filename in glob.glob(r'*.xls*'):

    device_workbook = xlrd.open_workbook(filename)
    for worksheet_name in device_workbook.sheet_names():
        device_sheet = device_workbook.sheet_by_name(worksheet_name)

    filename = device_sheet.cell(0, 0).value
    print filename
    for row in range(10, device_sheet.nrows):
        company_name = device_sheet.cell(row, 1).value
        odds_win = device_sheet.cell(row, 2).value
        odds_equal = device_sheet.cell(row, 3).value
        odds_lose = device_sheet.cell(row, 4).value
        cursor.execute('INSERT INTO ExcelComp (file_name,company_name,odds_win,odds_equal,odds_lose) VALUES (?,?,?,?,?)',
                      (filename,company_name,odds_win,odds_equal,odds_lose))

    ExcelComp_db.commit()


cursor.execute('SELECT file_name,company_name,odds_win,odds_equal,odds_lose '
               'FROM ExcelComp AS a ')

rows = cursor.fetchall()
brows = list(rows) 



temparr=[]
i=0
for row in rows:
    temparr.append(row[0])
    i=i+1
    for num in range(i,len(brows)):
        if row[0]!=brows[num][0] and \
            row[1]==brows[num][1] and \
            row[2]==brows[num][2] and \
            row[3]==brows[num][3] and \
            row[4]==brows[num][4]:
            temparr.append(brows[num][0])

    # for brow in brows:
    #     if row[0]!=brow[0] and \
    #     row[1]==brow[1] and \
    #     row[2]==brow[2] and \
    #     row[3]==brow[3] and \
    #     row[4]==brow[4]:
    #         temparr.append(brow[0])


    if len(temparr)>1:
        cursor.execute('INSERT INTO ExcelTempData (file_name,company_name,odds_win,odds_equal,odds_lose) VALUES (?,?,?,?,?)',
                      (';'.join(temparr),row[1],row[2],row[3],row[4]))
    
    del temparr[:]
ExcelComp_db.commit()


output = open('ExcelComp.txt', 'w')
cursor.execute('select file_name,company_name,odds_win,odds_equal,odds_lose  from ExcelTempData order by file_name  ')
rows = cursor.fetchall()
tempstr=""
cname=""
for row in rows:

    if tempstr!=row[0]: 
        output.write('\n')
        tempstr=str(row[0])
        t=tempstr.split(';')
        if len(t)>0:
            for x in t:
                output.write('\n'+x) 
        
        cname='\n        '+row[1]+","+row[2]+","+row[3]+","+row[4]
        print cname
    else:
        if cname!="":
            output.write(cname)
            cname=""
        output.write('\n        '+row[1]+","+row[2]+","+row[3]+","+row[4])
    if cname!="":
        output.write(cname)
        cname=""

output.close()
ExcelComp_db.close()











