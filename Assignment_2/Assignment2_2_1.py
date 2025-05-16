"""-------------------------------------------------------------------------------------------
                          Assignment 2_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a number from user and displays
                     number of * in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output * * * * *
                            * * * * *  
                            * * * * *
                            * * * * *
                            * * * * *  
-------------------------------------------------------------------------------------------"""
from Arithmatic import Mult
STAR ="*"
#---------------------------------------------------------------------------------------------
# This function accepts a parameter "number" and prints * in matrix format of number*number
# Used only one for loop and multiplication function
#------------------------------------------------------------------------------------------
def printStars(number):
    print(f"\nPrinting '*' in {number} * {number} matrix format")
    print("--------------------------------------------------------------------------\n")
    #Using Mult() function 
    loopCounter = Mult(number,number)
    for row in range(loopCounter):
        if (row % number == 0 and row !=0):
               print()
        print(STAR,end="   ") 
       
    print("\n---------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
# This function accepts a input number from users and calls function 
# printStars(number) to print the stars in specific format
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number:"))
   
    printStars(number)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
