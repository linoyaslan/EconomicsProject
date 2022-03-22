import csv
import pandas as pd

"""
convert excel to csv
input: path to xlsx file (string)
output: csv file with a name we choose
"""
def To_CSV(path):
    read_file = pd.read_excel(r''+path)
    print("enter file name: ")
    name = input()
    read_file.to_csv(r'C:\\Users\\or204\\PycharmProjects\\EconomicsProject\\'+name+'.csv',
                     index=False, header=True)

"""
convert csv to excel
input: path to csv file (string)
output: excel file with a name we choose
"""
def To_XL(path):
    read_file = pd.read_csv(r''+path)
    print("enter file name: ")
    name = input()
    read_file.to_excel(r'C:\\Users\\or204\\PycharmProjects\\EconomicsProject\\'+name+'.xlsx',
                     index=None, header=True)


"""
A dictionary that keep the probability to be fired 
or to resign from your work
"""
Fired_dict={}
Resigns_dict={}
for i in range(18,110):
    if i<30:
        Fired_dict[i] = 0.07
    elif i<40:
        Fired_dict[i] = 0.05
    elif i<40:
        Fired_dict[i] = 0.04
    elif i<60:
        Fired_dict[i] = 0.03
    elif i<110:
        Fired_dict[i] = 0.02
for i in range(18,110):
    if i<30:
        Resigns_dict[i] = 0.2
    elif i<40:
        Resigns_dict[i] = 0.13
    elif i<50:
        Resigns_dict[i] = 0.10
    elif i < 60:
        Resigns_dict[i] = 0.07
    elif i<110:
        Resigns_dict[i] = 0.03


"""
Read a single cell value from an Excel file
"""
def read_value_from_excel(filename, column, row):
    return pd.read_excel(filename, skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]

#To_CSV('C:\\Users\\or204\\PycharmProjects\\EconomicsProject\\life_table.xlsx')
csv_file = 'life_table_men.csv'
life_table = pd.read_csv(csv_file)




def Get_Value_From_Csv(file_name):
    filename = open(file_name, 'r')
    # creating dictreader object
    file = csv.DictReader(filename)

    AGEm_list=[]
    Lxm_list=[]
    Dxm_list=[]
    Pxm_list=[]
    Qxm_list=[]

    """
     iterating over each row and append
     values to empty list
    """
    for col in file:
        AGEm_list.append(col['Unnamed: 1'])
        Lxm_list.append(col['Unnamed: 2'])
        Dxm_list.append(col['Unnamed: 3'])
        Pxm_list.append(col['Unnamed: 4'])
        Qxm_list.append(col['Unnamed: 5'])

    return AGEm_list, Lxm_list, Dxm_list, Pxm_list, Qxm_list

new_list=Get_Value_From_Csv('life_table_men.csv')

"""
lx: represents the number of persons alive aged x in a life table.
Get_Lx Get 1 parm Age = current  Age
"""
def Get_Lx(Age):
    lx= new_list[1][Age-17]
    return lx
"""
dx: represents the number of persons who die aged x last birthday. dx=lx-lx+1
Get_Dx Get 1 parm Age = current  Age
"""
def Get_Dx(Age):
    dx = new_list[2][Age - 17]
    return dx

"""
qx: represents the probability that a person aged exactly x dies before exact age (x+1). qx= dx/lx
the probability of dying in the next year
Get_Qx Get 1 parm Age = current  Age
"""
def Get_Qx(Age):
    qx= new_list[1][Age-17]
    return qx

"""
px: px represents the probability that a person aged exactly x survives one year to exactly age (x+1).
(the probability of surviving one year)
Get_Px Get 1 parm Age = current  Age
"""
def Get_Px(Age):
    px= new_list[1][Age-17]
    return px
"""
tPx: represents the probability that a person aged exactly x lives for another t years to exact age (x+t).
(The probability of surviving t years)
Get_tPx Get 1 parm Age = current  Age
"""
def Get_tPx(Age):
    print("Enter age t (number of years an individual is expected to live):")
    Age2 = int(input())
    tPx = Get_Lx((Age+Age2)) / Get_Lx(Age)
    return tPx

"""
tqx: represents the probability that a person aged exactly x dies before exact age (x+t).
(The probability of dying within t years)
Get_tQx Get 1 parm Age = current  Age
"""
def Get_tQx(Age):
    #tqx = ( lx - l(x+t) ) / lx
    tQx = 1 - Get_tPx(Age)
    return tQx

"""
s+tPx : represents the probability that a person aged exactly x lives for another t years, and than another s years
to exact age (x+t+s)
probability to lives for another t years * probability to lives for another s years (after t years)
Get_stPx Get 1 parm Age = current  Age
"""
def Get_stPx(Age):
    print("Enter age t (number of years an individual is expected to live):")
    Age2 = int(input())
    tPx = Get_Lx((Age + Age2)) / Get_Lx(Age)
    print("Enter age s (number of years an individual is expected to live after t years):")
    Age3 = int(input())
    Age4=Age+Age2
    s_P_tx = Get_Lx((Age4 + Age3)) / Get_Lx(Age4)

    stPx = tPx * s_P_tx
    return stPx

"""
(n+1)qx : The probability that a person at age x will live n years and die next year.
Get_n1Qx Get 1 parm Age = current  Age
"""
def Get_n1Qx(Age):
    print("Enter Parameter n (number of years a person is expected to live):")
    Age2 = int(input())
    nPx =  Get_Lx((Age + Age2)) / Get_Lx(Age)
    n1_Q_x = nPx * Get_Qx(Age+Age2+1)
    return n1_Q_x
