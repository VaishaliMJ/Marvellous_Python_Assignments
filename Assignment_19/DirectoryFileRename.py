"""-----------------------------------------------------------------------------------------------------
                          Assignment19_2
                      DirectoryFileRename.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script program : DirectoryFileRename
                   Design Automation script Which accepts directory name and two file extensions from user.
                   Rename first file with second extension  
---------------------------------------------------------------------------------------------------------""" 
import Assignment19_Module as Module
import datetime
import sys,os

Border="-"*70
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Search specific extension files in directory--------")
        print("-----Rename them with new extension--------")
        print("\nRefer /Marvellous_log/DirectoryFileRename_log_{timestamp}.txt in current directory for output or error messages...")


        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1 or len(sys.argv)>4):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to rename specific extension files with new extension")
                print("This Script seraches given extension files in input directory")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName oldfileExtension newFileExtension")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryFileRename_log_{timestamp}.txt for output or error messages...")
            else:
                Module.invalidArgsMsg()       
        elif(len(sys.argv)==4):
            #Creates log file for script
            logFileName=createLogFile(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])
            #If valid number of args proceed directory search
            renameDirectoryFiles(sys.argv[1],sys.argv[2],sys.argv[3],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Search directory logic
#-------------------------------------------------------------------------------         
def renameDirectoryFiles(directoryName,oldExt,newExt,logFileName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate dirctory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory Search logic and rename files
            retrieveAndRenameFiles(directoryName,oldExt,newExt,logFileObj)
            #Close file object
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"Exception occured in renameDirectoryFiles().:{Err}")
#-------------------------------------------------------------------------------
# Retrieving particular extension files and rename with new extension
#-------------------------------------------------------------------------------
def retrieveAndRenameFiles(directoryName,oldExt,newExt,logFileObj):
      try:  
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName):
                  for fileName in fileNames:      
                        oldFilePath=os.path.join(folderName,fileName)
                        if(fileName.endswith(oldExt)):
                             logFileObj.write("\n"+Border)
                             logFileObj.write(f"\nOld File Name:{fileName}")
                             logFileObj.write(f"\nOld File Location:{oldFilePath}")
                             #Replacing old ext with new ext 
                             newFileWithExtensionPath=fileName.replace(oldExt,newExt)
                             #Copying file path
                             newFileWithExtensionPath=os.path.join(folderName,newFileWithExtensionPath)
                             
                             #Renaming the files 
                             os.rename(oldFilePath,newFileWithExtensionPath)
                             
                             logFileObj.write(f"\nRenamed file:{os.path.basename(newFileWithExtensionPath)}")
                             logFileObj.write(f"\nRenamed file Location:{newFileWithExtensionPath}")
                             logFileObj.write(f"\nRenamed on Date:{Module.formatDate()}")
                             logFileObj.write(f"\nRenamed at Time: {Module.getCurrFormattedTime()}")
                             #File counter
                             fileCount=fileCount+1
            logFileObj.write("\n"+Border)            
            logFileObj.write(f"\nRenamed '{oldExt}' with {newExt} File Count: {fileCount}")
            logFileObj.write("\n"+Border)            
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"Exception occured in retrieveExtParticularFiles().:{Err}")            
#-------------------------------------------------------------------------------
# This function return the name of the log file for directory search
#-------------------------------------------------------------------------------        
def createLogFile(progName,directoryName,oldExt,newExt):
      logFileName=""
      try:
            #Generate log folder and files
            logFolder=Module.getLogFolderName()
            logFileName=Module.generateLogFileName(progName)
            logFileName=os.path.join(logFolder,logFileName)

            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write(Border)
            actualDirectoryName=os.path.basename(directoryName)
            logFileObj.write(f"\n\t\tThis is log file of '{progName}'\n") 
            logFileObj.write(Border)
            logFileObj.write(f"\n\t\tSearch Directory Name :{actualDirectoryName}")
            logFileObj.write(f"\n\t\tSearch files with : '{oldExt}' extension \n")
            logFileObj.write(f"\n\t\tRename with : '{newExt}' extension \n")
            
            logFileObj.write(Border)
            logFileObj.write("\n")
            logFileObj.close()
      except FileExistsError as fileErr:
            print(f"{logFileName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            print(f"{logFileName} not found..:{fileErr}")    
      except Exception as Err:
            print(f"Exception occured in createLogFile().:{Err}")  
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