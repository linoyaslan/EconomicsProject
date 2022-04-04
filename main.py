import Mortality_Table_Women
import Mortality_Table_Men
import Calc_Function_Men
import maya
from math import pow
from dateutil.parser import parse


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
    k=0
    for item in new_list1[0:]:
            First_Name = item[0]
            Last_Name  =item[1]
            Gender = item[2]
            Birth_Date = item[3]
            Start_Work = item[4]
            Salary = float(item[5])
            Start_Date_Section_14 = item[6]
            Percent_Section_14 = item[7]
            if Percent_Section_14 != '':
                Percent_Section_14 = float(item[7])/100
            Property_Value = item[8]
            Deposits = item[9]
            Departure_Date = item[10]
            Paid_From_Property = item[11]
            Completion_Payment_Chuck = item[12]
            Leaving_Reason = item[13]
            Senioruty=float(Calc_Function_Men.Get_Senioruty_By_Years(Calc_Function_Men.Get_Start_Date(First_Name, Last_Name, new_list1)))
            #print((First_Name,Last_Name,Gender,Birth_Date,Start_Work,Salary,Start_Date_Section_14,Percent_Section_14))
            if Gender=='M':
                Age=67
            else:
                Age=64
            Age_2=Calc_Function_Men.Get_Age_By_Days(Birth_Date)//365

            sum1=0
            Sum=0
            Years_without_section_14=0
            S_G_Rate=Calc_Function_Men.Get_Salary_Growth_Rate()

            if Start_Date_Section_14 != '':
                No_SDS14=Calc_Function_Men.Get_Section_14_By_Years\
                    (Start_Work, Start_Date_Section_14)
            else:
                No_SDS14=-1

            if No_SDS14 == -1:
                sum1 += (Salary * Senioruty * ((1 + S_G_Rate) ** (0 + 0.5)) * \
                       (Mortality_Table_Men.Get_tPx(Age,0)) * \
                       (Mortality_Table_Men.Get_tQx(Age,0)))/pow(
                    1 + Calc_Function_Men.Get_Discounting(1, new_list2), (0 + 0.5))

                for i in range(1, Age - Age_2):
                    sum1 += float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5)) * \
                                                             (Mortality_Table_Men.Get_tPx(Age, i)) * \
                                                             (Mortality_Table_Men.Get_tQx(Age, i)) / pow(
                                    1 + Calc_Function_Men.Get_Discounting(i, new_list2), (i + 0.5)))

            else:
                for i in range(No_SDS14):
                    t=1
                    sum1 += float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5)) * \
                                                         (Mortality_Table_Men.Get_tPx(Age, t)) * \
                                                        (Mortality_Table_Men.Get_tQx(Age, t)) /
                                                pow(1 + Calc_Function_Men.Get_Discounting(t, new_list2), (i + 0.5)))
                    t+=1
                for i in range(1, Age - Age_2-No_SDS14+1):
                    sum1 += float(Salary * Senioruty)*(1-Percent_Section_14) * (pow((1 + S_G_Rate), (i + 0.5)) * \
                                                                 (Mortality_Table_Men.Get_tPx(Age, i)) * \
                                                                 (Mortality_Table_Men.Get_tQx(Age, i)) / pow(
                                        1 + Calc_Function_Men.Get_Discounting(i, new_list2), (i + 0.5)))
            Sum += sum1
            if Leaving_Reason!='':
                Sum=0
            print(First_Name+' '+ Last_Name+ ' '+str(Sum))
    #     # if Senioruty <= 3:
    #     #     Sum=sum1+sum2
    #     #     Sum=Sum-Property_Value
    #     # else:
    #     #     Sum=sum1+sum2


Main_Func("test")
