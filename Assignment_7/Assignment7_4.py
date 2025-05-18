"""-----------------------------------------------------------------------------
                          Assignment7_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept list of intgers from user and use reduce() function to 
                   find product of all numbers
----------------------------------------------------------------------------------------"""
from functools import reduce
#-------------------------------------------------------------------------------
# lambda function for even number
#-------------------------------------------------------------------------------
productOfNums = lambda num1,num2: (num1 * num2)
#-------------------------------------------------------------------------------
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
# Calls acceptNumbers() and calculates its product using reduce() function
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputElementList=acceptElements()
    productOfNumbers=int(reduce(productOfNums,inputElementList))
    print(f"\nProduct of all numbers is :",productOfNumbers)
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------