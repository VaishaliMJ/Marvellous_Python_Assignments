"""-----------------------------------------------------------------------------
                          Assignment7_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept list of intgers from user and use filter() function to 
                   find prime numbers from the list
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#  This function checks if the given number is prime or not
#----------------------------------------------------------------------------------
def ChkPrime(number):
    if number<=1:
        return False
    for num in range(2,number):
         if (number % num == 0) :
                return False
    return True 
#-------------------------------------------------------------------------------------------
# This Function accepts the number to be added in the list
#------------------------------------------------------------------------------------------
def acceptElements():
    noOfElements=int(input("Enter the number of elements in the list:"))
    inputNumberList =[]
    print(f"Enter the {noOfElements} number to be added in the list:")
    for count in range(noOfElements):
        number = int(input(f"Element({count+1}) : "))
        inputNumberList.append(number)
    print("\nInput list elements are:",inputNumberList)  
    return inputNumberList 
#------------------------------------------------------------------------------------------
# Calls acceptNumbers() and filter() function filters only Prime numbers from the list
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputElementList=acceptElements()
    primeNumberList=list(filter(ChkPrime,inputElementList))
    print(f"\nPrime numbers list after filter():",primeNumberList)
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------