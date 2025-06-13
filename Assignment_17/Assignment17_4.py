"""-----------------------------------------------------------------------------------------------------
                          Assignment17_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python task that prints "Namskar..." at 9AM
                   Use schedule.every(20).seconds.do(....) function
---------------------------------------------------------------------------------------------------------"""     
import schedule
import time
import datetime
Border="-"*58
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def eveyDay9AMTask():
    print("Namskar....")
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Every day 9 AM ->Namskar Print Script")
        print(Border)

        print("Current time is:",datetime.datetime.now())

        schedule.every().day.at("09:00").do(eveyDay9AMTask)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except Exception as errObj:
        print("\Exception in main():",errObj)          
#---------------------------------------------------------------------------------------------------------
# Entry point of prog
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------    