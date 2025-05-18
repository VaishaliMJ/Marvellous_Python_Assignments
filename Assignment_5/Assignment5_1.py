"""-------------------------------------------------------------------------------------------
                          Assignment 5_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts two numeric inputs from the user and performs 
                    artimatic operations on them. 
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------
#This function accepts two input parameters and performs Addition,Subtraction, 
# Multiplication and Division operations on them
#-----------------------------------------------------------------------------------
# Lambda functions
#Addition function 
Addition = lambda num1,num2:num1+num2
#Subtraction function
Subtraction=lambda num1,num2:num1-num2
#Multiplication
Product=lambda num1,num2:num1*num2
#Division
Division=lambda num1,num2:num1/num2
#-----------------------------------------------------------------------------------

def performOperations(num1,num2,choice):
    print("------------------------------------------------------")
    if choice==1:
        print(f"Sum: {num1} + {num2} =",Addition(num1,num2))
    elif choice==2:    
        print(f"Difference: {num1} - {num2} =",Subtraction(num1,num2))
    elif choice==3:    
        print(f"Product: {num1} * {num2} =",Product(num1,num2))
    elif choice==4:    
        if (num2 != 0 ) : 
          print(f"\nDivision: {num1} / {num2} = ",Division(num1,num2))
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
    choice = 0
    while not (choice == 5):
        print(f"\nPerforming following arithmatic operations on {number1} and {number2}:\n" \
        "1. Addition\n" \
        "2. Subtraction\n"\
        "3. Multiplication\n" \
        "4. Division\n"
        "5. Exit")
        choice = int(input("Enter operation number(1/2/3/4/5):"))
        performOperations(number1,number2,choice)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
