"""-----------------------------------------------------------------------------
                          Assignment9_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program which has three threads. 
                    Each thread prints number from 1 to 5 with a delay of second
-----------------------------------------------------------------------------------------"""
import threading,time,os
#-------------------------------------------------------------------------------
# This function displays numbers from 1 to 5 with a delay of 1 sec
#-------------------------------------------------------------------------------
def printNumbers():
    currentThreadName=threading.current_thread().name
    print(f"\nStarting thread '{currentThreadName}'")
    for num in range(6):
        print(f"'{currentThreadName}' --->'ThreadId:{threading.get_ident()}'---> ({num})")
        time.sleep(1)

    print(f"\nExiting thread '{currentThreadName}'")

#-------------------------------------------------------------------------------
# main() function,create and start three threads
#-------------------------------------------------------------------------------
def main():
    print(f"--------------------PID--->{os.getpid()}----------------------------------")
    firstThread = threading.Thread(target=printNumbers)
    secondThread = threading.Thread(target=printNumbers)
    thirdThread = threading.Thread(target=printNumbers)

    firstThread.start()
    time.sleep(1)
    secondThread.start()
    time.sleep(1)
    thirdThread.start()

    firstThread.join()
    secondThread.join()
    thirdThread.join()

    print("\nExiting main function")
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------