"""-----------------------------------------------------------------------------------------
                            Assignment1_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program accepts number from user and 
            checks if given number is positive or negative   
Learnings: 
        --->Returning result as a "str"
        --->if...elif...else
Function Used: 
Built-in-functions:-->input(),
                   -->int(input()) 
                   -->print()
User defined function : PositiveNegativeZero(num):
                      : Input : Integer number
                      : Output : Prints on console if given number is Positive/ Negative/0        
------------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------
# Function used :
# This function accepts "num" as a parameter and 
# checks if "num" is Positive or Negative or zero
#-------------------------------------------------------------------

def PositiveNegativeZero(num):
    result = ""
    if num  > 0 :
        result = "Positive Number"
    elif num < 0:
        result = "Negative Number"
    else:
        result = "Zero"
    return result  
#-------------------------------------------------------------------

#-------------------------------------------------------------------
# This function accepts a number  from user and 
# calls PostiveNegative(num) function
#-------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter the number : ",end="")
    number = int(input())          # Accept input and conversion to int
    ans = PositiveNegativeZero(number)
    print("-------------------------------------------------")
    print("Input : ",number)
    print(f"Output : {number}  is ",ans)
    print("-------------------------------------------------")
#--------------------------------------------------------------------  

#------------------------------------------------------------------  
# Entry point of program
if __name__=="__main__":
    main()
#----------------------------------------------------------------    