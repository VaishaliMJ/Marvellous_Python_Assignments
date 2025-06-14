"""-----------------------------------------------------------------------------------------------------
                          Assignment17_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 1.Write a python script that backup a file after every 1 hour
                   2.writes a log entry in backup_log.txt
---------------------------------------------------------------------------------------------------------"""     

import schedule
import time,os,sys
import datetime
from Assignment17_Module import invalidArgsMsg,checkIfFileExists
Border="-"*58
#------------------------------------------------------------------
#BackUp process
#-----------------------------------------------------------------
def generateBackupFolder(backupFileName):
    folderSuffix=backupFileName.split(".")
    backupDirectoryName=f"BACKUP_{folderSuffix[0]}_{folderSuffix[1]}"
    print(backupDirectoryName)
    #print(os.path.abspath(backupDirectoryName))
    if(not(os.path.exists(backupDirectoryName))):
        # Create the directory
        os.mkdir(backupDirectoryName)
        print(f"'{backupFileName}' backup folder  {backupDirectoryName}' created successfully.")
    else:
        print(f"'{backupFileName}' backup folder  {backupDirectoryName}' already Exists.")
    return backupDirectoryName  
#------------------------------------------------------------------
# Creates log file named "backup_log.txt"
# -----------------------------------------------------------------  
def createLogFile(backupDirectoryName,logFileName):
    try: 
        print("\n In createLogFile")
        backUpDirPath=os.path.abspath(backupDirectoryName)
        logFilePath=os.path.join(backUpDirPath,logFileName)
        isFileExists,currDirectory=checkIfFileExists(logFilePath)
        print(isFileExists)
        if(not(isFileExists)):
            print(logFilePath)
            logFileObj=open(logFilePath,'w')
            logFileObj.write(Border+"\n")
            logFileObj.write("Logging Backup File details\n")
            logFileObj.write(Border+"\n")
            logFileObj.close()
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in main():",errObj)  
    return logFilePath
#------------------------------------------------------------------
#BackUp process
#------------------------------------------------------------------
def createBackUpMainFolder(backupFileName,logFileName):
    try:
        #Check if file exsist
        isFileExists,currDirectory=checkIfFileExists(backupFileName)
        if(isFileExists):
            #Create backupFolder
            backupDirectoryName=generateBackupFolder(backupFileName)
            #Creating log file 
            logFilePath=createLogFile(backupDirectoryName,logFileName)
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in createBackUpMainFolder():",errObj)          
    return backupDirectoryName,logFilePath

#---------------------------------------------------------------------------------------
# Sub directory name
#---------------------------------------------------------------------------------------
def getSubDirectoryName(backupDirectoryName):
    try:
        print(backupDirectoryName)

        #backupDirectoryName=os.path.abspath(backupDirectoryName)
        currDateTime=datetime.datetime.now()

        #currFileTime=currDateTime.strftime("%I:%M:%S %p")
        todayDate=currDateTime.strftime("%d-%b-%Y")
        #today_FolderName="{backupDirectoryName}+{todayDate}"

        subFolderName=f"{backupDirectoryName}_{todayDate}"
        print(subFolderName)
        subFolderName=subFolderName.replace("-","_")
        print(subFolderName) 
    except Exception as errObj:
        print("Exception in main():",errObj)  
    return subFolderName      
#---------------------------------------------------------------------------------------
# This function daily generates a seperate backup folder in BACKUP_Filename directory
#----------------------------------------------------------------------------------------
def generateBackupFolderDaily(backupDirectoryName):
    try:
        
        subFolderName=getSubDirectoryName(backupDirectoryName)
        dailyBackUpFolderName=os.path.join(backupDirectoryName,subFolderName)
        print(dailyBackUpFolderName)

        if(not(os.path.exists(dailyBackUpFolderName))):
        # Create the directory
            os.mkdir(dailyBackUpFolderName)
            print(f"Daily backup folder  {dailyBackUpFolderName}' created successfully.")
        else:
            print(f"Daily backup folder  {dailyBackUpFolderName}' already Exists.")  
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in generateBackupFolderDaily():",errObj)          
    return dailyBackUpFolderName
#----------------------------------------------------------------------------------------
# This function generates backup File Name
#----------------------------------------------------------------------------------------
def generateBackUpFileName(backupFileName):
    try:
        currDateTime=datetime.datetime.now()
        todayDate=currDateTime.strftime("%d-%b-%Y")
        currTime=currDateTime.strftime("%I:%M:%S %p")
        filePrefix=backupFileName.split(".")
        currTime=currTime.replace(":","_")
        currTime=currTime.replace(" ","_")
        destiFileName=f"{filePrefix[0]}_{currTime}.txt"
    except Exception as errObj:
        print("Exception in generateBackUpFileName():",errObj)      
    return destiFileName
