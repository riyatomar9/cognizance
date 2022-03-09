import numpy as np

l1=list(input("Please Enter First array: ")) #Requesting input from user
array1=np.array(l1)#Creating array from user input
l2=list(input("Please Enter Second array: "))#Requesting input from user
array2=np.array(l2)#Creating array from user input

#Now we are Checking if the Two arrays have same elements or not.
print(np.array_equal(array1,array2))