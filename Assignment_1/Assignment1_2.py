"""-------------------------------------------------------------------------
                            Assignment1_2                         
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
-------------------------------------------------------------------------
Problem statement :
               - This program checks if number is even or odd
-------------------------------------------------------------------------"""

#-------------------------------------------------------------------------
# This function checks for even or odd number
#-------------------------------------------------------------------------
def ChkNum(number):
    print("-----------------------------------")
    if number % 2 ==0:
        print("Output : ",number," is Even Number")
    else:
        print("Output : ",number," is Odd Number")
#-------------------------------------------------------------------------   
# This function calls ChkNum(num) function with one parameter
#-------------------------------------------------------------------------
def main():
    print("Enter the number:")
    num= int(input())
    ChkNum(num)
#-------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-------------------------------------------------------------------------    