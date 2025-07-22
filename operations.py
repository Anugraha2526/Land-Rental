from read import *


'''to view all land's details'''
def viewAllLands(newlist):
    print()
    for line in newlist:  
        for item in line:  
            print(item,end="\t\t") 
        print()  

    

def check_kitta(newlist,kitta):
    for i in range(len(newlist)):
        if(newlist[i][0]==str(kitta)):  
            return i
    reply=input("\nPlease enter valid kitta no. or Type exit to return to main menu:\n-> ")
    if (reply.lower()=="exit"):
        return -1
    else:
        return check_kitta(newlist,reply)
    
            

def check_availability(newlist,i):
    check_avai_list=newlist
    check_avai_list[i][-1]=check_avai_list[i][-1].replace(" ","")
    if(check_avai_list[i][-1].lower()=="available"):
        return 0
    else:
        print("\nThe selected land is not available to rent.")
        reply=input("Please select another kitta no. OR Type exit to return to main menu:\n-> ")
        if (reply.lower()=="exit"):
            return -1
        else:
            return reply
    
def print_bill(newlist,name,duration,rented,unique,date):
    dur=0
    print("\n\n\n\t\t\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t\t\tKamalpokhari, Kathmandu")
    print("\t\t\t\t\t\t"+"-"*23+"\n")
    print("Date: "+date)
    print("Bill no.: "+unique)
    print("\n"+"="*131+"\n")
    print("Name: "+name.upper())
    for i in rented:  
        print("\nKitta Number: "+newlist[i][0])
        print("City/District: "+newlist[i][1])
        print("Direction of Land: "+newlist[i][2])
        print("Area of Land (Anna): "+newlist[i][3])
        print("\nDuration of rent: ",duration[dur])
        print("\nAmount: ",int(newlist[i][4])*duration[dur]) 
        print("\n"+"="*131)
        dur+=1 
    total=0
    print("\nTotal Amount:",end=" ")   
    count=0
    dur=0
    for i in rented:   
        if(count==0):
            print(int(newlist[i][4])*duration[dur],end=" ") 
        else:
            print("+",int(newlist[i][4])*duration[dur],end=" ")
        count+=1
        dur+=1
        total+=int(newlist[i][4])
    if(count>1):
        print("=",total)
        

def check_unavailability(newlist,i):
    check_unavai_list=newlist
    check_unavai_list[i][-1]=check_unavai_list[i][-1].replace(" ","")
    if(check_unavai_list[i][-1].lower()=="notavailable"):
        return 0
    else:
        print("\nThe selected land has not been rented")
        reply=input("Please select another kitta no. OR Type exit to return to main menu:\n-> ")
        if (reply.lower()=="exit"):
            return -1
        else:
            return reply

def print_ret_bill(newlist,return_list,name,ini,fin,unique,date,fine_list):
    dur=0
    total_amt=0
    print("\n\n\n\t\t\t\t\t\t Techno Property Nepal")
    print("\t\t\t\t\t\tKamalpokhari, Kathmandu")
    print("\t\t\t\t\t\t"+"-"*23+"\n")
    print("Date: "+date)
    print("Bill no.: "+unique+"\n")
    print("="*131+"\n")
    print("Name: "+name.upper()+"\n")
    for i in return_list:
        print("Kitta Numer: "+newlist[i][0])
        print("City/District: "+newlist[i][1])
        print("Direction of Land: "+newlist[i][2])
        print("Area of Land (Anna): "+newlist[i][3]+"\n")
        print("Duration of rent according to contract: "+str(ini[dur]))
        print("Actual duration of rent : "+str(fin[dur])+"\n")
        if(fine_list[dur]!=0):
            amount=int(newlist[i][4])*fin[dur]
            print("Amount: "+str(newlist[i][4])+" x "+str(fin[dur])+" = "+str(amount))
        else:
            amount=int(newlist[i][4])*ini[dur]
            print("Amount: "+str(newlist[i][4])+" x "+str(ini[dur])+" = "+str(amount))
        total_amt+=amount
        print()
        print("="*131+"\n")
        dur+=1
    
    if(fine_list[0]!=0):
        print("Post contract termination fine:")
    total_fine=0
    total=0
    dur=0
    for i in return_list:
        print("\nFor Kitta no.: "+ newlist[i][0])
        fine=(int(newlist[i][4])*0.20)
        for j in range(1,fine_list[dur]+1):
            print("Month "+str(j)+": " +str(fine))
            total+=fine
            fine+=fine*0.1
        print("Fine: "+str(total))
        total_fine+=total
        dur+=1
    print("\n"+"="*131+"\n")
    print("Total Amount: "+str(total_amt))
    print("Total Fine: "+str(total_fine))
    print("Grand Total: "+str(total_amt)+" + "+str(total_fine)+" = "+str(total_amt+total_fine))
    print("\n"+"="*131+"\n")
    print("Note: The initial fine is calculated as 20% of the monthly rent. It is compounded monthly at a rate of 10%.")

def check_fine(ini,fin):
    if(ini<fin):
        return fin-ini
    else:
        return 0


    
    








