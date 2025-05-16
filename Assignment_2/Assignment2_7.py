"""-------------------------------------------------------------------------------------------
                          Assignment2_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and displays
                     number in following matrix format of number*number
                     e.g. Input :accepted number 5
                     Output : 1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5
                              1 2 3 4 5  
-------------------------------------------------------------------------------------------"""
#---------------------------------------------------------------------------------------------
# This function accepts a parameter "number" and prints "number" in matrix format
#  of number*number used basic for loop
#------------------------------------------------------------------------------------------
def printNumberMatrix(number):
    print(f"\nPrinting  in {number} * {number} matrix format")
    print("--------------------------------------------------------------------------\n")
    for row in range(1,number+1):
        for column in range(1,number+1):
              print(column,end="   ") 
        print(end="\n")
    print("\n---------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------
# This function accepts a input number from users and calls function 
# printNumberMatrix(number) to print the number in specific format
#------------------------------------------------------------------------------------------

def main():
    number=int(input("Enter number:")) 
    printNumberMatrix(number)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
