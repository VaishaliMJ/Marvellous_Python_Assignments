"""-----------------------------------------------------------------------------------------------------
                          Assignment17_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python Script that prints "Checking Main..."Every 10 seconds
                   Use schedule.every(10).seconds.do(....) function
---------------------------------------------------------------------------------------------------------"""     

import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def checkEmail():
    print("Checking mail....")
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Automation Script for checking mail...")
        print(Border)

        print("Current time is:",datetime.datetime.now())

        schedule.every(10).seconds.do(checkEmail)
        while(True):
            schedule.run_pending()
            time.sleep(1)
        print("End of Automation script......")
    except Exception as errObj:
        print("\Exception in main():",errObj)      

#---------------------------------------------------------------------------------------------------------
# Entry point of prog
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------    