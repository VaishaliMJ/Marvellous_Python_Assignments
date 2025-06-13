"""-----------------------------------------------------------------------------------------------------
                          Assignment17_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Write a python script that prints current time in file Marvellous.txt
                   Use schedule.every(20).seconds.do(....) function
---------------------------------------------------------------------------------------------------------"""     
import schedule
import time,os
import datetime
from Assignment17_Module import checkIfFileExists
Border="-"*58
fileName="Marvellous.txt"
#---------------------------------------------------------------------------------------------------------
#Schedular function for printing message
#---------------------------------------------------------------------------------------------------------
def printCurrentTimeInFile():    
    try:
        fileObj=open(fileName,"a")
        currDateTime=datetime.datetime.now()
        currFileTime=currDateTime.strftime("%I:%M:%S %p")
        fileObj.write(f"\nTime:"+currFileTime)
        
        fileObj.close()
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in printCurrentTimeInFile():",errObj)  
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        print(Border)
        print("Every 5 mint Time Updater script")
        print(Border)

        print("Current time is:",datetime.datetime.now())
        isExists,currDirect=checkIfFileExists(fileName)
        if(not(isExists)):
            fileObj=open(fileName,"w")
        #   Border="-"*54
            fileObj.write(Border)
            fileObj.write("\nThis is a file For printing time after every 5 minutes...\n")
            fileObj.write("\nThis is Time Logger Script....\n")
            fileObj.write(Border)
            fileObj.write("\n")
            currDateTime=datetime.datetime.now()
            currFileTime=currDateTime.strftime("%I:%M:%S %p")
            fileObj.write(f"\nTime:"+currFileTime)
            fileObj.close()

        schedule.every(5).minutes.do(printCurrentTimeInFile)
        while(True):
            schedule.run_pending()
            time.sleep(1)
        
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in main():",errObj)  
#---------------------------------------------------------------------------------------------------------
# Entry point of prog
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------    