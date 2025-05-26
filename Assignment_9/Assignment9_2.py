"""-----------------------------------------------------------------------------
                          Assignment9_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program using multiprocessing.Process to square a list 
                    of numbers using multiple processes
-----------------------------------------------------------------------------------------"""
import multiprocessing,os
import Module_Assignment_9 as module
#-------------------------------------------------------------------------------
# This function displays square of a number
#-------------------------------------------------------------------------------
def squareNumbers(inputNumberList):
    sqaureNumberList=[]
    currentProcessName=multiprocessing.current_process().name
    print(f"\nStarting thread '{currentProcessName}'--->'PID:{os.getpid()}'")
    for num in inputNumberList:
        sqaureNumberList.append(num**2)
    print(f"Squared number list of process {currentProcessName} : {sqaureNumberList}")    
    print(f"\nExiting thread '{currentProcessName}'")

#-------------------------------------------------------------------------------
# main() function,create and start a process
#-------------------------------------------------------------------------------
def main():
    print("----------------Program to Find Square of Input Numbers---------------------")
    inputNumberList=module.acceptElements()
    if(len(inputNumberList)==0):
        print("\n\nInput list is empty.....")
    else: 
        print("------------------------------------------------------")

        squareProcess_1= multiprocessing.Process(target=squareNumbers,args=(inputNumberList,))

        squareProcess_1.start()

        squareProcess_1.join()

        print("\nExiting main function")
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------