"""-----------------------------------------------------------------------------------------------------
                          Assignment17_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python Script that prints current date and time every minute
                   Use datetime module 
---------------------------------------------------------------------------------------------------------"""     
import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing current date and time
#---------------------------------------------------------------------------------------------------------
def displayCurrentDateAndTime():
    currDateTime=datetime.datetime.now()
    print(f"Date:",currDateTime.strftime("%d-%b-%Y"))
    print(f"Time:",currDateTime.strftime("%I:%M:%S %p"))
    print(Border)
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Inside Printing Current date and Time Automation Script")
        print(Border)

        print("Current time is:",datetime.datetime.now())
        print(f"Time:",datetime.datetime.now().strftime("%I:%M:%S %p"))
        schedule.every(1).minute.do(displayCurrentDateAndTime)
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