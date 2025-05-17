"""-------------------------------------------------------------------------------------------
                Assignment4_3(Inbuilt Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Numbers should be 70 < = Number list <= 90 
                   Map : Increase numbers in list by 10
                   Reduce : Product of all numbers from the list
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
    numbersInRangeList=list(filter((lambda num : 70 <= num <= 90),numberList))     
    print("\nFiltered list of number with criteria (70<=number<=90):",numbersInRangeList)
    increaseByTenList=list(map(lambda no : (no+10),numbersInRangeList))
    print("\nMapped data(Increased by 10):",increaseByTenList)
    productOfNumbers = reduce((lambda A,B: A*B), increaseByTenList)
    print("\nReduced data(Multiplication of list numbers) :",productOfNumbers)
    print("---------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
