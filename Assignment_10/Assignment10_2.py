"""-----------------------------------------------------------------------------
                          Assignment10_2 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program which accept a paramter and return power of 2
                    using lambda function 
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------------
#Lambda function
#-----------------------------------------------------------------------------------------
multiply=lambda num1,num2 : num1 * num2
#-----------------------------------------------------------------------------------------
# This function accepts two numbers and calls multiply lambda function
#-----------------------------------------------------------------------------------------
def main():
    try:
        print("Enter two numbers for multiplication....")
        number1=int(input("Enter the first number :"))
        number2=int(input("Enter the second number :"))

        print(f"\n\nProduct of {number1}*{number2} is :{multiply(number1,number2)}")

    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj)
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------    