"""-------------------------------------------------------------------------------------------
                Assignment4_4_1(User defined Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Number list should be even only
                   Map : Calculate the square of number from list
                   Reduce : Addition of all numbers from the list
----------------------------------------------------------------------------------------------------------"""
from MarvellousFunctions import acceptElements,CustomFilterFunction,CustomMapFunction,CustomReduceFunction
#----------------------------------------------------------------------------------------------------------
# Lambda functions
#----------------------------------------------------------------------------------------------------------
chkEven = lambda num : (num%2==0)
squareNumber = lambda num  : (num**2)
addNumbers = lambda num1,num2 : (num1+num2)
#------------------------------------------------------------------------------------------
# This function accepts the numbers from the user and applies 
# filter,Map and reduce functionality
#------------------------------------------------------------------------------------------
def main():
    numberList = acceptElements()
    print("-----------Custom Filter(),Map() and Reduce() functions---------------------")
    evenNumbersList=CustomFilterFunction(chkEven,numberList) 
    print("\nFiltered function (Even number only) list:",evenNumbersList)
    squareNumbersList=CustomMapFunction(squareNumber,evenNumbersList)
    print("\nMapped function data (Sqaure of a number) list:",squareNumbersList)
    additionNumbers = CustomReduceFunction(addNumbers,squareNumbersList,Result=0)
    print("\nReduced data (Addition of all numbers) :",additionNumbers)
    print("------------------------------------------------------------------------")

#-----------------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
