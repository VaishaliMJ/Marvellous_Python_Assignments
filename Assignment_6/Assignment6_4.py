"""-----------------------------------------------------------------------------
                          Assignment6_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept a number and print its factorial using for loop
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# This function calculates the factorial of given number
#-------------------------------------------------------------------------------
def calculateFactorialOfNumber(number):
    factorial=1
    for num in range(number,0,-1):
        factorial=factorial * num
    print(f"\nFactorial of {number} is :",factorial)         
#-------------------------------------------------------------------------------
# Calls calculateFactorialOfNumber(number)
#-------------------------------------------------------------------------------
def main():
    number=int(input("Enter the number to find factorial:"))
    print("------------------------------------------------------")
    if number > 0:
        calculateFactorialOfNumber(number)
    else:
        print("Please enter number greater than 0")        
    print("------------------------------------------------------")
    
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------