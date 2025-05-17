"""-------------------------------------------------------------------------------------------
                Assignment4_4(Inbuilt Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Number list should be even only
                   Map : Calculate the square of number from list
                   Reduce : Addition of all numbers from the list
------------------------------------------------------------------------------------------"""
from MarvellousFunctions import acceptElements
from functools import reduce
#------------------------------------------------------------------------------------------
# This function accepts the numbers from the user and applies 
# filter,Map and reduce functionality
#------------------------------------------------------------------------------------------
def main():
    numberList = acceptElements()
    print("---------------------------------------------------------------")
    evenNumbersList=list(filter((lambda num : (num%2==0)),numberList))     
    print("\nFiltered (Even number) list:",evenNumbersList)
    squareNumbersList=list(map(lambda num : (num**2),evenNumbersList))
    print("\nMapped data (Sqaure of a number) list:",squareNumbersList)
    additionNumbers = reduce((lambda A,B: A+B), squareNumbersList)
    print("\nReduced data (Addition of all numbers) :",additionNumbers)
    print("---------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
