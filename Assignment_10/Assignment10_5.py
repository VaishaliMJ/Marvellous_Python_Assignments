"""-----------------------------------------------------------------------------
                          Assignment10_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement: This program implements Filter(),Map() and reduce() functionality
                   Input : List of numbers acepted from user 
                   filter() : filter out the elements which are PRIME NUMBER
                   map() : Multiply each PRIME NUMBER LIST number by 2 
                   reduce() : MAXIMUM of all numbers from the mapped data list
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------------
import Module_Assignment_10 as Module
from functools import reduce
#-----------------------------------------------------------------------------------------
#Lambda functions
#-----------------------------------------------------------------------------------------
multiplyBy2=lambda num : (num*2)
maximumNum=lambda num1,num2 : num1 if num1 > num2 else num2
#----------------------------------------------------------------------------------
#  This function checks if the given number is prime or not
#----------------------------------------------------------------------------------
def isPrime(number):
    if number<=1:
        return False
    for num in range(2,number):
         if (number % num == 0) :
                return False
    return True  
#----------------------------------------------------------------------------------------------
#This function filters out PRIME Numbers and DOUBLE them and find MAXXIMUM element from it
#----------------------------------------------------------------------------------------------
def processInputElements(inputNumberList):
    primeNumberList=[]
    doubledNumberList=[]
    maxNumber=0
    try:
        #Using filter() to select numbers which are PRIME only
        primeNumberList=list(filter(isPrime,inputNumberList))
        if (len(primeNumberList)>0):
            print("\nFiltered PRIME numbers from the input elements are:",primeNumberList)

            # Using map() to DOUBLE the filtered() elements
            doubledNumberList=list(map(multiplyBy2,primeNumberList))
            print("\nMapped Elements (DOUBLED ELEMENTS):",doubledNumberList)

            # Using reduce() to find MAXIMUM number from map() output/
            maxNumber=reduce(maximumNum,doubledNumberList)
            print("\nReduced data(MAXIMUM of DOUBLED numbers) :",maxNumber)
        else:
            print("---------------------------------------------------------------")
            print(f"\nNo PRIME elements found in input list {inputNumberList}.....Can not proceed further....") 
            print("---------------------------------------------------------------")
   
    except ValueError as valError:
        print("\nError occured during calculation:",valError)   
    except Exception as excObj:
        print("Exception occured:",excObj) 
#-----------------------------------------------------------------------------------------
def main():
    inputNumberList=Module.acceptNumberFromUser()
    if(len(inputNumberList)==0):
        print("\n\nInput list is empty...Can not proceed further...")
    else:    
        print("---------------------------------------------------------------")
        processInputElements(inputNumberList)
        print("---------------------------------------------------------------")   
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------    