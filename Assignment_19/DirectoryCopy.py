"""-----------------------------------------------------------------------------------------------------
                          Assignment19_3
                      DirectoryCopy.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script program : DirectoryCopy
                   1. Design Automation script Which accepts directory name.
                   2. Copy all content from directory to second one
                   3. Second directory should be created at runtime
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
        print("-----Copy Directory--------")
        print("\nRefer /Marvellous_log/DirectoryCopy_log_{timestamp}.txt in current directory for output or error messages...")

        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to copy input directory to another")
                print("Destination directory created runtime")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryCopy_log_{timestamp}.txt for output or error messages...")
            else:
                 #Creates log file for script #prog name and directory name
                  logFileName,copyDirectoryName=createLogFile(sys.argv[0],sys.argv[1])
                  #If valid number of args proceed directory search
                  copyDirectoryFiles(sys.argv[1],logFileName,copyDirectoryName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print(f"\nError while accepting the command line arguments...{excObj}")  
#-------------------------------------------------------------------------------
# Copy directory logic
#-------------------------------------------------------------------------------         
def copyDirectoryFiles(directoryName,logFileName,copyDirectoryName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate dirctory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory Search logic and rename files
            copyFilesAndFolders(directoryName,logFileObj,copyDirectoryName)
            #Close file object
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"Exception occured in copyDirectoryFiles().:{Err}")
#-------------------------------------------------------------------------------
# Copying files from source folder to destination folder
#-------------------------------------------------------------------------------
def copyFilesAndFolders(directoryName,logFileObj,copyDirectoryName):
      try:  
            totalFolderCount=0
            totalFileCount=0
            baseDirName=os.path.basename(directoryName)
            #print(baseDirName)   #only folder name "Accepted from command line"
            #print(directoryName)
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName): 
                  #print("FolderName:",folderName) 
                  if(folderName.startswith(directoryName)):
                        copyFolder=folderName.replace(baseDirName,copyDirectoryName)
                        #Make recursive directories
                        os.makedirs(copyFolder, exist_ok=True)
                        #Log File entry
                        folderLogFileEntry(logFileObj, folderName, copyFolder)
                        totalFolderCount=totalFolderCount+1
                  for fileName in fileNames:  
                        srcFilePath=os.path.join(folderName,fileName)
                        if(srcFilePath.startswith(directoryName)):  
                              targetfilePath=folderName.replace(baseDirName,copyDirectoryName)
                              targetFile=os.path.join(targetfilePath,fileName)
                              
                              if(not(fileName==".DS_Store")):
                                    #Reading source file
                                    sourceFileObj=open(srcFilePath,'r')
                                    #Writing data to destination file
                                    targetFileObj=open(targetFile,"w")
                                    targetFileObj.write(sourceFileObj.read())
                                    sourceFileObj.close()
                                    targetFileObj.close()

                                    filesLogEntry(logFileObj, srcFilePath, targetFile)
                                    totalFileCount=totalFileCount+1
            logFileObj.write("\n\n"+Border)            
            logFileObj.write(f"\nSuccessfully copied folder:{totalFolderCount}")
            logFileObj.write(f"\nSuccessfully copied files:{totalFileCount}")
            logFileObj.write("\n"+Border)
                
      except OSError as osObj:
             logFileObj.write(f"\nDirectory '{copyDirectoryName}' can not be created:{osObj}")                 
      except FileExistsError as fileErr:
            logFileObj.write(f"\n{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"\n{directoryName} not found..:{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"\nException occured in copyFilesAndFolders().:{Err}") 
#------------------------------------------------------------------
# This function makes log entry of folders
#------------------------------------------------------------------
def filesLogEntry(logFileObj, srcFilePath, targetFile):
    logFileObj.write(f"\nSource File :{srcFilePath}")
    logFileObj.write(f"\nTarget File Name:{targetFile}")
    logFileObj.write(f"\nDate:{Module.formatDate()} Time: {Module.getCurrFormattedTime()}")
    logFileObj.write("\n\n")
#------------------------------------------------------------------
# This function makes log entry for files
#------------------------------------------------------------------
def folderLogFileEntry(logFileObj, folderName, copyFolder):
    logFileObj.write(f"\nSource folder :{folderName}")
    logFileObj.write(f"\nCopied to folder:{copyFolder}")
    logFileObj.write(f"\nDate:{Module.formatDate()} Time: {Module.getCurrFormattedTime()}")
    logFileObj.write("\n\n")           
#-------------------------------------------------------------------------------
# This function return the name of the log file for directory search
#-------------------------------------------------------------------------------        
def createLogFile(progName,directoryName):
      logFileName=""
      try:
            #Generate log folder and files
            logFolder=Module.getLogFolderName()
            #Generate log file name
            logFileName=Module.generateLogFileName(progName)
            logFileName=os.path.join(logFolder,logFileName)

            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write(Border)
            #Actual directory name
            actualDirectoryName=os.path.basename(directoryName)
            #Copy Directory name
            copyDirectoryName=f"{actualDirectoryName}_Copy_{Module.formatTime()}"
            logFileObj.write(f"\n\t\tThis is log file of '{progName}'\n") 
            logFileObj.write(f"\n\t\tThis script makes a copy of directory {actualDirectoryName}")
            logFileObj.write(f"\n\t\tDirectory Name :{actualDirectoryName}")
            logFileObj.write(f"\n\t\tCopy Directory Name:{copyDirectoryName}")
            logFileObj.write("\n"+Border)
            logFileObj.write("\n")
            logFileObj.close()
      except FileExistsError as fileErr:
            print(f"{logFileName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            print(f"{logFileName} not found..:{fileErr}")    
      except Exception as Err:
            print(f"Exception occured in createLogFile().:{Err}")  
      return logFileName,copyDirectoryName                                      
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