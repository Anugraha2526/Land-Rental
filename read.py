'''to read file and store it in list'''
def read():
    newlist=[]
    with open("Data.txt","r") as file:
        for line in file:
            line=line.replace("\n","")
            newlist.append(line.split(','))
    return newlist