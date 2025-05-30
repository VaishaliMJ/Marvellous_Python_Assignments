"""-----------------------------------------------------------------------------
                          Assignment11_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to add  all digits in the number using recusrion
-----------------------------------------------------------------------------------------"""
SUM_DIGITS=0
#-----------------------------------------------------------------------------------------
#This function adds digits in the number(Non recursive)
#-----------------------------------------------------------------------------------------
def addDigitsInNumber(num):
    sum=0
    while(num!=0):
        sum=sum+(num%10)     # Find each digit and add
        num=int(num/10)     # Update number using division 
    return sum  
#-----------------------------------------------------------------------------------------
#Add digits in the number function(recursive)
#-----------------------------------------------------------------------------------------
def RecursiveAddDigitsInNumber(num):
     global SUM_DIGITS
     if(num!=0):
         SUM_DIGITS=SUM_DIGITS+(num%10)      #Find each digit and add  
         num=int(num/10)                    # Update number using division 
         RecursiveAddDigitsInNumber(num)  #Recursivel call update number
#-----------------------------------------------------------------------------------------
# main() function calls addDigitsInNumber(number)----Non recursive
#                        RecursiveAddDigitsInNumber(number)----->Recursive
#-----------------------------------------------------------------------------------------
def main():
    try:
        print("\nProgram for addition all digits in the number")
        print("---------------------------------------------------------")
        number=int(input("Enter the multi digit number:"))
        if(number<0):
            print(f"Can not process with input '{number}'")
        else: 
            sumOfDigits=addDigitsInNumber(number)   #Normal function to add digits of number
            RecursiveAddDigitsInNumber(number)      #Recursive function to add digits of number
            print(f"Sum of digits '{number}' using normal function:{sumOfDigits}")
            print(f"Sum of digits '{number}' using Recursive function:{SUM_DIGITS}")
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