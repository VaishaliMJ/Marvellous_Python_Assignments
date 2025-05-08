"""
-----------------------------------------------------------------------------------------
                            Assignment1_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-----------------------------------------------------------------------------------------
Problem statement :
            This program accepts "name" from user and displays its length
Learnings: In-build function "len()"
            
User defined Function Used:FindLength(name)
------------------------------------------------------------------------------------------
"""
#-------------------------------------------------------------------
# This function finds the length of the "name" entered by user
#-------------------------------------------------------------------
def FindLength(name):
    name_length = len(name)
    print(f"Length of name '{name} ' is : ",name_length)   
#-----------------------------------------------------------------


#-------------------------------------------------------------------
# This function accepts a "name" from user and 
# calls FindLength(name)
#-------------------------------------------------------------------
def main():
    print("---------------------------------------------------")
    print("Enter the name : ",end="")
    name = input()          # Accept input
    FindLength(name)   
#------------------------------------------------------------------  
# Entry point of program
if __name__=="__main__":
    main()
#-----------------------------------------------------------