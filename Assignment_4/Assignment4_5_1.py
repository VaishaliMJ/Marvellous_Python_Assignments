"""-------------------------------------------------------------------------------------------
                Assignment4_5_1(Custom user defined Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Number list contains only Prime number
                   Map : Multiply each number by 2
                   Reduce : Maximum of all numbers from the list
------------------------------------------------------------------------------------------"""
from MarvellousFunctions import acceptElements,CustomFilterFunction,CustomMapFunction,CustomReduceFunction
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
#-----------------------------------------------------------------------------------------------
# Lambda functions
#-----------------------------------------------------------------------------------------------
multiplyByTwo = lambda A : A*2
maxNumber = lambda A,B : A if A > B else B
#------------------------------------------------------------------------------------------
# This function accepts the numbers from the user and applies 
# filter,Map and reduce functionality
#------------------------------------------------------------------------------------------
def main():
    numberList = acceptElements()
    print("-----------Custom Filter(),Map() and Reduce() functions-----------------")
    primeNumberList=list(CustomFilterFunction(ChkPrime,numberList))    
    print("\nFiltered function (Prime number) list:",primeNumberList)
    multipliedumbersList=list(CustomMapFunction(multiplyByTwo,primeNumberList))
    print("\nMapped function data (Multiply by 2):",multipliedumbersList)
    maximumNumber = CustomReduceFunction(maxNumber,multipliedumbersList,Result=0)
    print("\nReduced Function data (Maximum number) :",maximumNumber)
    print("---------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
