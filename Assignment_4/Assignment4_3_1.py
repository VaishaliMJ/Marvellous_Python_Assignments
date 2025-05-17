"""-------------------------------------------------------------------------------------------
                Assignment4_3_1 (Used defined Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Numbers should be 70 < = Number list <= 90 
                   Map : Increase numbers in list by 10
                   Reduce : Product of all numbers from the list
------------------------------------------------------------------------------------------"""
from MarvellousFunctions import acceptElements,CustomFilterFunction,CustomMapFunction,CustomReduceFunction
#-----------------------------------------------------------------------------
# Lambda functions
#----------------------------------------------------------------------------
chkNumberInRange = lambda num : 70 <= num <= 90
increaseNumberBy10= lambda num : num + 10
multiplyNumber = lambda num1,num2 : num1 * num2
#------------------------------------------------------------------------------------------
# This function accepts the numbers from the user and applies 
# filter,Map and reduce functionality
#------------------------------------------------------------------------------------------
def main():
    numberList = acceptElements()
    print("-----------Custom Filter(),Map() and Reduce() functions----------------------")
    numbersInRangeList=CustomFilterFunction(chkNumberInRange,numberList)    
    print("\nFiltered function data with criteria (70<=number<=90)::",numbersInRangeList)
    increaseByTenList=CustomMapFunction(increaseNumberBy10,numbersInRangeList)
    print("\nMapped function data (Increased by 10):",increaseByTenList)
    productOfNumbers = CustomReduceFunction(multiplyNumber, increaseByTenList,Result=1)
    print("\nReduced function data result (Multiplication of list numbers) :",productOfNumbers)
    print("----------------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
