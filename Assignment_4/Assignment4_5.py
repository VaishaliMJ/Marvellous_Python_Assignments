"""-------------------------------------------------------------------------------------------
                Assignment4_5(Inbuilt Filter,Map and Reduce functions)
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program implements Filter,Map and reduce functionality
                   Input : List of numbers acepted from user 
                   Filter : Number list contains only Prime number
                   Map : Multiply each number by 2
                   Reduce : Maximum of all numbers from the list
------------------------------------------------------------------------------------------"""
from MarvellousFunctions import acceptElements
from functools import reduce
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
#------------------------------------------------------------------------------------------
# This function accepts the numbers from the user and applies 
# filter(),Map() and reduce() functionality
#------------------------------------------------------------------------------------------
def main():
    numberList = acceptElements()
    print("---------------------------------------------------------------")
    primeNumberList=list(filter(ChkPrime,numberList))     
    print("\nFiltered (Prime number) list:",primeNumberList)
    multipliedumbersList=list(map(lambda num : (num*2),primeNumberList))
    print("\nMapped data (Multiply by 2):",multipliedumbersList)
    maximumNumber = reduce((lambda A,B : A if A > B else B),multipliedumbersList)
    print("\nReduced data (Maximum number) :",maximumNumber)
    print("---------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
