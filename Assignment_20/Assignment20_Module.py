"""-----------------------------------------------------------------------------------------------------
                          Assignment20_Module
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement :This file coniatins all common functions used in Assignment 20
---------------------------------------------------------------------------------------------------------"""
import os,sys,datetime
#-------------------------------------------------------------------------------
# This method creates log directory
#----------------------------------------------------------------
def getLogFolderName():
    try:
        #create dediacted 
        logFolder=os.getcwd()
        logFolder=os.path.join(logFolder,"Marvellous_log")
        if(not(os.path.exists(logFolder))):
            os.mkdir(logFolder)
    except Exception as excObj:
        print("Error while creating log Folder getLogFolderName():",excObj)  
    return logFolder  
#-------------------------------------------------------------------------------
# This method formats date and time
#-------------------------------------------------------------------------------
def getCurrFormattedTime():
    currDateTime=datetime.datetime.now()
    currTime=currDateTime.strftime("%I:%M:%S %p")
    return currTime  
#-------------------------------------------------------------------------------
# This method formats date and time
#-------------------------------------------------------------------------------
def formatTime():
    currTime=getCurrFormattedTime()
    currTime=currTime.replace(":","_")
    currTime=currTime.replace(" ","_")
    return currTime
#-------------------------------------------------------------------------------
# This method formats time
#-------------------------------------------------------------------------------
def formatDate():
    currDateTime=datetime.datetime.now()
    currDate=currDateTime.strftime("%d-%b-%Y")
    return currDate
#-------------------------------------------------------------------------------
# This method generates log file name 
#-------------------------------------------------------------------------------
def generateLogFileName(progFileName):
      try:
            currTime=formatTime()
            fileName=progFileName.split(".")
            logFileName=f"{fileName[0]}_Log_{currTime}.txt"
      except Exception as Err:
            print(f"Exception occured in generateLogFileName().:",Err) 
      return logFileName         
#-------------------------------------------------------------------------------
# This function validates the directory
#-------------------------------------------------------------------------------
def validateDirectory(directoryName,logFileObj):
      # Return whether a path is absolute
      flag=os.path.isabs(directoryName)
      if(flag==False):
        #get absolute directory path
        directoryName=os.path.abspath(directoryName)
      #Check if directory path exists
      flag=os.path.exists(directoryName)
      if(flag==False):
          logFileObj.write(f"Invalid directory path :'{directoryName}' ")
          sys.exit() 
      #Check if given name is directory  
      flag=os.path.isdir(directoryName)
      if(flag==False):
        logFileObj.write(f"Input name '{directoryName}' is not name of directory.")
        sys.exit()  
      return directoryName     
#-------------------------------------------------------------------
#Invalid command line arguments message
#-------------------------------------------------------------------
def invalidArgsMsg():
    print("Invalid number of command line arguments....")
    print("use the given flags as :")
    print("--h : Used to display the help")
    print("--u : Used to display the usage")    
#-------------------------------------------------------------------
#This function checks if file exists in the current directory
#-------------------------------------------------------------------
def checkIfFileExists(FileName,logFileObj):
    try:
        #Gets current working directory path
        currentWorkingDirectory=os.getcwd()
        #Find the file path
        fileExists= os.path.exists(FileName)
    except Exception as exeObj:
       logFileObj.write("\nException in method checkFileIfFileExists()",exeObj)   
    return fileExists,currentWorkingDirectory

#-------------------------------------------------------------------
# This function opens the given file and reads its contents
#-------------------------------------------------------------------
def checkIfFileNotEmpty(fileName,logFileObj):
    try:
        #Finding absolute file path
        absfileName=os.path.abspath(fileName)
        #Check the size of the file
        fileSize=os.path.getsize(absfileName)
        #File empty message
        if(fileSize==0):
            logFileObj.write(f"File Name :'{fileName}'\nFile size is :0 bytes.")
            return True
        else:
            logFileObj.write(f"File Name :'{fileName}'\nFile size is :{fileSize} bytes.")
            return False
    except Exception as exeObj:
        logFileObj.write("\nExecption in checkIfFileNotEmpty() method.",exeObj)
    
#-------------------------------------------------------------------

