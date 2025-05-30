"""-----------------------------------------------------------------------------
                          Assignment11_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to find factorial of a number using recursion
-----------------------------------------------------------------------------------------"""
FACTORIAL=1
#-----------------------------------------------------------------------------------------
#factorial using normal function(Non recursive)
#-----------------------------------------------------------------------------------------
def calculateFactorial(num):
    fact=1
    while (num>=1):
        fact = fact * num
        num = num-1
    return fact  
#-----------------------------------------------------------------------------------------
#Factorial function(recursive)
#-----------------------------------------------------------------------------------------
def RecursiveCalculateFactorial(num):
    global FACTORIAL
    if (num>=1): 
        FACTORIAL = FACTORIAL * num  
        num = num-1 
        RecursiveCalculateFactorial(num)    
#-----------------------------------------------------------------------------------------
# main() function calls calculateFactorial(number)---->Non recursive
#                        RecursiveFactorial(number)---->Recursive
#-----------------------------------------------------------------------------------------
def main():
    try:
        number=int(input("Enter the number to find FACTORIAL:"))
        print("---------------------------------------------------------")
        if(number<=0):
            print(f"Can not process with input '{number}'")
        else: 
            fact=calculateFactorial(number) 
            RecursiveCalculateFactorial(number)
            print(f"\nFactorial of '{number}' using normal function:",fact)
            print(f"\nFactorial of '{number}' using recursive function:",FACTORIAL)
            print("\n")
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