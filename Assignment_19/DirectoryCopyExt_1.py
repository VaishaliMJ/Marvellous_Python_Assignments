"""-----------------------------------------------------------------------------------------------------
                          Assignment19_3
                      DirectoryCopyExt.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script program : DirectoryCopyExt
                   1. Design Automation script Which accepts directory name.
                   2. Copy all specific extension files from source directory to target directory
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
      print("\nRefer /Marvellous_log/DirectoryCopyExt_log_{timestamp}.txt in current directory for output or error messages...")

        #print(Border)    #Logic
        #Less number of args
      if(len(sys.argv)==1):
            Module.invalidArgsMsg()
      elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to copy input directory specific extension files to another")
                print("Destination directory created runtime")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName extFile")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryCopyExt_log_{timestamp}.txt for output or error messages...")
            else:
             Module.invalidArgsMsg()    
      elif(len(sys.argv)==3):
                 #Creates log file for script #prog name and directory name
                  logFileName,copyDirectoryName=createLogFile(sys.argv[0],sys.argv[1])
                  #If valid number of args proceed directory search
                  copyDirectoryExtFiles(sys.argv[1],sys.argv[2],logFileName,copyDirectoryName)
      else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError in initScript()...",excObj)  
#-------------------------------------------------------------------------------
# Copy directory logic
#-------------------------------------------------------------------------------         
def copyDirectoryExtFiles(directoryName,extFile,logFileName,copyDirectoryName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate dirctory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory Search logic and rename files
            copyFilesAndFolders(directoryName,logFileObj,copyDirectoryName,extFile)
            #Close file object
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"Exception occured in renameDirectoryFiles().:{Err}")
#-------------------------------------------------------------------------------
# Copying files from source folder to destination folder
#-------------------------------------------------------------------------------
def copyFilesAndFolders(directoryName,logFileObj,copyDirectoryName,extFile):
      try:  
            totalFileCount=0
            #print(directoryName)
            #print(copyDirectoryName)
            baseDirName=os.path.dirname(directoryName)
            #print(baseDirName)
            targetDirName=os.path.join(baseDirName,copyDirectoryName)
            #print(targetDirName)
            if(not(os.path.exists(targetDirName))):
                   os.mkdir(targetDirName)  
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName):          
                  targetFileCount=0

                  for fileName in fileNames:  
                        #print("fileName:",fileName)
                        srcFilePath=os.path.join(folderName,fileName)

                        # targetfilePath=folderName.replace(baseDirName,copyDirectoryName)
                        targetFile=os.path.join(targetDirName,fileName)
                       #print("targetFile",targetFile)
                        isExists=Module.checkIfFileExists(targetFile,logFileObj)
                        destFileNamePath,ext=os.path.splitext(targetFile)

                        if(isExists and not(ext=="")):
                            targetFileCount=targetFileCount+1
                            targetFile=destFileNamePath+"_"+str(targetFileCount)+ext
                            #print("targetFile",targetFile)
                            targetFile=os.path.join(targetDirName,targetFile)
  
                            logFileObj.write(f"\nFile with name already exists.Copying with name:{targetFile}") 

                        if(fileName.endswith(extFile)):
                              #Reading source file
                              sourceFileObj=open(srcFilePath,'r')
                              #Writing data to destination file
                              targetFileObj=open(targetFile,"w")
     
                              targetFileObj.write(sourceFileObj.read())
                              sourceFileObj.close()
                              targetFileObj.close()

                              logFileObj.write(f"\nSource File :{srcFilePath}")
                              logFileObj.write(f"\nTarget File Name:{targetFile}")
                              logFileObj.write(f"\nDate:{Module.formatDate()} Time: {Module.getCurrFormattedTime()}")
                              logFileObj.write("\n"+Border)
                              totalFileCount=totalFileCount+1
            logFileObj.write("\n\n"+Border)            
            logFileObj.write(f"\nSuccessfully copied files:{totalFileCount}")
            logFileObj.write("\n"+Border)
      except OSError as error:
             logFileObj.write(f"\nDirectory '{copyDirectoryName}' can not be created")                 
      except FileExistsError as fileErr:
            logFileObj.write(f"\n{directoryName} does not exists..:{fileErr}")    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"\n{directoryName} not found..:{fileErr}")    
      except Exception as Err:
            logFileObj.write(f"\nException occured in retrieveExtParticularFiles():{Err}")            
#-------------------------------------------------------------------------------
# This function return the name of the log file for directory search
#-------------------------------------------------------------------------------        
def createLogFile(progName,directoryName):
      logFileName=""
      try:
            #Generate log folder and files
            logFolder=Module.getLogFolderName()
            logFileName=Module.generateLogFileName(progName)
            logFileName=os.path.join(logFolder,logFileName)

            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write(Border)
            #Actual directory name
            actualDirectoryName=os.path.basename(directoryName)
            #Copy Directory name
            copyDirectoryName=f"{actualDirectoryName}_Copy"
            copyDirectoryName=f"{copyDirectoryName}_{Module.formatTime()}"
            logFileObj.write(f"\nThis is log file of '{progName}'\n") 
            logFileObj.write(f"\nThis script copy sprcific extension files to new directory")
            logFileObj.write(f"\nDirectory Name :{actualDirectoryName}")
            logFileObj.write(f"\nCopy Directory Name:{copyDirectoryName}")
            logFileObj.write(f"\nCopy files with Extension:{sys.argv[2]}")
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