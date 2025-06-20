"""-----------------------------------------------------------------------------------------------------
                          Assignment21_2
                          ProcInfoRunning.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Design automation script which accepts the process name display information of 
                    process if its running
---------------------------------------------------------------------------------------------------------""" 
import Assignment21_Module as Module
import psutil,sys,os
Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Display information of process if its running--------")
        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This Script shows process information ,if Process is in running state")
                print("Process name accepted from command line")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  processName")  
                print("\nRefer ProcInfoRunning_log_{timestamp}.txt for output or error messages...")
            else:
                  #Creates log file for script
                  logFileName=createLogFile(sys.argv[0])
                  #If valid number of args procced directory search
                  displayCurrentProcesses(sys.argv[1],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)   
#-------------------------------------------------------------------------------
# Displays current processes
#-------------------------------------------------------------------------------
def displayCurrentProcesses(processName,logFileName):
    try:
        #open log file
        logFolderName=Module.getLogFolderName()  
        outputFileName=sys.argv[0].split(".")[0]+".txt"
       
        outputFileName=os.path.join(logFolderName,outputFileName)
        logFileObj=open(logFileName,"a")
        outputobj=open(outputFileName,"w")
        for proc in psutil.process_iter():
            infoProc=proc.as_dict(attrs=['pid','name','username'])
            if(infoProc['name']==processName):
                print(infoProc)  
                #redirect output to a file
                print(infoProc,file=outputobj) 
                logFileObj.write(f"Process '{processName} : {infoProc }'")   
        outputobj.close() 
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass    
    except Exception as Err:
        logFileObj.write(f"Exception occured displayCurrentProcesses().:{Err}")  
    finally:
         logFileObj.close()    
#-------------------------------------------------------------------------------
# This function return the name of the log file for directory search
#-------------------------------------------------------------------------------        
def createLogFile(progName):
      logFileName=""
      try:
            #Generate log folder and files
            logFolder=Module.getLogFolderName()
            #generate log file name
            logFileName=Module.generateLogFileName(progName)
            logFileName=os.path.join(logFolder,logFileName)
            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write("\n"+Border)
            logFileObj.write(f"\n\t\tThis is log file of '{progName}' script") 
            logFileObj.write(f"\n\t\tDisplay currently running processes")
            logFileObj.write("\n"+Border)
            logFileObj.write(f"\n\t\tDate Created :{Module.formatDate()}")
            logFileObj.write(f"\n\t\tTime Created :{Module.getCurrFormattedTime()}\n")
            logFileObj.write(Border+"\n")
            logFileObj.close()
      except FileExistsError as fileErr:
            print(f"{logFileName} does not exists..{fileErr}")    
      except FileNotFoundError as fileErr:
            print(f"{logFileName} not found..:{fileErr}")    
      except Exception as Err:
             print(f"Exception occured in createLogFile().:{Err}")  
      return logFileName           

def main():
    try:
        #Initialise Script
        initScript()

    except Exception as excObj:
        print("Exception in main()")    
if __name__=="__main__":
    main()    