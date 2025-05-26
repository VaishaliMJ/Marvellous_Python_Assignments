"""-----------------------------------------------------------------------------
                          Assignment9_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program that compares execution time for 
                    additing 1 to 10 million numbers using normal function,
                    threading and multiprocessing
-----------------------------------------------------------------------------------------"""
import threading,time,multiprocessing,os


START_COUNT=1
END_COUNT=10000000
#-------------------------------------------------------------------------------
#     Normal addition function
#-------------------------------------------------------------------------------
def sumLargeNumbers():
    print(f"Inside sumLargeNumbers-->PID-->{os.getpid()}-->(ThreadId-->{threading.get_ident()})")
    SUM_NUMBERS=0
    for cnt in range(START_COUNT,END_COUNT+1):
        SUM_NUMBERS=SUM_NUMBERS+cnt
    print("Returning sum:",SUM_NUMBERS)    
    return SUM_NUMBERS            
#-----------------------------------------------------------------------------
# 
#-----------------------------------------------------------------------------
def main():
    print("---------Additing 1 to 10 million numbers------------- ")
    print("\n-----------Calculating using Normal function-----------------")
    start_time_normal_function=time.time()
    sumAllNumbers=sumLargeNumbers()
    end_time_normal_function=time.time()
    print("Sum using normal function is :",sumAllNumbers)
    print("------------------------------------------------------")
    
    print("\n-----------Calculating using Threading-----------------")

    start_time_threading=time.time()
    T1 = threading.Thread(target=sumLargeNumbers)
    T1.start()
    print("Thread started:",T1.name)
    T1.join()
    end_time_threading=time.time()
    print("Sum using threading is :",sumAllNumbers)
    print("------------------------------------------------------")

    print("\n-----------Calculating using Multiprocessing-----------------")

    start_time_multiprocessing=time.time()
    P1=multiprocessing.Process(target=sumLargeNumbers)
    P1.start()
    P1.join()
    print("Process started:",P1.name)

    end_time_multiprocessing=time.time()
    print("Sum using multiprocessing is :",sumAllNumbers)
    print("------------------------------------------------------")

    
    print("------------------TIME COMPARISION--------------------------------------")
    print("Execution Time for Normal function:",
          (end_time_normal_function-start_time_normal_function))
    print("\n\nExecution Time for threading:",
          (end_time_threading-start_time_threading))
    print("\n\nExecution Time for multiprocessing:",
          (end_time_multiprocessing-start_time_multiprocessing))

    print("--------------------------------------------------------------------")


#-----------------------------------------------------------------------------
#   Entry point of program
#-----------------------------------------------------------------------------
if __name__=="__main__":
    main()