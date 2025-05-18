"""-----------------------------------------------------------------------------
                          Assignment6_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept a number from user checks if it's prime or not
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# This function checks if number is prime or not
#-------------------------------------------------------------------------------
def checkPrime(num):
    if num <= 1:
        return False
    for cnt in range(2,num):
        if num % cnt == 0:
            return False
    return True        
#-------------------------------------------------------------------------------
# Calls checkPrime(number)
#-------------------------------------------------------------------------------
def main():
    number=int(input("Enter the number to check for prime :"))
    print("------------------------------------------------------")
    isPrime=checkPrime(number)
    if (isPrime):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
    print("------------------------------------------------------")
    
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------