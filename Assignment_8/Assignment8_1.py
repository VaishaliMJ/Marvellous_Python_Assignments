"""-----------------------------------------------------------------------------
                          Assignment8_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement :Write a program to display first 10 even and odd numbers 
                   -Even Thread ----for finding first 10 even numbers
                   -Odd Thread---- for odd finding first 10 odd numbers
----------------------------------------------------------------------------------------"""
import threading,os
#---------------------------------------------------------------------------
# Global (common) variables
#---------------------------------------------------------------------------
START_COUNT=2
END_COUNT=21
SKIP_COUNTER=2
EVEN_NUMBER_LIST=[]
ODD_NUMBER_LIST=[]
#---------------------------------------------------------------------------
# This function displays first 10 even and odd numbers
#---------------------------------------------------------------------------
def displayFirstTenEvenAndOddNumbers(startCnt,endCnt,stepCnt):
    global EVEN_NUMBER_LIST,ODD_NUMBER_LIST

    threadName=threading.current_thread().name
    print(f"'{threadName}' thread started..PID--->{os.getpid()}---(ThreadId-->{threading.get_ident()})")
    for num in range(startCnt,endCnt,stepCnt):
        if threadName=="even":
            EVEN_NUMBER_LIST.append(num)
        else:
            ODD_NUMBER_LIST.append(num)    
    print(f"Exiting '{threadName}' thread....")  

#-------------------------------------------------------------------------------
# main() function,create and start two thread even and odd
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    even=threading.Thread(target=displayFirstTenEvenAndOddNumbers,
                          args=(START_COUNT,END_COUNT,SKIP_COUNTER),
                          name="even")
    odd=threading.Thread(target=displayFirstTenEvenAndOddNumbers,
                         args=(START_COUNT-1,END_COUNT,SKIP_COUNTER),
                         name="odd")

    even.start()
    odd.start()

    even.join()
    odd.join()
    print("------------------------------------------------------")

    print(f"\nFirst 10 even numbers are:",EVEN_NUMBER_LIST)
    print(f"\nFirst 10 odd numbers are:",ODD_NUMBER_LIST)

    print("\nExiting main...")
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------