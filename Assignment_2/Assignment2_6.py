"""-------------------------------------------------------------------------------------------
                          Assignment2_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and displays
                     number of * in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output * * * * *
                            * * * *  
                            * * * 
                            * * 
                            *  
-------------------------------------------------------------------------------------------"""
from Arithmatic import Sub
STAR ="*"
#---------------------------------------------------------------------------------------------
# This function accepts a parameter "number" and prints * in matrix format of number*number
# Used basic for loop
#------------------------------------------------------------------------------------------
def printStars(number):
    print(f"\nPrinting '*' in specific format")
    print("--------------------------------------------------------------------------\n")
    
    for row in range(number):
        for coulmn in range(number):
            print(STAR,end="   ") 
        print()  
        #Substract number by 1  
        number=Sub(number,1)
    print("\n---------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
# This function accepts a input number from users and calls function 
# printStars(number) to print the stars in specific format
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number :"))
    printStars(number)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
