"""-------------------------------------------------------------------------------------------
                          Assignment2_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and 
                    checks if given number is prime or not
------------------------------------------------------------------------------------------"""
#----------------------------------------------------------------------------------------
# This function checks if given number is prime or not
#---------------------------------------------------------------------------------------

def checkPrime(number):
    isPrime = True   
    for num in range(2,number):
         if (number % num == 0) :
                isPrime = False
                break
    return isPrime      
#------------------------------------------------------------------------------------------
# This function accepts a input number from user and calls checkPrime(number) function
#------------------------------------------------------------------------------------------
def main():
    number=int(input("Enter number :"))

    if number==0 or number==1:
        print(f"\n{number} is not Prime Number")
    else:
        isPrimeNumber = checkPrime(number)
        if isPrimeNumber:
             print(f"\n{number} is Prime Number")
        else:
             print(f"\n{number} is not Prime Number")          
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
