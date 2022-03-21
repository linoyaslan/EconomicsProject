import pandas as pd

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
    return pd.read_excel(filename, sheet_name='נשים', skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]


"""
Open the Excel file and read from it
"""
excel_file = 'life_table.xlsx'
life_table = pd.read_excel(excel_file)

"""
Lists that save the value of Lx Dx Px Qx from the Excel life table - for women
"""
AGEw_list=[]
Lxw_list=[]
Dxw_list=[]
Pxw_list=[]
Qxw_list=[]

"""
Enter the values from the Excel life table file into the lists
"""
for i in range(1,len(life_table)):
    AGEw_list.append(read_value_from_excel(excel_file,'B',i+2))
    Lxw_list.append(read_value_from_excel(excel_file,'C',i+2))
    Dxw_list.append(read_value_from_excel(excel_file,'D',i+2))
    Pxw_list.append(read_value_from_excel(excel_file,'E',i+2))
    Qxw_list.append(read_value_from_excel(excel_file,'F',i+2))

"""
lx: represents the number of persons alive aged x in a life table.
Get_Lx Get 1 parm Age = current  Age
"""
def Get_Lx(Age):
    lx= Lxw_list[Age-18]
    return lx

"""
dx: represents the number of persons who die aged x last birthday. dx=lx-lx+1
Get_Dx Get 1 parm Age = current  Age
"""
def Get_Dx(Age):
    dx = Dxw_list[Age - 18]
    return dx

"""
qx: represents the probability that a person aged exactly x dies before exact age (x+1). qx= dx/lx
the probability of dying in the next year
Get_Qx Get 1 parm Age = current  Age
"""
def Get_Qx(Age):
    qx= Qxw_list[Age-18]
    return qx

"""
px: px represents the probability that a person aged exactly x survives one year to exactly age (x+1).
(the probability of surviving one year)
Get_Px Get 1 parm Age = current  Age
"""
def Get_Px(Age):
    px= Qxw_list[Age-18]
    return px

"""
tPx: represents the probability that a person aged exactly x lives for another t years to exact age (x+t).
(The probability of surviving t years)
Get_tPx Get 1 parm Age = current  Age
"""
def Get_tPx(Age):
    print("Enter age t (number of years an individual is expected to live:)")
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
    print("Enter age t (number of years an individual is expected to live:)")
    Age2 = int(input())
    tPx = Get_Lx((Age + Age2)) / Get_Lx(Age)
    print("Enter age s (number of years an individual is expected to live after t years:)")
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
    print("Enter Parameter n (number of years an individual is expected to live:)")
    Age2 = int(input())
    nPx =  Get_Lx((Age + Age2)) / Get_Lx(Age)
    n1_Q_x = nPx * Get_Qx(Age+Age2+1)
    return n1_Q_x

"""
The probability that a person at age X will leave his job after t years.
Get_Chance_To_Leave Get 1 parm Age = current  Age
"""
def Get_Chance_To_Leave(Age):
    print("Enter y (The number of years a person is expected to leave his workplace:)")
    Age2 = int(input())
    result = 1.0
    for i in range(Age+1,(Age+Age2)):
        result = result*(1-(Fired_dict[i] + Resigns_dict[i] + Get_Qx(i)))
    return result
