"""-----------------------------------------------------------------------------------------------------
                          Assignment17_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python task that prints 
                    "Lunch time !...." At 1 PM
                    "Wrap Up Work..." At 6 PM
---------------------------------------------------------------------------------------------------------"""     

import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def eveyDay6PMTask():
    currDateTime=datetime.datetime.now()
    #currFileTime=currDateTime.strftime("%I:%M:%S %p")

    print(f"\nDate:",currDateTime.strftime("%d-%b-%Y"),end="  ")
    print(f"Time:",currDateTime.strftime("%I:%M:%S %p"),end="  ")

    print(f" Wrap Up Work...")

#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def eveyDay1PMTask():
    currDateTime=datetime.datetime.now()
    #currFileTime=currDateTime.strftime("%I:%M:%S %p")

    print(f"\nDate:",currDateTime.strftime("%d-%b-%Y"),end="  ")
    print(f"Time:",currDateTime.strftime("%I:%M:%S %p"),end="  ")

    print("Lunch Time!....")    
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Every day Task Updater Script")
        print(Border)

        print("Current time is:",datetime.datetime.now())
        schedule.every().day.at("13:00").do(eveyDay1PMTask)
        schedule.every().day.at("18:00").do(eveyDay6PMTask)
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