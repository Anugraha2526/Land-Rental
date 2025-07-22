from operations import *;
def change_data(newlist,i):
    with open("Data.txt","w") as file:
        newlist[i][-1]=" Not Available"
        for line in range(len(newlist)):  
            for item in range(len(newlist[line])):  
                if(item==0):
                    file.write(newlist[line][item])
                else:
                    file.write(","+newlist[line][item])
            file.write("\n")

def bill(i,newlist,name,duration,count,unique,date):
    if(count==0):
        with open("Rent_"+name+"_"+unique+".txt","w") as file:
            file.write("\t\t\t\t\t\t\t Techno Property Nepal\n")
            file.write("\t\t\t\t\t\t\tKamalpokhari, Kathmandu\n")
            file.write("\t\t\t\t\t\t\t"+"-"*23+"\n\n")
            file.write("Date: "+date+"\n")
            file.write("Bill no.: "+unique+"\n\n")
            file.write("="*131+"\n\n")
            file.write("Name: "+name.upper()+"\n\n")
            file.write("Kitta Number: "+newlist[i][0]+"\n")
            file.write("City/District: "+newlist[i][1]+"\n")
            file.write("Direction of Land: "+newlist[i][2]+"\n")
            file.write("Area of Land (Anna): "+newlist[i][3]+"\n\n")
            file.write("Duration of rent: "+str(duration)+"\n\n")
            file.write("Amount: "+str(int(newlist[i][4])*duration)+"\n")   
    else:
        with open("Rent_"+name+"_"+unique+".txt","a") as file:      #open bill in apend mode for renting multiple land
            file.write("\n"+"="*131+"\n\n")
            file.write("Kitta Number: "+newlist[i][0]+"\n")
            file.write("City/District: "+newlist[i][1]+"\n")
            file.write("Direction of Land: "+newlist[i][2]+"\n")
            file.write("Area of Land (Anna): "+newlist[i][3]+"\n\n")
            file.write("Duration of rent: "+str(duration)+"\n\n")
            file.write("Amount: "+str(int(newlist[i][4])*duration)+"\n")   

'''to calculate total in rent bill'''
def bill_total(newlist,name,rented,unique,duration):
    with open("Rent_"+name+"_"+unique+".txt","a") as file:
        total=0
        file.write("\n"+"="*131+"\n\n")
        file.write("Total Amount:"+" ")   
        count=0
        for i in rented:   
            if(count==0):
                file.write(str(int(newlist[i][4])*duration[count])+" ") 
            else:
                file.write("+"+str(int(newlist[i][4])*duration[count])+" ")
            count+=1
            total+=int(newlist[i][4])
        if(count>1):
            file.write("= "+str(total))

def change_data_return(newlist,i):
    with open("Data.txt","w") as file:
        newlist[i][-1]=" Available"
        for line in range(len(newlist)):  
            for item in range(len(newlist[line])):  
                if(item==0):
                    file.write(newlist[line][item])
                else:
                    file.write(","+newlist[line][item])
            file.write("\n")



def return_note(newlist,return_list,name,ini,fin,unique,date,fine_list):
    with open("Return_"+name+"_"+unique+".txt","w") as file:
        dur=0
        total_amt=0
        file.write("\t\t\t\t\t\t Techno Property Nepal\n")
        file.write("\t\t\t\t\t\tKamalpokhari, Kathmandu\n")
        file.write("\t\t\t\t\t\t"+"-"*23+"\n\n")
        file.write("Date: "+date)
        file.write("\nBill no.: "+unique+"\n\n")
        file.write("="*131+"\n\n")
        file.write("Name: "+name.upper()+"\n")
        for i in return_list:
            file.write("Kitta Number: "+newlist[i][0]+"\n")
            file.write("City/District: "+newlist[i][1]+"\n")
            file.write("Direction of Land: "+newlist[i][2]+"\n")
            file.write("Area of Land (Anna): "+newlist[i][3]+"\n\n")
            file.write("Duration of rent according to contract: "+str(ini[dur])+"\n")
            file.write("Actual duration of rent : "+str(fin[dur])+"\n\n")
            if(fine_list[dur]!=0):
                amount=int(newlist[i][4])*fin[dur]
                file.write("Amount: "+str(newlist[i][4])+" x "+str(fin[dur])+" = "+str(amount))
            else:
                amount=int(newlist[i][4])*ini[dur]
                file.write("Amount: "+str(newlist[i][4])+" x "+str(ini[dur])+" = "+str(amount))
            total_amt+=amount
            file.write("\n\n")
            file.write("="*131+"\n\n")
            dur+=1
        
        if(fine_list[0]!=0):
            file.write("Post contract termination fine:\n")
        total_fine=0
        total=0
        dur=0
        for i in return_list:
            file.write("For Kitta no.: "+ newlist[i][0]+"\n")
            fine=(int(newlist[i][4])*0.20)
            for j in range(1,fine_list[dur]+1):
                file.write("Month "+str(j)+": " +str(fine)+"\n")
                total+=fine
                fine+=fine*0.1
            file.write("Fine: "+str(total)+"\n")
            total_fine+=total
            dur+=1
        file.write("\n"+"="*131+"\n\n")
        file.write("Total Amount: "+str(total_amt)+"\n")
        file.write("Total Fine: "+str(total_fine)+"\n")
        file.write("Grand Total: "+str(total_amt)+" + "+str(total_fine)+" = "+str(total_amt+total_fine))
        file.write("\n\n"+"="*131+"\n\n")
        file.write("Note: The initial fine is calculated as 20% of the monthly rent. It is compounded monthly at a rate of 10%.")
            
    
        
        
