import Mortality_Table_Women
import Mortality_Table_Men
import Calc_Function_Men
import maya

"""
Compound Interest Calculator (FV)
"""
def Calc_itrest():
    flag = 1
    while(flag==1):
        print("Enter amount: ")
        Amount = float(input())
        print("Enter intwrest: ")
        Interest = float(input())
        print("Enter number of years: ")
        Years = float(input())
        if type(Amount) != float or type(Interest) != float or type(Years) != float:
            flag=1
            print("You entered unexpected value, please ENTER only Numbers!")
        else:
            flag = 0
    New_Amount = Amount
    for i in range(int(Years)):
        New_Amount = New_Amount * (1 + (Interest/100))
    print("Your Amount after " + str(Years) + " years with Interest of " + str(Interest) + " is: ")
    return New_Amount

"""
Present Value Calculator (PV)

Find the amount you will receive at 
the end of the deposit period.
(Find the amount you initially deposited)
"""
def Calc_Present_Value():
    flag = 1
    while(flag==1):
        print("Enter current amount: ")
        Amount = float(input())
        print("Enter interest: ")
        Interest = float(input())
        print("Enter the amount of years that have passed until the money was withdrawn: ")
        Years = float(input())
        if type(Amount) != float or type(Interest) != float or type(Years) != float:
            flag=1
            print("You entered unexpected value, please ENTER only Numbers!")
        else:
            flag = 0
    New_Interest = 1
    for i in range(int(Years)):
        New_Interest = New_Interest * (1 + (Interest/100))
    New_Amount=Amount/New_Interest
    print("The amount of money you deposited was: ")
    return New_Amount

"""
present value of cash flow (Continuous PV)

Find the amount you borrowed based on 
the amount you are required to pay, 
the interest rate, and the number of annual payments.
"""
def Present_Value():
    flag = 1
    while (flag == 1):
        print("Enter the total amount you need to return: ")
        Amount = float(input())
        print("Enter interest: ")
        Interest = float(input())
        print("Enter the number of payments (number of years): ")
        Years = float(input())
        if type(Amount) != float or type(Interest) != float or type(Years) != float:
            flag = 1
            print("You entered unexpected value, please ENTER only Numbers!")
        else:
            flag = 0
    New_Amount = Amount/Years
    PV=0
    for i in range(int(Years)):
        PV += New_Amount / (1 + Interest / 100)**(i+1)
    print("The amount you borrow is: ")
    return PV

#for i in range(1,Calc_Function_Men.Get_Senioruty_By_Years('22/01/2000','25/01/2020')):




def Main_Func(File_name):

    New_file_name = Mortality_Table_Men.To_CSV(File_name)
    New_file_name2 = Mortality_Table_Men.To_CSV(File_name)
    new_list1 = Calc_Function_Men.Create_Data_List(New_file_name)
    new_list2 = Calc_Function_Men.Create_Data_List2(New_file_name2)
    x=Calc_Function_Men.Get_Senioruty_By_Years(Calc_Function_Men.Get_Start_Date('מאיר',"טרבלסי",new_list1),
                                                Calc_Function_Men.Get_leaving_Date('מאיר',"טרבלסי",new_list1))
    for item in new_list1:
        First_Name =item[0]
        Last_Name =item[1]
        Gender =item[2]
        Birth_Date =item[3]
        Start_Work =item[4]
        Salary = item[5]
        Start_Date_Section_14 =item[6]
        Percent_Section_14 =item[7]
        Property_Value =item[8]
        Deposits =item[9]
        Departure_Date =item[10]
        Paid_From_Property =item[11]
        Completion_Payment_Chuck =item[12]
        Leaving_Reason =item[13]
        Senioruty=Calc_Function_Men.Get_Senioruty_By_Years(Calc_Function_Men.Get_Start_Date(First_Name, Last_Name, new_list1),
                                                 Calc_Function_Men.Get_leaving_Date(First_Name, Last_Name, new_list1))
        Age=Calc_Function_Men.Get_Age_By_Days(Birth_Date)//365
        sum=0
        t=0
        S_G_Rate=Calc_Function_Men.Get_Salary_Growth_Rate()
        if Start_Date_Section_14 != None:
            No_SDS14=Senioruty-Calc_Function_Men.Get_Section_14_By_Years\
                (Start_Work, Start_Date_Section_14)
        if Senioruty != type(int):
            continue
        for i in range(1,Age):
            if i<No_SDS14:
                sum1=Salary * Senioruty*((1+S_G_Rate)**(t+0.5))*\
                    (Mortality_Table_Men.Get_tPx(Age))*\
                    (Mortality_Table_Men.Get_Qx(Age))
            else:
                sum2 = Salary * Senioruty * ((1 + S_G_Rate) ** (t + 0.5)) * \
                       (Mortality_Table_Men.Get_tPx(Age)) * \
                       (Mortality_Table_Men.Get_Qx(Age))



Main_Func("data5")

















"""
The probability of dying within T years


def  dying_probability():
    flag = 1
    while (flag == 1):
        print("Enter your age: ")
        Age = float(input())
        print("Enter number of years: ")
        Years = float(input())
        print("Enter the number of payments (number of years): ")
        Years = float(input())
        if type(Amount) != float or type(Interest) != float or type(Years) != float:
            flag = 1
            print("You entered unexpected value, please ENTER only Numbers!")
        else:
            flag = 0
    New_Amount = Amount/Years
    PV=0
    for i in range(int(Years)):
        PV += New_Amount / (1 + Interest / 100)**(i+1)
    print("The amount you borrow is: ")
    return PV
"""
