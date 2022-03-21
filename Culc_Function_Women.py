import Mortality_Table_Women
import pandas as pd

"""
The probability that a person at age X will leave his job after t years.
Get_Chance_To_Leave Get 1 parm Age = current  Age
"""
def Get_Chance_To_Leave(Age):
    print("Enter y (The number of years a person is expected to leave his workplace:)")
    Age2 = int(input())
    result = 1.0
    for i in range(Age+1,(Age+Age2)):
        result = result*(1-(Mortality_Table_Women.Fired_dict[i] + Mortality_Table_Women.Resigns_dict[i]
                            + Mortality_Table_Women.Get_Qx(i)))
    return result


"""
Get start date of work
"""
def Get_Start_Date(Name):
    excel_file = 'data.xlsx'
    Get_Date = pd.read_excel(excel_file)
    Mortality_Table_Women.read_value_from_excel()



"""
Calculates the seniority of an employee by days
"""
def Culc_seniority():
    employment_start_date=0