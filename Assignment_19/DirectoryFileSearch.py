"""-----------------------------------------------------------------------------------------------------
                          Assignment19_1
                      DirectoryFileSearch.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script program : DirectoryFileSearch
                   Design Automation script Which accepts directory name and file extension from user.
                   Display all the files from directory with that extension 
---------------------------------------------------------------------------------------------------------""" 
import Assignment19_Module as Module
import datetime
import sys,os
Border="-"*59
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Search specific extension files in directory--------")
        print("\nRefer /Marvellous_log/DirectoryFileSearch_log_{timestamp}.txt in current directory for output or error messages...")

        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to find specific extension files")
                print("This Script searches given extension files in input directory")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName fileExtension")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryFileSearch_log_{timestamp}.txt for output or error messages...")
            else:
                Module.invalidArgsMsg()       
        elif(len(sys.argv)==3):
            #Creates log file for script
            logFileName=createLogFile(sys.argv[0],sys.argv[1],sys.argv[2])
            #If valid number of args procced directory search
            searchDirectory(sys.argv[1],sys.argv[2],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Search directory logic
#-------------------------------------------------------------------------------         
def searchDirectory(directoryName,extFile,logFileName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate directory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory Search logic
            retrieveExtParticularFiles(directoryName,extFile,logFileObj)
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in searchDirectory().:",Err)
#-------------------------------------------------------------------------------
# Retrieving particular extension files only
#-------------------------------------------------------------------------------
def retrieveExtParticularFiles(directoryName,extFile,logFileObj):
      try:  
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName):
                  for fileName in fileNames: 
                        if(fileName.endswith(extFile)):
                             logFileObj.write("\n")
                             logFileObj.write(f"\nFile Name:{fileName}")
                             logFileObj.write(f"\nFile Location:'{os.path.join(folderName,fileName)}")
                             fileCount=fileCount+1
            logFileObj.write("\n"+Border)            
            logFileObj.write(f"\nTotal file count with '{extFile}' : {fileCount}")
            logFileObj.write("\n"+Border)            
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in retrieveExtParticularFiles().:",Err)            
#-------------------------------------------------------------------------------
# This function return the name of the log file for directory search
#-------------------------------------------------------------------------------        
def createLogFile(progName,directoryName,extFile):
      logFileName=""
      try:
            #Generate log folder and files
            logFolder=Module.getLogFolderName()
            logFileName=Module.generateLogFileName(progName)
            logFileName=os.path.join(logFolder,logFileName)
            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write("\n"+Border)
            actualDirectoryName=os.path.basename(directoryName)
            logFileObj.write(f"\n\t\tThis is log file of '{progName}' program\n") 
            logFileObj.write(f"\n\t\tSearch script for specific extension files ")
            logFileObj.write("\n"+Border)
            logFileObj.write(f"\n\t\tScript Date Created :{Module.formatDate()}")
            logFileObj.write(f"\n\t\tTime Created :{Module.getCurrFormattedTime()}")
            logFileObj.write(f"\n\t\tSearch Directory Name :{actualDirectoryName}")
            logFileObj.write(f"\n\t\tSearch files with : '{extFile}' extension")
            logFileObj.write(f"\n\t\tDirectory location:{directoryName}\n")

            logFileObj.write(Border+"\n")
            logFileObj.close()
      except FileExistsError as fileErr:
            print(f"{logFileName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            print(f"{logFileName} not found..:",fileErr)    
      except Exception as Err:
             print(f"Exception occured in createLogFile().:",Err)  
      return logFileName           
#-------------------------------------------------------------------------------
# This function main function initialises script
#------------------------------------------------------------------------------
def main():
    try:
      #Initialise script
      initScript()
    except Exception as Err:
      print(f"Exception occured in main().:",Err)  
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------