# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#this is where all the files will be downloaded after the program is run
directory_path = '/home/user/Documents/python_webscraper/'

year = 2020 
selectedcompany = 'WD 40 CO'
selectedreport = '10-Q'

#when this is set to true the tsv documents pulled from from the SEC will be deleted after they are used.
purge_file_directory = False

import edgar
import pandas as pd
import os

tsv_file_names = []
balance_sheets = []
cash_flow_statements = []

#this function creates a list of files created that will be used to create the spreadsheets.
def tsv_name_formatter():
    for file in tsv_files:
        split_file = file.split('.')
        tsv_file_names.append(split_file[0])
        print('{} was created'.format(file))
        
#This will go through the documents and find the balance sheet.
def balance_sheet():
    for item in df:
        BS = (item[0].astype(str).str.contains('Retained') | item[0].astype(str).str.contains('Total Assets'))
        if BS.any():
            Balance_Sheet = item     
    
            Balance_Sheet = Balance_Sheet.iloc[10:57,[0,2,5]]
            
            header = Balance_Sheet.iloc[0]
            Balance_Sheet = Balance_Sheet[1:]
            
            Balance_Sheet.columns = header
            
            
            Balance_Sheet.columns.values[0] = 'Item'
            Balance_Sheet = Balance_Sheet[Balance_Sheet['Item'].notna()]
            
            Balance_Sheet[Balance_Sheet.columns[1:]] = Balance_Sheet[Balance_Sheet.columns[1:]].astype(str)
            Balance_Sheet[Balance_Sheet.columns[1]] = Balance_Sheet[Balance_Sheet.columns[1]].map(lambda x: x.replace('-','0'))
            Balance_Sheet[Balance_Sheet.columns[2]] = Balance_Sheet[Balance_Sheet.columns[2]].map(lambda x: x.replace('-','0'))
            
            Balance_Sheet[Balance_Sheet.columns[1]] = Balance_Sheet[Balance_Sheet.columns[1]].map(lambda x: x.replace('(','-'))
            Balance_Sheet[Balance_Sheet.columns[2]] = Balance_Sheet[Balance_Sheet.columns[2]].map(lambda x: x.replace('(','-'))
            
            Balance_Sheet[Balance_Sheet.columns[1]] = Balance_Sheet[Balance_Sheet.columns[1]].map(lambda x: x.replace(')',''))
            Balance_Sheet[Balance_Sheet.columns[2]] = Balance_Sheet[Balance_Sheet.columns[2]].map(lambda x: x.replace(')',''))
            
            Balance_Sheet[Balance_Sheet.columns[1]] = Balance_Sheet[Balance_Sheet.columns[1]].map(lambda x: x.replace(',',''))
            Balance_Sheet[Balance_Sheet.columns[2]] = Balance_Sheet[Balance_Sheet.columns[2]].map(lambda x: x.replace(',',''))
            
            Balance_Sheet[Balance_Sheet.columns[1]] = Balance_Sheet[Balance_Sheet.columns[1]].map(lambda x: x.replace('nan','0'))
            Balance_Sheet[Balance_Sheet.columns[2]] = Balance_Sheet[Balance_Sheet.columns[2]].map(lambda x: x.replace('nan','0'))
            
            
            Balance_Sheet[Balance_Sheet.columns[1:]] = Balance_Sheet[Balance_Sheet.columns[1:]].astype(float)
            
            balance_sheets.append(Balance_Sheet)
            

