"""-----------------------------------------------------------------------------------------
                            Assignment1_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
    This program accepts 'number' from user and checks if given number is divisible by 5   
------------------------------------------------------------------------------------------"""
#------------------------------------------------------------------
# This function checks if input number 'num' is divisible by 5 or not
# If divisible by 5 returns 'True' , else 'False'    
#------------------------------------------------------------------
def isDivisibleByFive(num):
    isDivisible=False 
    if num % 5==0:
        isDivisible = True
    return isDivisible        
#-------------------------------------------------------------------
# This function accepts a number from user and 
# calls isDivisibleByFive(num) function
#-------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter the number : ",end="")
    number = int(input())          # Accept input and conversion to int
    ans = isDivisibleByFive(number)
      
    print("-------------------------------------------------")
    print(f"Output : Number {number} divisible by 5 :",ans)
    print("-------------------------------------------------")
#--------------------------------------------------------------------  
#------------------------------------------------------------------  
# Entry point of program
#------------------------------------------------------------------
if __name__=="__main__":
    main()
#----------------------------------------------------------------    


    