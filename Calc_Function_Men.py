import csv
import Mortality_Table_Men
import Mortality_Table_Women
import pandas as pd
import datetime
from datetime import datetime
from datetime import date
from dateutil.parser import parse



"""
input: csv file name (string)
output: list of column names
"""
def Get_Csv_Column(Csv_File_Name):
    csv_file = open(Csv_File_Name+'.csv',encoding="utf-8")
    # creating an object of csv reader
    # with the delimiter as ' , '
    csv_reader = csv.reader(csv_file, delimiter=',')
    list_of_column_names = []
    # loop to iterate through the rows of csv
    for row in csv_reader:
        list_of_column_names.append(row)
        break
    return list_of_column_names

"""
Enter the values from the Excel data file into the lists
"""
def Get_All_Data(file_name):
    filename = open(file_name+'.csv', 'r', encoding="utf8")
    # creating dictreader object
    file = csv.DictReader(filename)
    """
    Lists that save the value from the csv date file
    """
    First_Name = []
    Last_Name = []
    Gender = []
    Birth_Date = []
    Start_Work = []
    Salary = []
    Start_Date_Section_14 = []
    Percent_Section_14 = []
    Property_Value = []
    Deposits = []
    Departure_Date = []
    Paid_From_Property = []
    Completion_Payment_Chuck = []
    Leaving_Reason = []

    for col in file:
        First_Name.append(col['Unnamed: 1'])
        Last_Name.append(col['Unnamed: 2'])
        Gender.append(col['Unnamed: 3'])
        Birth_Date.append(col['Unnamed: 4'])
        Start_Work.append(col['Unnamed: 5'])
        Salary.append(col['Unnamed: 6'])
        Start_Date_Section_14.append(col['Unnamed: 7'])
        Percent_Section_14.append(col['Unnamed: 8'])
        Property_Value.append(col['Unnamed: 9'])
        Deposits.append(col['Unnamed: 10'])
        Departure_Date.append(col['Unnamed: 11'])
        Paid_From_Property.append(col['Unnamed: 12'])
        Completion_Payment_Chuck.append(col['Unnamed: 13'])
        Leaving_Reason.append(col['Unnamed: 14'])

    return First_Name, Last_Name, Gender,Birth_Date, Start_Work, \
            Salary, Start_Date_Section_14, Percent_Section_14, Property_Value,\
            Deposits, Departure_Date, Paid_From_Property, Completion_Payment_Chuck, Leaving_Reason

def Get_All_Data2(file_name):
    filename = open(file_name+'.csv', 'r', encoding="utf8")
    # creating dictreader object
    file = csv.DictReader(filename)
    """
    Lists that save the value from the csv date file
    """
    Year = []
    Discounting = []
    for col in file:
        Year.append(col['Unnamed: 0'])
        Discounting.append(col['Unnamed: 1'])
    return Year, Discounting

"""
The function gets a file name, and returns a list that contains lists of data from the csv file.
input: file name (without ending xlsx, csv etc.)
output: list of lists with csv data
"""
def Create_Data_List(File_name):
    My_Data=Get_All_Data(File_name)
    my_new_data=[]
    for i in range(1,len(My_Data[0])):
        temp_list=[]
        for j in range(len(My_Data)):
            temp_list.append(My_Data[j][i])
        my_new_data.append(temp_list)
    return my_new_data

def Create_Data_List2(File_name):
    My_Data=Get_All_Data2(File_name)
    my_new_data=[]
    for i in range(1,len(My_Data[0])):
        temp_list=[]
        for j in range(len(My_Data)):
            temp_list.append(My_Data[j][i])
        my_new_data.append(temp_list)
    return my_new_data


def Get_Age_By_Days(Age):
    temp1 = parse(Age)
    b_date = datetime(temp1.year, temp1.month, temp1.day)
    temp2=parse('2021-12-31')
    date2 = datetime(temp2.year, temp2.month, temp2.day)
    return (date2-b_date).days

