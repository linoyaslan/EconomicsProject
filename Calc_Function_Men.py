import csv
import maya
import Mortality_Table_Men
import pandas as pd
import datetime
from datetime import datetime
from datetime import date

def read_value_from_excel(filename, column, row):
    return pd.read_excel(filename,sheet_name='data', skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]


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

def Get_Age_By_Days(Age):
    b_date = Age
    b_date = datetime(b_date.year, b_date.month, b_date.day)
    date2 = datetime(2021,12,31)
    return (date2-b_date).days

"""
The probability that a person at age X will leave his job after t years.
Get_Chance_To_Leave Get 1 parm Age = current  Age
"""
def Get_Chance_To_Leave(Age):
    print("Enter y (The number of years a person is expected to leave his workplace:)")
    Age2 = int(input())
    result = 1.0
    for i in range(Age+1,(Age+Age2)):
        result = result*(1-(Mortality_Table_Men.Fired_dict[i] + Mortality_Table_Men.Resigns_dict[i]
                            + Mortality_Table_Men.Get_Qx(i)))
    return result


"""
Get start date of work
"""
def Get_Start_Date(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if  Data_list[i][0] == Name and Data_list[i][1] ==last_name:
            return maya.parse(Data_list[i][4]).datetime()


def Get_leaving_Date(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if  Data_list[i][0] == Name and Data_list[i][1] == last_name:
            if Data_list[i][10] =='-':
                return 0
            return maya.parse(Data_list[i][10]).datetime()


"""
Calculates the seniority of an employee by days
"""
def Get_Senioruty_By_Years(start,end):
    a_date = start
    a_date = datetime(a_date.year, a_date.month, a_date.day)
    b_date = end
    if type(end) != type(start):
        return "The employee has not yet been fired"
    b_date = datetime(b_date.year, b_date.month, b_date.day)
    return ((b_date-a_date)/365.25).days

def Get_Salary(Name,last_name,Data_list):
    for i in range(len(Data_list)):
        if Data_list[i][0] == Name and Data_list[i][1] == last_name:
            return Data_list[i][5]









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

