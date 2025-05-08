"""--------------------------------------------------------------------------------------
                            Assignment1_3 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
----------------------------------------------------------------------------------------
Problem statement :
                This program accepts two numbers from user and pass these numbers as 
                parameters to the function named Add(num1 , num2) and returns result 
                of addition 

Learnings :
            ----> How to accepts input from user 
                  i.e. built-in input() function in Python 
            ----> Input conversion from str--->int     
            ----> How to use Function with two parameters 
                  and return value as result                                      
------------------------------------------------------------------------------------------
Functions Used :
Built-In function : input(),int(input())
User defined Function: 
Add(num1,num2) : 
               : Input -->Two parameters as num1, num2
               : Functionality - > Adds num1 and num2
               : Output--> Returns result of addition
-----------------------------------------------------------------------------------------"""

#------------------------------------------------------------------
# This function accepts two numbers as parameters and 
# returns addition of these numbers
#-------------------------------------------------------------------
def Add(num1,num2):
    result = num1 + num2
    return result
#-------------------------------------------------------------------

#-------------------------------------------------------------------
# This function accepts two numbers no1 and no2  from user and 
# calls Add(no1,no2) function
#-------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter first number : ")
    no1 = int(input())          # Accept input and conversion to int
    print("Enter second number : ")
    no2 = int(input())          # Accept input and conversion to int
    ans = Add(no1,no2)          # Return value 
    print("-------------------------------------------------")
    print(f"Addition of {no1} and {no2} is :",ans)
    print("-------------------------------------------------")
#----------------------------------------------------------------  


#------------------------------------------------------------------  
# Entry point of program
if __name__=="__main__":
    main()
#----------------------------------------------------------------    