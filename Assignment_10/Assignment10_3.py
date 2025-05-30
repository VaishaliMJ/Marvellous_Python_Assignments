"""-----------------------------------------------------------------------------
                          Assignment10_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement: This program implements Filter(),Map() and reduce() functionality
                   Input : List of numbers acepted from user 
                   Filter() : Numbers should be 70 < = Number list <= 90 
                   Map()    : Increase numbers in list by 10
                   Reduce() : Product of all numbers from the list
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------------
import Module_Assignment_10 as Module
from functools import reduce
#-----------------------------------------------------------------------------------------
#Lambda functions
#-----------------------------------------------------------------------------------------
isNumInRange=lambda num : 70<=num<=90
increaseBy10=lambda num : num +10
multiply=lambda num1,num2 : num1 * num2
#---------------------------------------------------------------------------------------------
#This function Filter out numbers in range 70 to 90,then INCREASE it by 10 and MULTIPLY all numbers
#----------------------------------------------------------------------------------------------
def processInputElements(inputNumberList):
    numbersInRange70To90List=[]
    increaseNumbersBy10List=[]
    finalProduct=1
    try:
        #Using filter() to select numbers in range 70 to 90
        numbersInRange70To90List=list(filter(isNumInRange,inputNumberList))
        if (len(numbersInRange70To90List)>0):
            print("\nFiltered list of number with criteria (70<=number<=90):",numbersInRange70To90List)

            # Using map() to increase filtered numbers by 10
            increaseNumbersBy10List=list(map(increaseBy10,numbersInRange70To90List))
            print("\nMapped data(Increased by 10):",increaseNumbersBy10List)

            # Using reduce() to multiply all the numbers from map() output
            finalProduct=reduce(multiply,increaseNumbersBy10List)
            print("\nReduced data(Multiplication of list numbers) :",finalProduct)
        else:
            print("---------------------------------------------------------------")

            print(f"\nNo elements found with criteria (70<=number<=90) in list {inputNumberList}..Can not proceed further....")    
            print("---------------------------------------------------------------")

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