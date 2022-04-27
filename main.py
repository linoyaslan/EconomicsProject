import csv

import Mortality_Table_Women
import Mortality_Table_Men
import Calc_Function_Men
import maya
from math import pow
from dateutil.parser import parse
#
#
# """
# Compound Interest Calculator (FV)
# """
# def Calc_itrest():
#     flag = 1
#     while(flag==1):
#         print("Enter amount: ")
#         Amount = float(input())
#         print("Enter intwrest: ")
#         Interest = float(input())
#         print("Enter number of years: ")
#         Years = float(input())
#         if type(Amount) != float or type(Interest) != float or type(Years) != float:
#             flag=1
#             print("You entered unexpected value, please ENTER only Numbers!")
#         else:
#             flag = 0
#     New_Amount = Amount
#     for i in range(int(Years)):
#         New_Amount = New_Amount * (1 + (Interest/100))
#     print("Your Amount after " + str(Years) + " years with Interest of " + str(Interest) + " is: ")
#     return New_Amount
#
# """
# Present Value Calculator (PV)
#
# Find the amount you will receive at
# the end of the deposit period.
# (Find the amount you initially deposited)
# """
# def Calc_Present_Value():
#     flag = 1
#     while(flag==1):
#         print("Enter current amount: ")
#         Amount = float(input())
#         print("Enter interest: ")
#         Interest = float(input())
#         print("Enter the amount of years that have passed until the money was withdrawn: ")
#         Years = float(input())
#         if type(Amount) != float or type(Interest) != float or type(Years) != float:
#             flag=1
#             print("You entered unexpected value, please ENTER only Numbers!")
#         else:
#             flag = 0
#     New_Interest = 1
#     for i in range(int(Years)):
#         New_Interest = New_Interest * (1 + (Interest/100))
#     New_Amount=Amount/New_Interest
#     print("The amount of money you deposited was: ")
#     return New_Amount
#
# """
# present value of cash flow (Continuous PV)
#
# Find the amount you borrowed based on
# the amount you are required to pay,
# the interest rate, and the number of annual payments.
# """
# def Present_Value():
#     flag = 1
#     while (flag == 1):
#         print("Enter the total amount you need to return: ")
#         Amount = float(input())
#         print("Enter interest: ")
#         Interest = float(input())
#         print("Enter the number of payments (number of years): ")
#         Years = float(input())
#         if type(Amount) != float or type(Interest) != float or type(Years) != float:
#             flag = 1
#             print("You entered unexpected value, please ENTER only Numbers!")
#         else:
#             flag = 0
#     New_Amount = Amount/Years
#     PV=0
#     for i in range(int(Years)):
#         PV += New_Amount / (1 + Interest / 100)**(i+1)
#     print("The amount you borrow is: ")
#     return PV

def Get_Senioruty(First_Name,Last_Name, new_list1):
    return float(
        Calc_Function_Men.Get_Senioruty_By_Years(Calc_Function_Men.Get_Start_Date(First_Name, Last_Name, new_list1)))


