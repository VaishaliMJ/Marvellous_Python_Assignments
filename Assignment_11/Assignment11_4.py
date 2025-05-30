"""-----------------------------------------------------------------------------
                          Assignment11_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to implement "POWER" function using recursion
-----------------------------------------------------------------------------------------"""
POWER_OUTPUT=1
#-----------------------------------------------------------------------------------------
#This function implements 'POWER' functionality in non recursive way
#-----------------------------------------------------------------------------------------
def findPowerOfNumber(num,power):
    answerPower=1
    while(power!=0):
        answerPower=answerPower*num
        power=power-1
    return answerPower 
#-----------------------------------------------------------------------------------------
#Finds the power of a number (recursive)
#-----------------------------------------------------------------------------------------
def recursivePowerFunction(num,power):
     global POWER_OUTPUT
     if(power!=0):
         POWER_OUTPUT=POWER_OUTPUT * num
         power=power-1
         recursivePowerFunction(num,power)
#-----------------------------------------------------------------------------------------
# main() function calls findPowerOfNumber(number)----Non recursive
#                       recursivePowerFunction()----->Recursive
#-----------------------------------------------------------------------------------------
def main():
    try:
        print("\nPower functionality")
        print("---------------------------------------------------------")
        number=int(input("Enter the number:"))
        powerDigit=int(input("Enter the power digit:"))
        if(number>0 and powerDigit >0):
            answerPower=findPowerOfNumber(number,powerDigit)

            recursivePowerFunction(number,powerDigit)
            print(f"power ({number}^{powerDigit}) using normal function:{answerPower}")
            print(f"power ({number}^{powerDigit}) using Recursive function:{POWER_OUTPUT}")
        else:
            print(f"One of the input is '0' can not proceed with POWER calculation....")    
        print("---------------------------------------------------------")
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 

#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()