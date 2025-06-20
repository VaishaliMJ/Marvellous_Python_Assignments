"""-----------------------------------------------------------------------------------------------------
                        Assignment21_1
                         ProcInfo.py
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Design automation script which display information of 
                   running processes as its name,pid and username
---------------------------------------------------------------------------------------------------------""" 
import Assignment21_Module as Module
import psutil,sys,os
Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        print("-----Display currently running processes--------")
        print("This application is used to display currently running processes")
        #Creates log file for script
        logFileName=createLogFile(sys.argv[0])
        #If valid number of args procced directory search
        displayCurrentProcesses(logFileName)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Displays current processes
#-------------------------------------------------------------------------------
def displayCurrentProcesses(logFileName):
    try:
        print(logFileName)
        #open log file
        logFolderName=Module.getLogFolderName()  
        dictOutput=os.path.join(logFolderName,"outputProcInfo.txt")
        logFileObj=open(logFileName,"a")
        outputobj=open(dictOutput,"w")
        logFileObj.write(f"\nProcess output saved in :\n\t\t{dictOutput}\n\n") 

        for proc in psutil.process_iter():
            infoProc=proc.as_dict(attrs=['pid','name','username'])
            
            logFileObj.write(str(infoProc))
            print(infoProc)
            #Redirect output to file
            print(infoProc,file=outputobj) 
        
        outputobj.close()
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
            print(f"{logFileName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            print(f"{logFileName} not found..:{fileErr}")    
      except Exception as Err:
             print(f"Exception occured in createLogFile().:{Err}")  
      return logFileName           
#-------------------------------------------------------------------------------        
#Initialise the script
#-------------------------------------------------------------------------------        

def main():
    try:
        #Initialise Script
        initScript()

    except Exception as excObj:
        print("Exception in main()")  
#-------------------------------------------------------------------------------          
if __name__=="__main__":
    main()    
#-------------------------------------------------------------------------------    