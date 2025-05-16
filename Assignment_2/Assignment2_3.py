"""-------------------------------------------------------------------------------------------
                          Assignment2_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and displays
                    factorial of given number
------------------------------------------------------------------------------------------"""
from Arithmatic import Mult
#----------------------------------------------------------------------------------------
# This function calculates factorial of given number
#---------------------------------------------------------------------------------------

def calculate_factorial(number):
    result = 1
    for num in range(2,number+1):
        result = Mult(result,num)
    return result
#------------------------------------------------------------------------------------------
# This function accepts a input number from user and calls factorial function
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number to calculate factorial:"))
    result=calculate_factorial(number)
    print(f"Factorial of {number} is :",result)
    
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
