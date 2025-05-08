"""-------------------------------------------------------------------------
                            Assignment1_2                         
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
-------------------------------------------------------------------------
Problem statement :
               - This program has one function with one number parameter
                and checks if number is even or odd
Learnings:
        ---> Passing a parameter to user defined function
        ---> "if---else" block in Python
        ---> Modulous operator and Even or Odd number logic                    
------------------------------------------------------------------------- 
Function used :
ChkNum(number) : Input -->One parameter as number
               : Functionality - > Check if number is even or Odd
               : Output--> if number even --> Even Number
                           else ------------> Odd Number
-------------------------------------------------------------------------"""

#-------------------------------------------------------------------------
# This function checks for even or odd number
def ChkNum(number):
    print("-----------------------------------")
    print("Input : ",number)
    if number % 2 ==0:
        print("Output : ",number," : Even Number")
    else:
        print("Output : ",number," : Odd Number")
#-------------------------------------------------------------------------   
# This function calls ChkNum() function with one parameter
def main():
    ChkNum(11)
    ChkNum(8)

#-------------------------------------------------------------------------
# Entry point of program
if __name__=="__main__":
    main()
#-------------------------------------------------------------------------    