#This will go through the documents and find the balance sheet.
def cash_flow_statment():
    for item in df:
        CFS = (item[0].astype(str).str.contains('CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS'))
        if CFS.any():
            Cash_Flow_Statement = item     
    
            Cash_Flow_Statement = Cash_Flow_Statement.iloc[6:48,[0,2,5]]
            
            header = Cash_Flow_Statement.iloc[0]
            Cash_Flow_Statement = Cash_Flow_Statement[1:]
            
            Cash_Flow_Statement.columns = header
            
            
            Cash_Flow_Statement.columns.values[0] = 'Item'
            Cash_Flow_Statement = Cash_Flow_Statement[Cash_Flow_Statement['Item'].notna()]
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1:]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1:]].astype(str)
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1]].map(lambda x: x.replace('-','0'))
            Cash_Flow_Statement[Cash_Flow_Statement.columns[2]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[2]].map(lambda x: x.replace('-','0'))
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1]].map(lambda x: x.replace('(','-'))
            Cash_Flow_Statement[Cash_Flow_Statement.columns[2]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[2]].map(lambda x: x.replace('(','-'))
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1]].map(lambda x: x.replace(')',''))
            Cash_Flow_Statement[Cash_Flow_Statement.columns[2]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[2]].map(lambda x: x.replace(')',''))
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1]].map(lambda x: x.replace(',',''))
            Cash_Flow_Statement[Cash_Flow_Statement.columns[2]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[2]].map(lambda x: x.replace(',',''))
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1]].map(lambda x: x.replace('nan','0'))
            Cash_Flow_Statement[Cash_Flow_Statement.columns[2]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[2]].map(lambda x: x.replace('nan','0'))
            
            
            Cash_Flow_Statement[Cash_Flow_Statement.columns[1:]] = Cash_Flow_Statement[Cash_Flow_Statement.columns[1:]].astype(float)
            
            cash_flow_statements.append(Cash_Flow_Statement)
            
            
#This will clean up the SEC tsv files after running the script and extracting the relevant information.
def purge_tsv_files():
    for file in tsv_files:
        os.remove(directory_path + file)
        print('{} deleted'.format(file))
        
#Downloads the list of all company files including the location of those files for us to look through.
if os.path.exists(directory_path + str(year) + '-' + 'QTR1.tsv') == True:
    print('No new files downloaded')
    tsv_files = os.listdir(directory_path)
    tsv_name_formatter()
else:
    edgar.download_index(directory_path, year,
                         skip_all_present_except_last=False)
    print('Files downloaded successfully')
    tsv_files = os.listdir(directory_path)
    tsv_name_formatter()

#This for loop will take all the tsv files that were downloaded for the year and compile the different 
#financial reports
for file in tsv_file_names:
    csv = pd.read_csv('/home/user/Documents/python_webscraper/' + file + '.tsv', 
                  sep='\t',  lineterminator='\n', names=None) 

    csv.columns.values[0] = 'Item'
    
    #This for loop ensures that the proper documents are found regardless of whether we are looking at a 10-Q or 10-K
    if file is not (str(year) + '-QTR4'):
        selectedreport = '10-Q'
    else:
        selectedreport = '10-K'
        
    companyreport = csv[(csv['Item'].str.contains(selectedcompany)) & 
                        (csv['Item'].str.contains(selectedreport))]

    Filing = companyreport['Item'].str.split('|')
    Filing = Filing.to_list()

    for item in Filing[0]:

        if 'html' in item:
            report = item

    url = 'https://www.sec.gov/Archives/' + report
    #https://www.sec.gov/ix?doc=/Archives/edgar/data/1652044/000165204419000032/goog10-qq32019.htm

    df = pd.read_html(url)
    document_index = df[0]
    document_index = document_index.dropna()

    document_name = document_index[document_index['Description'].str.contains(selectedreport)]
    document_name = document_name['Document'].str.split(' ')
    document_name = document_name[0][0]

    report_formatted = report.replace('-','').replace('index.html','')
    url = 'https://www.sec.gov/Archives/' + report_formatted + '/' + document_name


    df = pd.read_html(url)
    
    #invoking the balance_sheet definition to compile the report
    balance_sheet()
    
    
#This is used at the end of the script to clean up any residual junk files that will not be needed. It will delete 
#all the tsv files that were downloaded at the beginning. 
if purge_file_directory is True:
    purge_tsv_files()