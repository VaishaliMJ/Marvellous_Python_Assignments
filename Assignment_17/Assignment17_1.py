"""-----------------------------------------------------------------------------------------------------
                          Assignment17_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python Script that prints "Jay Ganesh..."Every 2 seconds
                   Use schedule.every(20).seconds.do(....) function
---------------------------------------------------------------------------------------------------------"""     
import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def printEverySecondFunction():
    print("Current time is:",datetime.datetime.now())
    print("Jay Ganesh....")
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Inside Printing Automation Script")
        print(Border)

        print("Current time is:",datetime.datetime.now())

        schedule.every(2).seconds.do(printEverySecondFunction)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except Exception as errObj:
        print("\nException in main():",errObj)        
#---------------------------------------------------------------------------------------------------------
# Entry point of prog
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------    