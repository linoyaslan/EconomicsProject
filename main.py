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



def Main_Func(File_name):
    New_file_name = Mortality_Table_Men.To_CSV(File_name)
    new_list = Calc_Function_Men.Create_Data_List(New_file_name)
    x=Calc_Function_Men.Get_Senioruty_By_Years(Calc_Function_Men.Get_Start_Date('מאיר',"טרבלסי",new_list),
                                               Calc_Function_Men.Get_leaving_Date('מאיר',"טרבלסי",new_list))
    print(Calc_Function_Men.Get_Salary('מאיר',"טרבלסי",new_list))
    print(x)


Main_Func("data.xlsx")

















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
