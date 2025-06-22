"""-----------------------------------------------------------------------------------------------------
                          Extra Assignment
                          TerminateAndRestartProcess.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement :This file terminates the process.
                   Process Name accepted from user and again restart that process
                   Also accepts time interval to schedule task
---------------------------------------------------------------------------------------------------------"""
import os,sys,datetime,schedule,time
import Assignment_Module as Module

import subprocess

import psutil
Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Terminate given process--------")
        print("\nRefer /Marvellous_log/TerminateAndRestartProcess_log_{timestamp}.txt in current directory for output or error messages...")

        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to terminate the process")
                print("Again restart the same process")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  ProcessName")  
                print("Please provide valid absolute path....")
                print("\nRefer TerminateAndRestartProcess_log_{timestamp}.txt for output or error messages...")
            else:
                Module.invalidArgsMsg()    
        elif(len(sys.argv)==3):
                scheduleProcess()
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#---------------------------------------------------------------------------------------------
#This method schedules timely termination and restart of same process
#---------------------------------------------------------------------------------------------
def scheduleProcess():
    try:
        logFileName=createLogFolderAndFile(sys.argv[0])
        schedule.every(int(sys.argv[2])).minutes.do(terminateProcess,sys.argv[1],logFileName)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except ValueError as valErr:
        print("\nNumber expected...",valErr)
    except Exception as excObj:
        print("\nException in schedule task scheduleDeleteFileTask()")
#---------------------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------------------- 
def terminateProcess(processName,logFileName):
    try:
        
        KillAndRestartProcess(sys.argv[1],logFileName)

    except Exception as excObj:
        print("\nException in schedule task terminateProcess():",excObj)

#---------------------------------------------------------------------------------------------
#  Terminates the process and again restart
#---------------------------------------------------------------------------------------------

def KillAndRestartProcess(processName,logFileName):
    logFileObj=open(logFileName,"a")
    print(f"{processName}")

    for proc in psutil.process_iter(['name']):
        if(proc.info['name']==processName):
            print(f"Terminating Process: {processName}")
            proc.kill()
    #newProcess=f"Open /Application/{processName}.app"  
    time.sleep(1)      
    #os.system(newProcess)
    #ret=subprocess.Popen(["Calculator"])
    #pName=f"open  /System/Applications/Calculator.app/Contents/MacOS/Calculator"
    #os.system(pName)
    #newProcess="/bin/sh/"
    #newProcess = psutil.Popen([processName])
    #subprocess.Popen(["/System/Applications/Calculator.app/Contents/MacOS/Calculator"])
    logFileObj.write(f"Terminating the process:{processName}")
    logFileObj.write(f"\nDate :{Module.formatDate()}")
    logFileObj.write(f"\nTime :{Module.getCurrFormattedTime()}")
    logFileObj.write("\n\n")

    newProcess=f"open -a {processName}"
    os.system(newProcess)

    logFileObj.write(f"Restarting the process:{processName}")
    logFileObj.write(f"\nDate :{Module.formatDate()}")
    logFileObj.write(f"\nTime :{Module.getCurrFormattedTime()}")
    logFileObj.write("\n\n")
    logFileObj.close()
    #print(newProcess)       
    


#-------------------------------------------------------------------------------    
#This function creates log file
#-------------------------------------------------------------------------------
def createLogFolderAndFile(progName):
    try:
        #Store log folder name in env file
        #logFolderName=os.getenv("LOG_FOLDER")
        logFolderName=Module.getLogFolderName()
        #generate log file name
        logFileName=Module.generateLogFileName(progName)
        logFileName=os.path.join(logFolderName,logFileName)
        #Creates log file for script
        logFileObj=open(logFileName,'w')
        logFileObj.write("\n"+Border)
        logFileObj.write(f"\n\t\tThis is log file of '{progName}' script") 
        logFileObj.write(f"\n\t\tScript to terminate process and restart ") 
        logFileObj.write(f"\n\t\tProcess Name:{sys.argv[1]}")
        logFileObj.write("\n"+Border)
        logFileObj.write(f"\n\t\tDate File Created :{Module.formatDate()}")
        logFileObj.write(f"\n\t\tTime File Created :{Module.getCurrFormattedTime()}\n")
        logFileObj.write(Border+"\n")
        logFileObj.close()
    except FileExistsError as fileErr:
        print(f"{logFileName} does not exists..:{fileErr}")    
    except FileNotFoundError as fileErr:
        print(f"{logFileName} not found..{fileErr}")    
    except Exception as Err:
        print(f"Exception occured in createLogFile().:{Err}")  
    return logFileName           
#-------------------------------------------------------------------------------
def main():
    initScript()
    
#-------------------------------------------------------------------------------
if __name__=="__main__":
    main()