#------------------------------------------------------------------
#Start copying file to destination folder
#------------------------------------------------------------------

def backupSourceFile(backupFileName,backupDirectoryName,logFileName):
    try:
        print(logFileName)
        subFolderPath=generateBackupFolderDaily(backupDirectoryName)
        destiFileName=generateBackUpFileName(backupFileName)

        destiFileName=os.path.join(subFolderPath,destiFileName)
        print("\npath")
        print(subFolderPath)
        print(os.path.abspath(backupFileName))
        
        #print(destiFileName)
        #Reading source file
        sourceFileObj=open(backupFileName,"r")
        sourceData=sourceFileObj.read()
        #print(sourceData)
        sourceFileObj.close()

        #Writing data to destination file
        targetFileObj=open(destiFileName,"w")
        targetFileObj.write(str(sourceData))
        targetFileObj.close()

        #Update log file
        logFileUpdate(logFileName,destiFileName)

    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in backupSourceFile():",errObj)          
#---------------------------------------------------------------
# Update log file
#----------------------------------------------------------------
def logFileUpdate(logFileName,destiFileName):
    try:    
        destActualFileName=os.path.basename(destiFileName)
    # Writing log entry to log file
        logFileObj=open(logFileName,'a')
        logFileObj.write(f"Created Backup file successfully:")
        #logFileObj.write(f"'{destiFileName}' Successfully !!")
        logFileObj.write(f"{destActualFileName}")
        logFileObj.write(f"\nFile Location:{os.path.dirname(destiFileName)}")
        currDateTime=datetime.datetime.now()
        #currFileTime=currDateTime.strftime("%I:%M:%S %p")
        todayDate=currDateTime.strftime("%d-%b-%Y")
        currTime=currDateTime.strftime("%I:%M:%S %p")
        logFileObj.write("\n"+str(todayDate))
        logFileObj.write("\n"+str(currTime))
        #Check the size of the file
        destFileSize=os.path.getsize(destiFileName)
        logFileObj.write("\nFile Size :"+str(destFileSize)+" bytes\n")
        logFileObj.write(Border+"\n")
        logFileObj.close()
    except FileExistsError as fileErr:
        print("File error:",fileErr)
    except FileNotFoundError as errObj:
        print("File not found:",errObj) 
    except Exception as errObj:
        print("Exception in logFileUpdate():",errObj)
#-----------------------------------------------------------------------------
#BackUp process
#----------------------------------------------------------------------------
def startBackupProcess(backupFileName,logFileName):

    backupDirectoryName,logFileNamePath=createBackUpMainFolder(backupFileName,logFileName)
    currDateTime=datetime.datetime.now()
    #currFileTime=currDateTime.strftime("%I:%M:%S %p")
    todayDate=currDateTime.strftime("%d-%b-%Y")
    currTime=currDateTime.strftime("%I:%M:%S %p")
    print(f"\nDate:",todayDate)
    print(f"Time:",currTime)
    schedule.every().day.at("00:01").do(generateBackupFolderDaily,backupDirectoryName)
    schedule.every().hour.at("09:01").do(backupSourceFile,backupFileName,backupDirectoryName,logFileNamePath)
    while(True):
        schedule.run_pending()
        time.sleep(1)

#------------------------------------------------------------------
#Initialise script
#------------------------------------------------------------------
def initScript():
    print(Border)
    print("---------------File Backup Automation--------------")
    print(Border)    #Logic
    print("Automatic File Backup....")
    if(len(sys.argv)==1):
        invalidArgsMsg()
    elif(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to backup of file....")
            print("This is the backup automation script.....")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")  
            print("ScriptName.py backUpFileName LogFileName")  
            print("Please provide valid absolute path....")
        else:
            invalidArgsMsg()       
    elif(len(sys.argv)==3):
        #If valid number of args proceed with backUp file
         #backUpFileProcess(sys.argv[1],sys.argv[2])
         startBackupProcess(sys.argv[1],sys.argv[2])
    else:
        invalidArgsMsg()
    print(Border)
    print("--------Thank You for using our script--------------------")
    print(Border)
    
#---------------------------------------------------------------------------------------------------------
# Main function calls schedular
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        #Init Script  
        initScript()
    except Exception as errObj:
        print("\nException in main():",errObj)      
#---------------------------------------------------------------------------------------------------------
# Entry point of prog
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------    
