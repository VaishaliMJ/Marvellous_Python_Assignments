"""----------------------------------------------------------------------------------------
                          Assignment8_5
                    (Student name - Vaishali Jorwekar)
                   Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionality
                    1.Creates two threads named thread1 and thread2
                    2.Thread1 display numbers from 1 to 50
                    3.Thread2 display numbers from 50 to 1
                    4.Schedule Thread2 after completion of Thread1
-------------------------------------------------------------------------------------------------"""
import threading
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# This function displays the numbers in increasing and decreasing order
#-------------------------------------------------------------------------------
def displayNumbersInOrder(StartCount,EndCount,StepCount):
     curreThread=threading.current_thread().name
     print("--------------------------------------------------------------------")
     print(f"\n-----Printing Numbers in '{curreThread}' from {StartCount}----------- ")
     print(f"\nStarting thread --->{curreThread}")
     print("--------------------------------------------------------------------")
     for count in range(StartCount,EndCount,StepCount):
          if (count%10==0):
            if (curreThread=="Increasing_Order"):
                 print(count,end="\n\n")
            elif (curreThread=="Decreasing_Order"):     
                 print("\n\n",count,end=" ")
          else:
              print(count,end=" ")   
     print(f"\n\nExiting thread --->{curreThread}")
     print("--------------------------------------------------------------------")

#-------------------------------------------------------------------------------
#This is main() function,creates and calls two threads Thread1 and Thread2
#-------------------------------------------------------------------------------
def main():
     start_counter=1
     end_counter=50
     step_count=1
     Thread1=threading.Thread(target=displayNumbersInOrder,
                              args=(start_counter,
                                    end_counter+1,
                                    step_count),
                              name="Increasing_Order")
     
     Thread2=threading.Thread(target=displayNumbersInOrder,
                              args=(end_counter,
                                    start_counter-1,
                                    -step_count),
                              name="Decreasing_Order")
     Thread1.start()
     Thread1.join()
     print("Thread Increasing_Order is alive...",Thread1.is_alive())
     #Check if Thread1 is not alive then only start Thread2
     if (not (Thread1.is_alive())):
        Thread2.start()
        Thread2.join()
     
     print("\n\nExiting main......")
#-------------------------------------------------------------------------------    
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":
    main()