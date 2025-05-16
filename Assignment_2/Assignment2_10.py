"""-------------------------------------------------------------------------------------------
                          Assignment2_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement:This program accepts a number from user and displays 
                     the addition of digits in the given number
------------------------------------------------------------------------------------------"""
from Arithmatic import Div,Add
#----------------------------------------------------------------------------------------
# This function adds the digits of number 
#---------------------------------------------------------------------------------------

def addDigitsInNumber(number):
    sumOfDigits = 0
    while (number !=0):
        digit = number % 10
        sumOfDigits=Add(sumOfDigits,digit)
        number = int(Div(number,10)) 
    return sumOfDigits   

#-----------------------------------------------------------------------------------------
# This function accepts a input number from user and 
# calls function addDigitsInNumber(number)
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number:"))
    digitAddition = addDigitsInNumber(number)
    print("---------------------------------------------------------")
    print(f"Addition of digits in {number} are :",digitAddition)
    print("---------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#------------------------------------------------------