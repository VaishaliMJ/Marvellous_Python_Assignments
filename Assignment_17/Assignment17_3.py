"""-----------------------------------------------------------------------------------------------------
                          Assignment17_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python Script that prints "Do Coding...!!"Every 30 Minutes
                   Use schedule.every(30).minutes.do(....) function
---------------------------------------------------------------------------------------------------------"""     
import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def printEvery30MinsFunction():
    print("Do Coding...!!")
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("'Do Coding...!!' Script")
        print(Border)

        print("Current time is:",datetime.datetime.now())

        schedule.every(30).minutes.do(printEvery30MinsFunction)
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