def Main_Func(File_name):
    New_file_name = Mortality_Table_Men.To_CSV(File_name)
    New_file_name2 = Mortality_Table_Men.To_CSV(File_name)
    new_list = Calc_Function_Men.Create_Data_List(New_file_name)
    new_list2 = Calc_Function_Men.Create_Data_List2(New_file_name2)
    new_list1= new_list[1:]
    k=1
    new_list3 = [["", 'First Name', 'Last Name', 'Retirement Compensation']]
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
            else:
                Percent_Section_14=0
            Property_Value = float(item[8])
            Deposits = item[9]
            Departure_Date = item[10]
            Paid_From_Property = item[11]
            Completion_Payment_Chuck = item[12]
            Leaving_Reason = item[13]
            Senioruty = Get_Senioruty(First_Name, Last_Name, new_list1)
            if Gender=='M':
                Age=67
            else:
                Age=64

            Age_2=Calc_Function_Men.Get_Age_By_Days(Birth_Date)//365
            if Age_2 >= 67 and Gender=='M':
                Sum = Salary * Senioruty
                print(First_Name + ' ' + Last_Name + ' ' + str(Sum))
                new_list3.append([k, item[0], item[1], Sum,'More Then 67'])
                k = k + 1
                continue
            if Age_2 >= 64 and Gender=='F':
                Sum = Salary * Senioruty
                print(First_Name + ' ' + Last_Name + ' ' + str(Sum))
                new_list3.append([k, item[0], item[1], Sum,'More Then 64'])
                k = k + 1
                continue
            sum1 = 0
            sum2 = 0
            sum3 = 0
            Sum=0
            last_year1 = 0
            last_year2 = 0
            last_year3 = 0
            last_year4 = 0
            S_G_Rate=Calc_Function_Men.Get_Salary_Growth_Rate()
            if Start_Date_Section_14 != '':
                No_SDS14=Calc_Function_Men.Get_Section_14_By_Years(Start_Work, Start_Date_Section_14)
                if No_SDS14<1 and No_SDS14>0:
                    No_SDS14=1
                else:
                    No_SDS14=int(No_SDS14)
            else:
                No_SDS14=-1
            Next_Senioruty=Senioruty
            if No_SDS14 == -1:
                for i in range(1, Age - (Age_2+2)):
                    Px = Calc_Function_Men.Get_Chance_To_Stay(Age_2, i, Gender)
                    temp = Calc_Function_Men.Get_Discounting(i, new_list2)
                    temp2 = Mortality_Table_Men.Resigns_dict[Age_2+i]
                    temp3 = Mortality_Table_Men.Fired_dict[Age_2 + i]
                    if Gender == 'M':
                        temp4=Mortality_Table_Men.Get_Qx((i+Age_2))
                    else:
                        temp4=Mortality_Table_Women.Get_Qx((i+Age_2))

                    sum1 += (float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5-1)) * Px * temp3) / pow(1 + temp, (i + 0.5-1)))
                    sum2 += (float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5-1)) * Px * temp4) / pow(1 + temp, (i + 0.5-1)))
                    if Next_Senioruty >= 3: sum3 += Property_Value * Px * temp2
                    Next_Senioruty+=1


            else:
                flag=0
                if No_SDS14>0:
                    for i in range(1,No_SDS14+2):
                        flag=1
                        Px = Calc_Function_Men.Get_Chance_To_Stay(Age_2, i, Gender)
                        temp = Calc_Function_Men.Get_Discounting(i , new_list2)
                        temp2 = Mortality_Table_Men.Resigns_dict[Age_2 + i]
                        temp3 = Mortality_Table_Men.Fired_dict[Age_2 + i]
                        if Gender == 'M':
                            temp4 = Mortality_Table_Men.Get_Qx(Age_2+i)
                        else:
                            temp4 = Mortality_Table_Women.Get_Qx((Age_2+i))

                        sum1 += float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5-1)) * Px * temp3) / pow(1 + temp, (i + 0.5-1))
                        sum2 += float(Salary * Senioruty) * (pow((1 + S_G_Rate), (i + 0.5-1)) * Px * temp4) / pow(1 + temp, (i + 0.5-1))
                        if Next_Senioruty >= 3: sum3 += Property_Value * Px * temp2
                        Next_Senioruty += 1

                Next_Senioruty = Senioruty
                for i in range(1, Age - (Age_2+2)):
                    Px = Calc_Function_Men.Get_Chance_To_Stay(Age_2, i, Gender)
                    temp = Calc_Function_Men.Get_Discounting(i, new_list2)
                    temp2 = Mortality_Table_Men.Resigns_dict[Age_2 + i]
                    temp3 = Mortality_Table_Men.Fired_dict[Age_2 + i]
                    if Gender == 'M':
                        temp4 = Mortality_Table_Men.Get_Qx((Age_2 + i))
                    else:
                        temp4 = Mortality_Table_Men.Get_Qx((Age_2 + i))
                    sum1 += (float(Salary*Senioruty)*(1-Percent_Section_14)*pow((1+S_G_Rate),(i+0.5-1))*Px*temp3)/pow(1+temp,(i+0.5-1))
                    sum2 += (float(Salary*Senioruty)*(1-Percent_Section_14)*pow((1+S_G_Rate),(i+0.5-1))*Px*temp4)/pow(1+temp,(i+0.5-1))
                    if flag!=1:
                        if Next_Senioruty >= 3: sum3 += Property_Value * Px * temp2
                    Next_Senioruty += 1

            if Gender == 'M':
                    temp4 = Mortality_Table_Men.Get_Qx((Age_2+i))
            else:
                    temp4 = Mortality_Table_Women.Get_Qx((Age_2+i))


            if No_SDS14 == -1 and Leaving_Reason == '' and Percent_Section_14==0:
                last_year1 += temp5 * (float(Salary * Senioruty) *
                                       (1 - Percent_Section_14) *
                                       (pow((1 + S_G_Rate), (Age - 1 - Age_2 + 0.5)) *
                                        Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) * temp4) /
                                       pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2),
                                           (Age - 1 - Age_2 + 0.5)))
                last_year2 = float(Salary * Senioruty) * \
                             (1) * \
                             (pow((1 + S_G_Rate), (Age - Age_2)) *
                              Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) *
                              (1 - temp4 - Mortality_Table_Men.Resigns_dict[Age - 1] - Mortality_Table_Men.Fired_dict[
                                  Age - 1])) \
                             / pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2))

                if Next_Senioruty >= 3: last_year3 += temp5 * Property_Value * \
                                                      (Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1,
                                                                                            Gender)) * \
                                                      Mortality_Table_Men.Resigns_dict[Age - 1]
                # Q1
                last_year4 += temp5 * float(Salary * Senioruty) * \
                              (1 - Percent_Section_14) * \
                              (pow((1 + S_G_Rate), (Age - Age_2 + 0.5)) *
                               Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) *
                               Mortality_Table_Men.Fired_dict[Age - 1]) \
                              / pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2 + 0.5))


            elif No_SDS14>0 and Percent_Section_14!=0 and Leaving_Reason == '':
                temp5=No_SDS14/(Age-Age_2+Senioruty)+0.15
                last_year1 += temp5 * (float(Salary * Senioruty) *
                                       (1 - Percent_Section_14) *
                                       (pow((1 + S_G_Rate), (Age - 1 - Age_2 + 0.5)) *
                                        Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) * temp4) /
                                       pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2),
                                           (Age - 1 - Age_2 + 0.5)))
                last_year2 = float(Salary * Senioruty) *\
                                  (1*temp5) *\
                                  (pow((1 + S_G_Rate), (Age - Age_2)) *
                                  Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2-1, Gender) *
                                  (1-temp4 - Mortality_Table_Men.Resigns_dict[Age - 1] -Mortality_Table_Men.Fired_dict[Age - 1]))\
                                  /pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2))

                if Next_Senioruty >= 3: last_year3 += temp5 * Property_Value * \
                                                      (Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1,
                                                                                            Gender)) * \
                                                      Mortality_Table_Men.Resigns_dict[Age - 1]
                # Q1
                last_year4 += temp5 * float(Salary * Senioruty) * \
                              (1 - Percent_Section_14) * \
                              (pow((1 + S_G_Rate), (Age - Age_2 + 0.5)) *
                               Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) *
                               Mortality_Table_Men.Fired_dict[Age - 1]) \
                              / pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2 + 0.5))

            else:
                temp5 = 1 - (No_SDS14 / (Age - Age_2 + Senioruty))
                #Q3
                last_year1 += temp5*(float(Salary * Senioruty) *
                                      (1-Percent_Section_14) *
                                      (pow((1 + S_G_Rate), (Age - 1 - Age_2 + 0.5)) *
                                      Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender)* temp4)/
                                      pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - 1 - Age_2 + 0.5)))
                #last year
                if Percent_Section_14<1:
                    last_year2 += 0.9*temp5*float(Salary * Senioruty) *\
                                          (1-Percent_Section_14) *\
                                          (pow((1 + S_G_Rate), (Age - Age_2)) *
                                          Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2-1, Gender) *
                                          (1-temp4 - Mortality_Table_Men.Resigns_dict[Age - 1] -Mortality_Table_Men.Fired_dict[Age - 1]))\
                                          /pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2))

                #Q2
                if Next_Senioruty>=3:last_year3 += temp5*Property_Value * \
                                     (Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender)) *\
                                     Mortality_Table_Men.Resigns_dict[Age - 1]
                #Q1
                last_year4 += temp5*float(Salary * Senioruty) *\
                                 (1-Percent_Section_14) *\
                                 (pow((1 + S_G_Rate), (Age - Age_2 + 0.5)) *
                                 Calc_Function_Men.Get_Chance_To_Stay(Age_2, Age - Age_2 - 1, Gender) *
                                 Mortality_Table_Men.Fired_dict[Age - 1])\
                                 /pow(1 + Calc_Function_Men.Get_Discounting(Age - Age_2, new_list2), (Age - Age_2 + 0.5))

            Sum = sum1+sum2+sum3+last_year1+last_year2+last_year3+last_year4
            if Next_Senioruty > 3 and Sum < Property_Value:
                Sum = Property_Value
            if Leaving_Reason != '':
                Sum=0
            new_list3.append([k,item[0], item[1], Sum])
            print(k,end='. ')
            k=k+1
            print(str(Sum))
    with open("C:\\Users\\or204\\PycharmProjects\\EconomicsProject\\myfile.csv", 'a', newline='') as myfile:
        for i in new_list3:
            writer = csv.writer(myfile)
            writer.writerow(i)



Main_Func("data5")
