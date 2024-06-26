#Name: Lilla Ball
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.png"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights

            elif room_type == "DR":
                subtotal = ROOM_RATES[0] * num_nights

            else:
                subtotal = ROOM_RATES[0] * num_nights
                
      
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy 
             
            grandtotal += total
        
       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
            guest[i].append(grandtotal)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style = background color: rgb(241, 241, 241);font-family: Verdana, Geneva, Tahoma, sans-serif;>')
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'


    
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + "emerald-web-page.png" + ' to view data.')
    
    

##call on main program to execute##
main()
