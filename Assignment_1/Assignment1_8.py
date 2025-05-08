"""
-----------------------------------------------------------------------------------------
                            Assignment1_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program accepts number from user and prints * on the console 
            in a single line
Learnings:---> Printing special character on console
          ---> for loop logic 
          --->If we use end="\t" then it prints % at the end.
                 To solve this add (if...else condition) 
Built-in function used :input(),
                        end="\t" 
                        CONSTANT
Function Used: PrintStars(num):
                        : Input : Integer number
                        : Output : prints on console number of  * == accepted input(number) 
------------------------------------------------------------------------------------------"""

STAR="*"

#-----------------------------------------------------------------
# This function accepts a parameter int 'num' from user
# and outputs number of * == num value
#-----------------------------------------------------------------
def PrintStars(num):
    for i in range(0,num):
        if i!=(num-1):
            print(STAR,end="\t")
        else: 
            print(STAR)                
#-------------------------------------------------------------------
# This function accepts a number  from user and 
# calls PrintStars(num) function
#-------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter the number : ",end="")
    number = int(input())          # Accept input and conversion to int
    PrintStars(number)     
#------------------------------------------------------------------  
# Entry point of program
if __name__=="__main__":
    main()
#-----------------------------------------------------------