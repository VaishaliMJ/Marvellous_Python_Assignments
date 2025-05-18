"""-------------------------------------------------------------------------------------------
                          Assignment 5_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts Three numeric inputs from the user and
                    finds maximum number from them
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------
# This function finds the maximum of three numbers,used nested if...else statement
#-----------------------------------------------------------------------------------
def findMaximumNumber(num1,num2,num3):
    max = 0
    print("--------------using Nested if..else statement-----------------------")
    if num1 > num2:
        if num1 > num3 :
            max = num1
        elif num1< num3:
            max = num3
    elif num1 < num2:
        if num2 > num3:
            max = num2
        elif num2 < num3:
            max = num3 
    print(f"Max of ({num1},{num2},{num3}):",max)
    print("-------------------------------------------------------------------")
#-----------------------------------------------------------------------------------
def findMaximumNumber1(num1,num2,num3):
    max = num1
    print("-------------------using if statement only------------------------")
    if num2 > max:
        max=num2
    if num3 > max:
        max=num3    
    print(f"Max of ({num1},{num2},{num3}):",max)
    print("-----------------------------------------------------------------")    
#-----------------------------------------------------------------------------------
# This function accepts Three input numbers from users and calls function 
# findMaximumNumber(no1,no2,no3) to find maximum number
#-----------------------------------------------------------------------------------
def main():
    number1=int(input("Enter first number:"))
    number2=int(input("Enter second number:"))
    number3=int(input("Enter Third number:"))
    findMaximumNumber(number1,number2,number3)
    findMaximumNumber1(number1,number2,number3)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
