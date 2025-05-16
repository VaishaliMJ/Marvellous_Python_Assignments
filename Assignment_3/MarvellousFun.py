"""-------------------------------------------------------------------------------------------
                          Assignment3_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------
This file is module and contains function ChkPrime(number),acceptElements() 
a function to accept all the elements of the list
-----------------------------------------------------------------------------------------"""
#----------------------------------------------------------------------------------
#  This function checks if the given number is prime or not
#----------------------------------------------------------------------------------
def ChkPrime(number):
    isPrime = True   
    for num in range(2,number):
         if (number % num == 0) :
                isPrime = False
                break
    return isPrime  
#----------------------------------------------------------------------------------
 #-------------------------------------------------------------------------------------------
# This Function accepts the number to be added in the list
#------------------------------------------------------------------------------------------
def acceptElements(noOfElements):
    inputNumberList =[]
    print(f"Enter the {noOfElements} number to be added in the list:")
    for count in range(noOfElements):
        number = int(input(f"Element({count+1}) : "))
        inputNumberList.append(number)
    print("Input Elements List is:",inputNumberList)  
    return inputNumberList 
#------------------------------------------------------------------------------------------
