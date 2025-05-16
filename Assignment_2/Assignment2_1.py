"""-------------------------------------------------------------------------------------------
                          Assignment 2_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts two numeric inputs from the user and performs 
                    artimatic operations on them. These arithmaic functions are defined 
                    in a Module Arithmatic.
-----------------------------------------------------------------------------------------"""
from Arithmatic import Add,Sub,Mult,Div
#-----------------------------------------------------------------------------------
#This function accepts two input parameters and performs Addition,Subtraction, 
# Multiplication and Division operations on them
#-----------------------------------------------------------------------------------

def performOperations(number1,number2):
    result = 0
    print("------------------------------------------------------")
    result = Add(number1,number2)
    print(f"Addition Result: {number1} + {number2} =",result)
    result = Sub(number1,number2)
    print(f"\nSubtraction Result: {number1} - {number2} = ",result)
    print
    result = Mult(number1,number2)
    print(f"\nMultiplication Result: {number1} * {number2} = ",result)
    if (number2 != 0 ) : 
        result = Div(number1,number2)
        print(f"\nDivision Result: {number1} / {number2} = ",result)
    else :
        print("\nDivision is not possible")    
    print("------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This function accepts two input numbers from users and calls function 
# performOperations with these two input parameters
#-----------------------------------------------------------------------------------

def main():
    number1=int(input("Enter first number:"))
    
    number2=int(input("Enter second number:"))
    
    print(f"\nPerforming following arithmatic operations on {number1} and {number2}:\n" \
    "1. Addition\n" \
    "2. Subtraction\n"\
    "3. Multiplication\n" \
    "4. Division\n")
    performOperations(number1,number2)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
