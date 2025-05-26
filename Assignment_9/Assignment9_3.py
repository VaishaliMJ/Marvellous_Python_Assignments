"""-----------------------------------------------------------------------------
                          Assignment9_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program which uses multiprocessing.Pool to 
                    compute the factorial of a number
-----------------------------------------------------------------------------------------"""
import multiprocessing,os
import Module_Assignment_9 as module
#-------------------------------------------------------------------------------
# This function calculates factorial of a number
# #-------------------------------------------------------------------------------
def calculateFactorial(number):
    currentProcessName=multiprocessing.current_process().name
    print("Process id is : ",os.getpid())
    factorial = 1
    print(f"\nStarting process pool: '{currentProcessName}'")
    for num in range(2,number+1):
        factorial = factorial*num
    print(f"\nExiting process pool: '{currentProcessName}'")
    return factorial
#-------------------------------------------------------------------------------
# main() function creates a multiprocess pool
#-------------------------------------------------------------------------------
def main():
    try:
        numberFactorialList=[]
        print("----------Program to find FACTORIAL of numbers(Multiprocessing POOL)---------")
        inputElements=module.acceptElements()
        if(len(inputElements)==0):
             print("\n\nInput list is empty.....")
        else: 
            print("------------------------------------------------------")
            print(f"\nInput elements are :{inputElements}")

            userProcess = multiprocessing.Pool()
            numberFactorialList=userProcess.map(calculateFactorial,inputElements)

            userProcess.close()
            userProcess.join()

            print(f"\nInput elements are :{inputElements}")
            print(f"\nFactorial of numbers are:{numberFactorialList}")
            print("\nExiting main function")
    except ValueError as valError:
        print("\nError occured during calculation:",valError)   
    except Exception as excObj:
        print("Exception occured:",excObj)     
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------