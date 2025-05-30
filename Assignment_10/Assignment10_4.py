"""-----------------------------------------------------------------------------
                          Assignment10_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement: This program implements Filter(),Map() and reduce() functionality
                   Input : List of numbers acepted from user 
                   Filter() : Number list should be even only
                   Map() : Calculate the square of number from list
                   Reduce() : Addition of all numbers from the list
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------------
import Module_Assignment_10 as Module
from functools import reduce
#-----------------------------------------------------------------------------------------
#Lambda functions
#-----------------------------------------------------------------------------------------
isEvenNumber=lambda num : num%2==0
squareNums=lambda num : (num**2)
addNums=lambda num1,num2 : num1 + num2
#---------------------------------------------------------------------------------------------------------
# This function filter out EVEN numbers from input,Calculate its SQUARE and then ADDS all SQUARED elements
#----------------------------------------------------------------------------------------------------------
def processInputElements(inputNumberList):
    evenNumbersList=[]
    squareNumbersList=[]
    addSquaredNums=0
    try:
        #Using filter() to select numbers which are EVEN only
        evenNumbersList=list(filter(isEvenNumber,inputNumberList))
        if (len(evenNumbersList)>0):
            print("\nFiltered EVEN numbers from the input elements are:",evenNumbersList)

            # Using map() to SQUARE the filtered() elements
            squareNumbersList=list(map(squareNums,evenNumbersList))
            print("\nMapped Elements (SQAURED ELEMENTS):",squareNumbersList)

            # Using reduce() to add all the numbers from map() output/
            addSquaredNums=reduce(addNums,squareNumbersList)
            print("\nReduced data(Addition of SQUARED numbers) :",addSquaredNums)
        else:
            print("----------------------------------------------------------------------------------------")
            print(f"\nNo EVEN elements found in input list {inputNumberList}.....Can not proceed further....") 
            print("----------------------------------------------------------------------------------------")
   
    except ValueError as valError:
        print("\nError occured during calculation:",valError)   
    except Exception as excObj:
        print("Exception occured:",excObj) 
#-----------------------------------------------------------------------------------------
# This function accepts numbers from the user and pass it to ProcessInputElements()
#-----------------------------------------------------------------------------------------
def main():
    inputNumberList=Module.acceptNumberFromUser()
    if(len(inputNumberList)==0):
        print("\n\nInput list is empty.....")
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