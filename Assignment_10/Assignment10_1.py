"""-----------------------------------------------------------------------------
                          Assignment10_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program which accept a paramter and return power of 2
                    using lambda function 
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------------
#Lambda function
#-----------------------------------------------------------------------------------------
powerOfTwo=lambda num : num ** 2
#-----------------------------------------------------------------------------------------
# This function accepts one number and calls lambda function for square
#-----------------------------------------------------------------------------------------
def main():
    try:
        number=int(input("Enter the number to find square:"))
        print(f"\n\nSquare of {number} is :{powerOfTwo(number)}")
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj)    
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()