"""-----------------------------------------------------------------------------
                          Assignment11_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program adds natural numbers upto "N" 
-----------------------------------------------------------------------------------------"""
DIGIT_ADDITION=0
#-----------------------------------------------------------------------------------------
# This function adds first N natural numbers--->Non recursive
#-----------------------------------------------------------------------------------------
def addFirstNNumbers(num):
    sum=0
    while (num > 0):
        sum=sum+num
        num=num-1
    return sum    
#-----------------------------------------------------------------------------------------
# This function adds first N natural numbers--->Recursive
#-----------------------------------------------------------------------------------------
def recursiveAddFirstNNumbers(num):
    global DIGIT_ADDITION
    if (num > 0):
        DIGIT_ADDITION=DIGIT_ADDITION+num
        num=num-1
        recursiveAddFirstNNumbers(num)
#-----------------------------------------------------------------------------------------
# main() function calls addFirstNNumbers(number)----Non recursive
#                       recursiveAddFirstNNumbers(number)----->Recursive
#------------------------------------------------------------------------------------
def main():
    try:
        print("Addition program to add first N natural numbers")
        print("---------------------------------------------------------")
        number=int(input("Enter the number :"))
        SumNums=addFirstNNumbers(number)     #non Recursive function
        recursiveAddFirstNNumbers(number)   #recursive function
        print(f"Sum of numbers upto'{number}' using normal function:{SumNums}")
        print(f"Sum of numbers upto '{number}' using Recursive function:{DIGIT_ADDITION}")
        print("---------------------------------------------------------")
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nExceptiom occured :",excObj) 
    

#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()