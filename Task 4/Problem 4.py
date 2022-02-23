#Reading number from the user
x=input("Enter the number: ")

#Reversing the number entered by the user
y=x[::-1]

if x==y:
    print("True")
elif x!=y:
    print("False")