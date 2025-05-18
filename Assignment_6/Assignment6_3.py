"""-----------------------------------------------------------------------------
                          Assignment6_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to print a multiplication table of a user accepted input
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# This function prints the table of given number 
#-------------------------------------------------------------------------------
def printTableOfNumber(num):
    for i in range(1,11):
        print(f"{num} * {i} =",num*i)
#-------------------------------------------------------------------------------
# Calls printTableOfNumber(number)
#-------------------------------------------------------------------------------
def main():
    number=int(input("Enter the number for which you want to print the table:"))
    if number > 0:
        print("------------------------------------------------------")
        print(f"Printing multiplcation table of {number}...")
        print("------------------------------------------------------")
        printTableOfNumber(number)
        print("------------------------------------------------------")

    else:
        print("Please enter number grater than 0")    

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------