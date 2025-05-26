"""-----------------------------------------------------------------------------
                          Assignment8_3_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionality
                    1. Accept list elements from user
                    2. Create two threads 'evenList' and 'oddList'
                    3. 'evenList' thread adds all 'even' elements from the list
                    4. 'oddList' thread adds all 'odd' elements from the list
-------------------------------------------------------------------------------------------------"""
import threading
from functools import reduce
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# lambda functions
#--------------------------------------------------------------------------------
evenNums = lambda num : (num%2==0)
oddNums=lambda num : (num%2 != 0)
addNums=lambda X,Y: X+Y
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# This function accepts numbers from user and creates a input number list
#--------------------------------------------------------------------------------
def acceptElements():
    inputNumberList=[]
    try:
        numOfElements=int(input("Enter the total number of elements in the list:"))

        while (numOfElements<=0) :
            print("\n\nPlease enter number greater than 0.....")
            numOfElements=int(input("Enter again number of elements in the list:")) 


        print(f"\nAccepting {numOfElements} numbers from user")
        print("------------------------------------------------------")

        for count in range(numOfElements):
            number=int(input(f"Number({count+1}):"))
            inputNumberList.append(number)
    except ValueError as errObj:
        print("Error while accepting element:",errObj)   
    except Exception as excObj:
        print("Exceptiom occured :",excObj)
    finally:
        print("Input list elements are:",inputNumberList)                
    return inputNumberList    
#---------------------------------------------------------------------------------
# This function calculates sum of even numbers from input number list
#---------------------------------------------------------------------------
def evenNumberAddition(inputNumberList):
    nameOfCurrentThread=threading.current_thread().name
    print(f"\nStarting thread '{nameOfCurrentThread}'....(ThreadId-->{threading.get_ident()})")
    Even_Number_List=[]
    Sum_Even=0
    try: 
        #Filter() function to find EVEN numbers only from input list  
        Even_Number_List=list(filter(evenNums,inputNumberList))

        #reduce() function to find addition of EVEN Numbers
        Sum_Even=reduce(addNums,Even_Number_List)  

        print(f"\nEven number list:{Even_Number_List}")        
        print(f"\nAddition of all even numbers is :",Sum_Even)    
    except TypeError as typErrObj:
        print(f"There are no EVEN numbers in the input list: {Even_Number_List}",typErrObj)   
    except Exception as excObj:
        print("Exceptiom occured :",excObj) 
    finally:
        print(f"\nExiting '{nameOfCurrentThread}'....")
#---------------------------------------------------------------------------------
# This function calculates sum of odd numbers from input number list
#---------------------------------------------------------------------------
def oddNumberAddition(inputNumberList):
    nameOfCurrentThread=threading.current_thread().name
    print(f"\nStarting thread '{nameOfCurrentThread}'....(ThreadId-->{threading.get_ident()})")
    Odd_Number_List=[]
    Sum_Odd=0
    try:
        #Filter() function to find ODD numbers only from input list  
        Odd_Number_List=list(filter(oddNums,inputNumberList))

        #reduce() function to find addition of EVEN Numbers
        Sum_Odd=reduce(addNums,Odd_Number_List) 
    except TypeError as typErrObj:
        print(f"There are no odd numbers in the input list : {Odd_Number_List}",typErrObj)   
    except Exception as excObj:
        print("Exceptiom occured :",excObj)  
    finally:
        print(f"\nOdd number list:{Odd_Number_List}")        
        print(f"\nAddition of all Odd numbers is :",Sum_Odd)

    print(f"\nExiting '{nameOfCurrentThread}'....")

#-------------------------------------------------------------------------------
# main() function create and start two threads evenList and oddList
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputNumberList=acceptElements()
    if(len(inputNumberList)==0):
        print("\n\nInput list is empty.....")
    else:    
        print("------------------------------------------------------")

        evenList=threading.Thread(target=evenNumberAddition,
                                args=(inputNumberList,))
        oddList=threading.Thread(target=oddNumberAddition,
                                args=(inputNumberList,))
        
        evenList.start()
        oddList.start()

        evenList.join()
        oddList.join()
        
        print("\n\nExiting main...")
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------
