"""-----------------------------------------------------------------------------------------
                            Assignment1_9
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program displays first 10 even numbers on the screen
------------------------------------------------------------------------------------------"""
START_COUNT=2
END_COUNT=22
SKIP_COUNT_BY=2
#--------------------------------------------------------------------
# This function displays first 10 even numbers on the screen
#--------------------------------------------------------------------
# Solution 1: Using modulus operator
#------------------------------------------------------------------
def DisplayEvenNumbers_1():  
    print("--------------------------------------------------------------------------") 
    print("SOLUTION 1: Using Modulus Operator .....")
    print("--------------------------------------------------------------------------") 

    for num in range(START_COUNT-1,END_COUNT):
        if (num%2==0):
            if (num != (END_COUNT-2)):
                print(num,end="\t")
            else:
                print(num)
    print("--------------------------------------------------------------------------") 

#-------------------------------------------------------------------------------------
#Solution 2 : Using for loop range function
#------------------------------------------------------------------
def DisplayEvenNumbers_2():  
    print("--------------------------------------------------------------------------")
    print("SOLUTION 2 : Using for loop range function.....")
    print("--------------------------------------------------------------------------") 

    for num in range(START_COUNT,END_COUNT,SKIP_COUNT_BY):
       if (num != (END_COUNT-2)):
                print(num,end="\t")
       else:
                print(num)
    print("--------------------------------------------------------------------------") 

#-------------------------------------------------------------------
# Calls DisplayEvenNumbers_1 and DisplayEvenNumbers_2 function
#-------------------------------------------------------------------
def main():
    DisplayEvenNumbers_1()
    DisplayEvenNumbers_2()
#------------------------------------------------------------------  
# Entry point of program
#------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------