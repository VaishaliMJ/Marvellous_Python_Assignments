"""
-----------------------------------------------------------------------------------------
                            Assignment1_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
    This program accepts number from user and prints * on the console 
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
#------------------------------------------------------------------------------
# This function accepts a number  from user and calls PrintStars(num) function
#-------------------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter the number of stars to display : ",end="")
    number = int(input())          # Accept input and conversion to int
    PrintStars(number)     
#------------------------------------------------------------------  
# Entry point of program
#------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------