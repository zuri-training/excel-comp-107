import pandas as pd

#Exporting raw data from a csv file
DataOrigin = pd.read_csv('RAWDATA.csv')
#Sorting raw data per interesting columns
DataOriginSorted = DataOrigin.sort_values(['srcip','attack','dstip'])
#Exporting some columns of historical data and sorting them
Historicaldata2 = pd.read_excel('Historicaldata.xlsx', sheet_name=1, usecols = ['Source_IP','Ticket','Customer_Notification','Hostname','Service_desk_ticket'])
Historicaldata2Sorted = Historicaldata2.sort_values(['Source_IP','Ticket'])
#Creating a multindex variable with sorted raw data
index = pd.MultiIndex.from_frame(DataOriginSorted)
Sorted_DataOrigin = pd.DataFrame(index=index)
#Making a count of events per source IP and exporting them as a csv for the code to work (rename column oepration)
Daily_IncidentsIPS = pd.crosstab(DataOrigin.srcip,DataOrigin.attack).to_csv('ControlFile1.csv')
Daily_IncidentsIPS = pd.read_csv('ControlFile1.csv').rename(columns = {'srcip': 'Source_IP'}, inplace = False )
#Mergin 2 dataframes to find coincident data and exporting them to a csv for the next operations to take place and using only interesting columns
Historical2vsSortedOrigin = Historicaldata2Sorted.merge(Daily_IncidentsIPS,left_on='Source_IP',right_on='Source_IP', how='inner').to_csv('ControlFile2.csv')
Historical2vsSortedOrigin = pd.read_csv('ControlFile2.csv', usecols = ['Ticket','Hostname','Source_IP','Customer_Notification','Service_desk_ticket'])
#Searching for duplicated data between two interesting dataframes
duplicated = Daily_IncidentsIPS['Source_IP'].isin(Historical2vsSortedOrigin['Source_IP'])
#Creating a rule to color the rows where the duplicated values are present
def row_styler(row):
    return ['background-color: yellow' if duplicated[row.name] else ''] * len(row)

#Creating a multindex variable to show the data as I want it
index2 = pd.MultiIndex.from_frame(Historical2vsSortedOrigin)
IncidentMatching = pd.DataFrame(index=index2)
#Saving 3 interesting dataframes in an excel file, highlighting the results of previous "search for duplicated" operation
writer = pd.ExcelWriter('C:\\Users\myuser\Documents\Spyder\Results_IPS.xlsx', engine='xlsxwriter')
Daily_IncidentsIPS.style.apply(row_styler, axis=1).to_excel(writer, sheet_name='Sheet1')
Sorted_DataOrigin.to_excel(writer, sheet_name='Sheet2')
IncidentMatching.to_excel(writer, sheet_name='Sheet3')
writer.save()

