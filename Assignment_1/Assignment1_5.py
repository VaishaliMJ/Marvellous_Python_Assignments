"""------------------------------------------------------------------------------
                            Assignment1_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------
Problem statement :
            This program outputs number 10 to 1    
Learnings:
          ---> Use of "for loop" with range() in python
          ---> Decrementing counter
          ---> Printing output on same line end=" "
Special Variable used : end=" "          
Control statment used:
                   ---> for _______ in range(___,____,___) 

------------------------------------------------------------------------------"""
#----------------------------------------------------------------------
#  This function prints numbers in decreasing order
#----------------------------------------------------------------------
def PrintNoDecreasingOrder(num):
    print("----------------------------------------------")
    print("Decreasing order numbers from 10 to 1  : ")
    for no in range(num,0,-1):
        print(no,end=" ")  
    
    print("\n-------------------------------------------")
#-------------------------------------------------------------------
# This function accepts a number and 
# calls PrintNoDecreasingOrder(num) function
#----------------------------------------------------------------------
def main():
    number = 10
    PrintNoDecreasingOrder(number)
#------------------------------------------------------------------

#------------------------------------------------------------------  
# Entry point of program
if __name__=="__main__":
    main()
#----------------------------------------------------------------   