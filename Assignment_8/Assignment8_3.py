"""-----------------------------------------------------------------------------
                          Assignment8_3
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
    print(f"\nStarting thread '{nameOfCurrentThread}'...(ThreadId-->{threading.get_ident()})")
    evenNumberList=[]
    sumEvenNums=0
    for num in inputNumberList:
        if(num%2==0):
            #print("Even number in list:",num)
            evenNumberList.append(num)
            sumEvenNums+=num
    print(f"\nEven number list:{evenNumberList}")        
    print(f"\nAddition of all even numbers is :",sumEvenNums)
    print(f"\nExiting '{nameOfCurrentThread}'....")
#---------------------------------------------------------------------------------
# This function calculates sum of odd numbers from input number list
#---------------------------------------------------------------------------
def oddNumberAddition(inputNumberList):
    nameOfCurrentThread=threading.current_thread().name
    print(f"\nEntering '{nameOfCurrentThread}'....(ThreadId-->{threading.get_ident()})")
    oddNumberList=[]
    sumOddNums=0
    for num in inputNumberList:
        if(num%2!=0):
            #print("\nOdd number in list:",num)
            oddNumberList.append(num)
            sumOddNums+=num
    print(f"\nOdd number list:{oddNumberList}")        
    print(f"\nAddition of all Odd numbers is :",sumOddNums)
    print(f"\nExiting '{nameOfCurrentThread}'....")    

#-------------------------------------------------------------------------------
# main() function create and start two threads evenList and oddList
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputNumberList=acceptElements()
    print("------------------------------------------------------")
    if(len(inputNumberList)==0):
        print("\n\nInput list is empty.....")
    else:    
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
