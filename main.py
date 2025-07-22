from read import *
from write import *
from operations import *
import datetime;


print("\n\n\n\t\t\t\t\t\t Techno Property Nepal")
print("\t\t\t\t\t\tKamalpokhari, Kathmandu")
print("\t\t\t\t\t\t"+"-"*23)

'''for unique name in bills'''
unique_bill=str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second)
date_bill=str(datetime.datetime.now().year)+"."+str(datetime.datetime.now().month)+"."+str(datetime.datetime.now().day) #for date in bill
loop=True
while(loop):
    print("\n\nTo view all rental properties, press 1")
    print("To rent a land, press 2")
    print("To return the land, press 3")
    print("To exit, press 4")
    while(True):
        try:
            reply=int(input("\nWhat would you like to do?\n-> "))
            break
        except:
            print("Invalid Format, Please provide proper values")
    newlist=read()
    if (reply==1):
        viewAllLands(newlist)
    elif (reply==2):
        rent_count=0            #for opening the bill in a mode or w mode, for renting multiple land & to not ask name again for renting more land by same person
        rented_list=[]          #list of row index of renting lands, for renting multiple land
        rent_more_outer=0       #for rent more land loop, for renting multiple land    
        duration_list=[]        #list for rental duration 
        while(rent_more_outer==0):
            viewAllLands(newlist)
            valid_kitta=True    #to run try except block in loop
            while valid_kitta:  #to check if kitta is in proper format
                try:
                    kitta=int(input("\nEnter kitta no. of the land you would like to rent:\n-> "))
                    valid_kitta=False
                except:
                    print("Invalid Format, Please provide proper values")
            in_loop=0           #to loop again from check_kitta
            while (in_loop==0):
                i=check_kitta(newlist,kitta)
                if(i==-1):
                    rent_more_outer=1   #to exit to main menu
                    break
                available=check_availability(newlist,i)
                if(available==-1):
                    rent_more_outer=1   #to exit to main menu
                    break
                elif(available==0):
                    if(rent_count==0):
                        name=input("\nEnter your full name:\n-> ")
                    valid_duration=True
                    while True:
                        while valid_duration:
                            try:
                                duration=int(input("\nHow long would you like to rent this land?(in months)\n-> "))
                                break
                            except:
                                print("Invalid Format, Please provide proper values")
                        if(duration<1):
                            print("Please enter valid duration for renting")
                        else:
                            duration_list.append(duration)
                            break
                    rent_more=0         #to loop again to rent more land
                    while(rent_more==0):
                        while True:
                            try:
                                rent_more_reply=int(input("\nWould you like to rent more lands?\nPress 1 to rent more lands\nPress 2 to complete the renting process\n-> "))
                                break
                            except:
                                print("Invalid Format, Please provide proper values")
                        
                        if(rent_more_reply==1):     #for renting first land
                            in_loop=1
                            rented_list.append(i)
                            bill(i,newlist,name,duration,rent_count,unique_bill,date_bill)
                            rent_count+=1
                            change_data(newlist,i)
                            break
                        elif(rent_more_reply==2):   #for renting multiple land
                            rented_list.append(i)
                            bill(i,newlist,name,duration,rent_count,unique_bill,date_bill)
                            change_data(newlist,i)
                            bill_total(newlist,name,rented_list,unique_bill,duration_list)
                            print_bill(newlist,name,duration_list,rented_list,unique_bill,date_bill)
                            print("\n\n\n\t\t\t\t\t\tWelcome to the Techno Property Nepal family.\n")
                            in_loop=1
                            rent_more_outer=1
                            break  
                        else:
                            print("Invalid input detected, Please provide valid number")    
                else:
                    kitta=available

             
    elif(reply==3):
        return_list=[]
        duration_ini_list=[]
        duration_fin_list=[]
        fine_list=[]
        return_loop=True
        return_count=0      #to not ask name again while rentint multiple lands
        while(return_loop):
            viewAllLands(newlist)
            while True:
                try:
                    return_land_no=int(input("\nEnter kitta number of the land you would like to return:\n-> "))
                    break
                except:
                    print("Invalid format, Please provide proper values")
            not_available=0     #to loop from check kitta
            while(not_available==0):
                i=check_kitta(newlist,return_land_no)
                if(i==-1):
                    return_loop=False
                    break
                unavailable=check_unavailability(newlist,i)
                if(unavailable==-1):
                    return_loop=False
                    break
                elif(unavailable==0):
                    if(return_count==0):
                        name=input("\nEnter your full name:\n-> ")
                    while True:
                        while(True):
                            try:
                                duration_ini=int(input("\nEnter the duration of rent as per the contract\n-> "))
                                break
                            except:
                                print("Invalid Format, Please provide proper values")
                        if(duration_ini<1):
                            print("Please enter valid duration for renting")
                        else:
                            break
                    while True:
                        while(True):
                            try:
                                duration_final=int(input("\nEnter the actual duration of rent:\n-> "))
                                break
                            except:
                                print("Invalid Format, Please provide proper values")
                        if(duration_final<1):
                            print("Please enter valid duration for renting")
                        else:
                            break
                    fine=check_fine(duration_ini,duration_final)
                    fine_list.append(fine)
                    while(True):
                        while(True):
                            try:
                                return_more=int(input("\nWould you like to return more lands?\nPress 1 to return more land\nPress 2 to complete the returning process\n-> "))
                                break
                            except:
                                print("Invalid Format, Please provide proper values")
                        if(return_more==1):
                            change_data_return(newlist,i)
                            return_list.append(i)
                            duration_ini_list.append(duration_ini)
                            duration_fin_list.append(duration_final)
                            return_count+=1
                            not_available=1
                            break
                        elif(return_more==2):
                            return_list.append(i)
                            duration_ini_list.append(duration_ini)
                            duration_fin_list.append(duration_final)
                            return_note(newlist,return_list,name,duration_ini_list,duration_fin_list,unique_bill,date_bill,fine_list) 
                            change_data_return(newlist,i)
                            print_ret_bill(newlist,return_list,name,duration_ini_list,duration_fin_list,unique_bill,date_bill,fine_list)
                            print("\n\n\n\t\t\t\t\tLand returned sucessfully")
                            return_loop=False
                            not_available=1
                            break
                        else:
                            print("Invalid number, Please provide valid number")
                else:
                    return_land_no=unavailable

    elif(reply==4):
        print("\n\n\n\t\t\t\t\t\tThank you for choosing us\n\n")
        loop=False  # to exit the system
    else:
        print("Invalid number, Please provide valid value.")











    








    


    
    

        





