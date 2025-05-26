"""-----------------------------------------------------------------------------
                          Assignment8_2_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionality
                   1.Creates two threads 'evenfactor' and 'oddfactor'
                   2.Accepts one integer number from user and pass as a argument to these threads
                   3.'evenfactor' thread will add even factors of the number
                   4.'oddfactor' thread will add odd factors of the number   
                   5.After completion of main thread should display message "exit from main"
----------------------------------------------------------------------------------------------"""
import threading,os
from functools import reduce
#---------------------------------------------------------------------------------
evenNumberFun=lambda num:num%2==0
additionOfTwoNums=lambda num1,num2:num1+num2
oddNumberFun=lambda num:num%2!=0

#---------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
# This function finds the all factors of the number
#---------------------------------------------------------------------------------------
def findFactorsOfNumber(number):
    factors=[]
    for num in range(1,number):
        if (number % num == 0):
            factors.append(num)
    return factors
#---------------------------------------------------------------------------
# This function calculates sum of even factors of input number
#---------------------------------------------------------------------------
def evenFactorsAddition(number):
    try:
        nameCurrentThread=threading.current_thread().name
        print(f"Starting '{nameCurrentThread}' thread--->{os.getpid()}--(ThreadId-->{threading.get_ident()})")
    
        # Find all the factors of the number
        allFactors = findFactorsOfNumber(number)

        # filter() to filter out only even factors   
        evenFactors=list(filter(evenNumberFun,allFactors)) 

         #reduce() to add all even factors 
        additionEvenFactors=reduce(additionOfTwoNums,evenFactors)

        print(f"\nAll factors of {number} are:",allFactors)
        print(f"\nEven factors of {number} are:",evenFactors)
        print(f"\nAddition of even factors of {number} is :",additionEvenFactors)
    except TypeError as TErrorObj:
        print("Number does not have any EVEN factors..",TErrorObj)
    except Exception as excObj:
        print("Exception occured...",excObj)
#---------------------------------------------------------------------------
# This function calculates sum of odd factors of input number
#---------------------------------------------------------------------------
def oddFactorsAddition(number):
    try:
        nameCurrentThread=threading.current_thread().name
        print(f"Starting '{nameCurrentThread}' thread--->{os.getpid()}--(ThreadId-->{threading.get_ident()})")
        # Find all the factors of the number
        allFactors = findFactorsOfNumber(number)

        # filter() to filter out only Odd factors   
        oddFactors=list(filter(oddNumberFun,allFactors)) 

         #reduce() to add all Odd factors 
        additionEvenFactors=reduce(additionOfTwoNums,oddFactors)

        print(f"\nAll factors of {number} are:",allFactors)
        print(f"\nOdd factors of {number} are:",oddFactors)
        print(f"\nAddition of Odd factors of {number} is :",additionEvenFactors)
    except TypeError as TErrorObj:
        print("One of the list is empty:",TErrorObj)
    except Exception as excObj:
        print("Exception occured...",excObj)
#-------------------------------------------------------------------------------
# main() function,create and start two thread evenfactor and oddfactor
#-------------------------------------------------------------------------------
def main():
    try:
        print("------Program to find EVEN and ODD factors of number(Threading)----------")
        number = int(input("Enter the number to find factors:"))
        if (number>1):
            evenfactor=threading.Thread(target=evenFactorsAddition,args=(number,))
            oddfactor=threading.Thread(target=oddFactorsAddition,args=(number,))
            
            evenfactor.start()
            oddfactor.start()

            evenfactor.join()
            oddfactor.join()
        else:
            print(f"\n'{number}' does not have any EVEN or ODD factors")
    
    except ValueError as valObj:
        print("Exception ocuured while accepting input number:",valObj)
    except Exception as excObj:
        print("Exception occured...",excObj)  
    finally: 
        print("\n\nExit from main...")
        print("------------------------------------------------------") 
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------