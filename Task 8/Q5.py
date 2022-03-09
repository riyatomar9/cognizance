import numpy as np

#(a) Addition of two numpy arrays
#Creating two arrays namely '"array1" and "array2"
array1=np.array([1,1,1,1,1])
array2=np.array([0,0,0,0,0])
#Now, Adding both the arrays
print(array1+array2)



#(b) Array DataType Conversion

#Creating an array "a" having floating point numbers
a=np.array([12.3,144.09,1.5,33.2])
print(a)

#Changing the datatype of array into int
a=np.array([12.3,144.09,1.5,33.2],dtype='int32')
print(a)








# #Creating an array with 20 Enteries
# arr3=np.arange(1,21)
#
# #Printing that array
# print("Original Array is ",arr3)
#
# #Printing the size of array
# print("Size of original array is ",arr3.size)
#
# #Redimensioning the array and printing it
# print("ReDimensioned Array is: \n",arr3.reshape(10,2))


