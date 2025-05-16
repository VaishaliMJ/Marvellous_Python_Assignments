"""-------------------------------------------------------------------------------------------
                          Assignment2_9
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement:This program accepts a number from user and displays 
                    number of digits in the given number
------------------------------------------------------------------------------------------"""
from Arithmatic import Div,Add
#----------------------------------------------------------------------------------------
# This function counts number of digits using division by 10 
#---------------------------------------------------------------------------------------

def countNumberOfDigits(number):
    digitCount = 0
    while (number !=0):
        number = int(Div(number,10))
        digitCount=Add(digitCount,1)
    return digitCount   

#-----------------------------------------------------------------------------------------
# This function accepts a input number from user and 
# calls function countNumberOfDigits(number)
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number:"))
    digitCount = countNumberOfDigits(number)
    print("---------------------------------------------------------")
    print(f"Number of digits in {number} are :",digitCount)
    print("---------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#------------------------------------------------------