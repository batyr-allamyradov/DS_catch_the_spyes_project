
import os
import openpyxl
import pandas as pd
print("11")
Id=0
data = []
for filename in os.listdir("/home/mikhail/Рабочий стол/DS_lab3/YourBoardingPassDotAero"):
    if(filename.endswith(".xlsx")):
        file_ = f'/home/mikhail/Рабочий стол/DS_lab3/YourBoardingPassDotAero/{filename}'
        file_obj = openpyxl.load_workbook(file_)
        for sh in file_obj.worksheets:
            sheet = file_obj[sh.title]
            data.append([])
            data[Id].append(sheet["H1"].value)  # Sequence
            data[Id].append(sheet["A3"].value)  # Title
            data[Id].append(sheet["B3"].value)  # Name
            data[Id].append(sheet["A5"].value)  # FlightNumber
            data[Id].append(sheet["F3"].value)  # BoardNumber
            data[Id].append(sheet["B7"].value)  # Gate
            data[Id].append(sheet["D5"].value)  # From
            data[Id].append(sheet["D7"].value)  # FromCode
            data[Id].append(sheet["H5"].value)  # To
            data[Id].append(sheet["H7"].value)  # ToCode
            data[Id].append(sheet["A9"].value)  # Date
            data[Id].append(sheet["C9"].value)  # Time
            data[Id].append(sheet["E9"].value)  # Operated
            data[Id].append(sheet["A11"].value)  # BoardingEnded
            data[Id].append(sheet["H11"].value)  # Seat
            data[Id].append(sheet["B13"].value)  # PNR
            data[Id].append(sheet["E13"].value)  # ETicket
            Id += 1
    print(".")
col = ['Sequence', 'Title', 'Name', 'FlightNumber', 'BoardNumber',
           'Gate', 'From', 'FromCode', 'To', 'ToCode', 'Date',
           'Time', 'Operated', 'BoardingEnded', 'Seat', 'PNR', 'ETicket']
df = pd.DataFrame(data, columns=col)
print(df.head())
df.to_csv(r'YourBoardingPassDotAero.csv', index_label='id')
