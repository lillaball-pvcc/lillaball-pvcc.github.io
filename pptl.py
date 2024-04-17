# Name: Lilla Ball
# Program Purpose: This program uses lists to find personal property tax for vehicles
#   in Charlottesville and produces a report which displays all data and the total tax due
#   for six months
#
# Personal property tax in Charlottesville:
#       -- 4.20% per year
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Owned or leased vehicles which are predominately used for non-business purposes & have passenger license plates. (These vehicles do not have to pay a license fee.)
#       -- Tax relief rate is 33%

import datetime

################# define tax rates #################
PPT_RATE = .042
RELIEF_RATE = .33

#define global variables
vehicle_value = 0
eligible_relief = 1  # 1 for yes, 2 for no

relief_amt = 0
annual_tax_amt = 0
six_month_tax_amt = 0
total = 0
total_due = 0


############## define program function ##############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate your personal property tax for a vehicle in Charlottesville again(Y or N)? ")
        if yesno.upper() == "N" :
            more = False
            print("Thank you. Have a nice day!")

def get_user_data():
    global vehicle_value, eligible_relief
    print('****PERSONAL PROPERTY TAX CALCULATOR FOR CHARLOTTESVILLE ****')
    vehicle_value = int(input(" Assessed vehicle value: "))
    eligible_relief = int(input(" Are you Eligible for relief? Enter a 1 for yes; enter a 2 for no: "))

def perform_calculations():
    global relief_amt, annual_tax_amt, six_month_tax_amt,total_due
    if eligible_relief == 1:
        relief_amt = six_month_tax_amt * RELIEF_RATE
        annual_tax_amt = vehicle_value * PPT_RATE
        six_month_tax_amt = annual_tax_amt / 2
        total_due = six_month_tax_amt - relief_amt
        
    else:
        relief_amt = 0
        annual_tax_amt = vehicle_value * PPT_RATE
        six_month_tax_amt = annual_tax_amt / 2
        total_due = six_month_tax_amt - relief_amt
       

def display_results():
    currency = '8,.2f'
    line = '----------------------------------------'

    print(line)
    print('****PERSONAL PROPERTY TAX  ****')
    print('    City of Charlottesville, Virginia')
    print('Assessed value of the vehicle     $ ' + format(vehicle_value,currency))
    print('Annual Amount Owed                $ ' + format(annual_tax_amt,currency))
    print('Six Month Tax Fee                 $ ' + format(six_month_tax_amt,currency))
    print('Relief Amount                     $ ' + format(relief_amt,currency))
    print('Total Due                         $ ' + format(total_due,currency))
    print(str(datetime.datetime.now()))
    print(line)


##########  call on main program to execute  ##########
main()




        