"""
The probability that a person at age X will stay in his job after t years.
Get_Chance_To_Stay Get 3 parm : Age = current  Age, i = stay t years , Gender = Gender
"""
def Get_Chance_To_Stay(Age, i, Gender):
    if i==0:
        return 1
    if i == 1:
        return 1
    if Gender=='M':
        result = (1-(Mortality_Table_Men.Fired_dict[(Age+i-1)] + Mortality_Table_Men.Resigns_dict[(Age+i-1)]
                                + float(Mortality_Table_Men.Get_Qx(Age+i-1))))
        return result*Get_Chance_To_Stay(Age,i-1,Gender)

    else:
        result = (1 - (Mortality_Table_Women.Fired_dict[Age+i-1] + Mortality_Table_Women.Resigns_dict[Age+i-1]
                                    + float(Mortality_Table_Women.Get_Qx(Age+i-1))))
        return result*Get_Chance_To_Stay(Age,i-1,Gender)

"""
Get start date of work
"""
def Get_Start_Date(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if Data_list[i][0] == Name and Data_list[i][1] == last_name:
            return parse(Data_list[i][4])

def Get_leaving_Date(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if  Data_list[i][0] == Name and Data_list[i][1] == last_name:
            if Data_list[i][10] =='-':
                return 0
            return parse(Data_list[i][10])

"""
Calculates the seniority of an employee by days
"""
def Get_Senioruty_By_Years(start):
    a_date = start
    a_date = datetime(a_date.year, a_date.month, a_date.day)
    b_date = parse('28/04/2022')
    b_date = datetime(b_date.year, b_date.month, b_date.day)
    return ((b_date-a_date)/365.25).days
"""
Returns the years in which an employee worked without section 14
"""
def Get_Section_14_By_Years(start,end):
    a_date = parse(start)
    a_date = datetime(a_date.year, a_date.month, a_date.day)
    b_date = parse(end)
    if type(end) != type(start):
        return "There is no section 14"
    b_date = datetime(b_date.year, b_date.month, b_date.day)
    return ((b_date-a_date)/365.25).days

"""
Returns the salary of each employee based on input: first, last name, Data_list
"""
def Get_Salary(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if Data_list[i][0] == Name and Data_list[i][1] == last_name:
            return Data_list[i][5]

def Get_Discounting(Year,Data_list):
    for i in range(len(Data_list)):
        if Data_list[i][0] == str(Year):
            return float(Data_list[i][1])

def Get_Salary_Growth_Rate():
    return 0.03

def Get_All_Data_XL(file_name):
    excel_file = file_name
    life_table = pd.read_excel(excel_file)
    #Lists that save the value from the Excel date file
    First_Name = []
    Last_Name = []
    Gender = []
    Birth_Date = []
    Start_Work = []
    Salary = []
    Start_Date_Section_14 = []
    Percent_Section_14 = []
    Property_Value = []
    Deposits = []
    Departure_Date = []
    Paid_From_Property = []
    Completion_Payment_Chuck = []
    Leaving_Reason = []

    for i in range(1,len(life_table)-145):
        First_Name.append(read_value_from_excel(excel_file,'B',i+2))
        Last_Name.append(read_value_from_excel(excel_file,'C',i+2))
        Gender.append(read_value_from_excel(excel_file,'D',i+2))
        Birth_Date.append(read_value_from_excel(excel_file,'E',i+2))
        Start_Work.append(read_value_from_excel(excel_file,'F',i+2))
        Salary.append(read_value_from_excel(excel_file,'G',i+2))
        Start_Date_Section_14.append(read_value_from_excel(excel_file,'H',i+2))
        Percent_Section_14.append(read_value_from_excel(excel_file,'I',i+2))
        Property_Value.append(read_value_from_excel(excel_file,'J',i+2))
        Deposits.append(read_value_from_excel(excel_file,'K',i+2))
        Departure_Date.append(read_value_from_excel(excel_file,'L',i+2))
        Paid_From_Property.append(read_value_from_excel(excel_file,'M',i+2))
        Completion_Payment_Chuck.append(read_value_from_excel(excel_file,'N',i+2))
        Leaving_Reason.append(read_value_from_excel(excel_file,'O',i+2))
    return First_Name, Last_Name, Gender,Birth_Date, Start_Work, \
            Salary, Start_Date_Section_14, Percent_Section_14, Property_Value,\
            Deposits, Departure_Date, Paid_From_Property, Completion_Payment_Chuck, Leaving_Reason

def read_value_from_excel(filename, column, row):
    return pd.read_excel(filename,sheet_name='data', skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]
