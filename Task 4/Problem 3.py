# i)
row1=['Roll Number','Name','Marks']
l=[row1]
#Getting the No. of enteries the user want
en=int(input("Enter the Number of records:- "))
for x in range(en):
    print('Enter the following details: ','Record no:-',x+1)
    row2 = [input('Enter Roll number:- '),input('Enter Name:- '),input('Enter Marks:- ')]
    row3 =row2
    #Adding the following details in the existing record
    l.append(row3)
print()
for x in l:
    print(x[0]+'    '+x[1]+'    '+x[2])


# ii)
#Now here, We are checking record 2 is present or not.
if len(l)<3:
    print("Record 2 not found")
else:
    print("Record 2")
    print(l[2][0]+'  '+l[2][1]+'  '+l[2][2])