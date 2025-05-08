"""
----------------------------------------------------------------------------------------
                          Assignment1_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------
Problem statement :
        This program  outputs string "Hello from Fun" on console.
Learnings:
         --->How to define and use user defined function in Python
         --->Use of Built-In "print()" function and __name__ variable             
----------------------------------------------------------------------------------------
Built-In-Functions and variables:
    :print()
    :__name__ usuage

User defined function:
Fun() : Input -->nothing 
      : Output--> prints "Hello from Fun" on console
-------------------------------------------------------------------------    
"""
#-------------------------------------------------------------------------------
# This function displays "Hello from Fun" on the console
def Fun():
    print("Hello from Fun")
#-------------------------------------------------------------------------------
# Calls Fun()
def main():
    Fun()
#-------------------------------------------------------------------------------

# Entry point of program
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------