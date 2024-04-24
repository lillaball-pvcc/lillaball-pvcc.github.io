# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James ",
    "Johnson, Patricia",
    "Brown, Michael ",
    "Jones, Elizabeth ",
    "Garcia, Brian ",
    "Miller, Deborah ",
    "Davis, Timothy ",
    "Rodriguez, Ronald",
    "Martinez, Karen ",
    "Hernandez, Lisa ",
    "Lopez, Nancy ",
    "Gonzales, Betty ",
    "Wilson, Sandra ",
    "Anderson, Margie ",
    "Thomas, Daniel ",
    "Taylor, Steven ",
    "Moore, Andrew ",
    "Jackson, Donna ",
    "Martin, Yolanda ",
    "Lee, Carolina ",
    "Perez, Kevin ",
    "Thompson, Brian ",
    "White, Deborah ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

######### NEW LISTS for calculated amounts #####

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

############# TUPLES of constants ############
#           C      S       J      M
# indexes   0      1       2      3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed  state  ss  med  ret
# indexes    0     1    2    3    4
DED_RATE = (.12, .03, .062, .0145, .04 )

############# define program functions #############
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):

    #calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

    #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        ss = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]
        total = fed + state + ss + med + ret
        net = pay - fed - state - ss - med - ret

    #add to totals
        total_gross += pay
        total_net += net

    #append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(ss)
        medicare.append(med)
        ret401k.append(ret)
        net_pay.append(net)

def display_results():
    currency = '8,.2f'
    line = '-------------------------------------------------'
    tab = "\t"

    print(line)
    print('*********** FRESH FOODS MARKET ***********')
    print('---------- WEEKLY PAYROLL REPORT ---------')
    print(tab +  str(datetime.datetime.now()))
    print(line)
    titles1 = "EMP NAME" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    print(titles1 + titles2)
    
        
    for i in range(num_emps):
        data1 = " Smith, Jones" + C + format(gross_pay[i],currency)
        print(data1)
        data2 =  "Johnson, Patricia " + job[S]+ format(gross_pay[i],currency)
        print(data2)
        data3 = emp[i] + " Brown, Micheal" + job[M]+ format(gross_pay[3],currency)
        print(data3)
        data4 = emp[i] + " Jones, Elizabeth" + job[C]+ format(gross_pay[0],currency)
        print(data4)
        data5 = emp[i] + " Garcia, Brian" + job[C]+ format(gross_pay[0],currency)
        print(data5)
        data6 = emp[i] + " Miller, Deborah" + job[C]+ format(gross_pay[0],currency)
        print(data6)
        data7 = emp[i] + " Davis, Timothy" + job[C]+ format(gross_pay[0],currency)
        print(data7)
        data8 = emp[i] + " Rodriguez, Ronald" + job[S]+ format(gross_pay[1],currency)
        print(data8)
        data9 = emp[i] + " Martinez, Karen" + job[M]+ format(gross_pay[3],currency)
        print(data9)
        data10 = emp[i] + " Hernandez, Lisa" + job[C]+ format(gross_pay[0],currency)
        print(data10)
        data11 = emp[i] + "Lopez, Nancy " + job[S]+ format(gross_pay[1],currency)
        print(data11)
        data12 = emp[i] + "Gonzales, Betty " + job[C]+ format(gross_pay[0],currency)
        print(data12)
        data13 = emp[i] + "Wilson, Sandra " + job[C]+ format(gross_pay[0],currency)
        print(data13)
        data14 = emp[i] + " Anderson, Margie" + job[S]+ format(gross_pay[1],currency)
        print(data14)
        data15 = emp[i] + " Thomas, Daniel" + job[C]+ format(gross_pay[0],currency)
        print(data15)
        data16 = emp[i] + "Taylor, Steven " + job[C]+ format(gross_pay[0],currency)
        print(data16)
        data17 = emp[i] + "Moore, Andrew " + job[M]+ format(gross_pay[3],currency)
        print(data17)
        data18 = emp[i] + "jackson, Donna " + job[J]+ format(gross_pay[2],currency)
        print(data18)
        data19 = emp[i] + "Martin, Yolanda " + job[S]+ format(gross_pay[1],currency)
        print(data19)
        data20 = emp[i] + "Lee, Carolina " + job[S]+ format(gross_pay[1],currency)
        print(data20)
        data21 = emp[i] + "Perez, Kevin " + job[C]+ format(gross_pay[0],currency)
        print(data21)
        data22 = emp[i] + " Thompson, Brian" + job[S]+ format(gross_pay[1],currency)
        print(data22)
        data23 = emp[i] + " White, Deborah" + job[M]+ format(gross_pay[3],currency)
        print(data23)
    print(line)
    print("********************TOTAL GROSS: $" + format(total_gross, currency))
    print("********************TOTAL NET  : $" + format(total_net, currency))
    print(line)

######## call on main program to execute ########
main()




    
            
            
     
        
        




