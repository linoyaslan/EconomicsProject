import Mortality_Table_Men
import pandas as pd
import datetime
# excel_file = 'data.xlsx'
# Date = pd.read_excel(excel_file)

def read_value_from_excel(filename, column, row):
    return pd.read_excel(filename,sheet_name='data', skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]




"""
Enter the values from the Excel data file into the lists
"""

def Get_All_Data(string):
    """
    Lists that save the value from the Excel date file
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
    excel_file = string
    Date = pd.read_excel(excel_file)
    for i in range(1,len(Date)-149):
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

My_Data_New=[]
My_Data=Get_All_Data('data.xlsx')
for i in range(len(My_Data[0])):
    temp_list=[]
    for j in range(len(My_Data)):
        temp_list.append(My_Data[j][i])
    My_Data_New.append(temp_list)
for el in My_Data_New:
    print(el)

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
def Get_Start_Date(Name):
    return 0




"""
Calculates the seniority of an employee by days
"""
def Culc_seniority():
    employment_start_date=0



