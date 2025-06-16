"""-----------------------------------------------------------------------------------------------------
                          Assignment20_3
                      DirectoryDuplicateRemoval.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script  : DirectoryDuplicateRemoval.py
                   Design Automation script Which accepts directory from command line
                   Display duplicate files and delete them from the directory
---------------------------------------------------------------------------------------------------------""" 
import Assignment20_Module as Module
import hashlib
import sys,os
Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Find Duplicate files and remove from the directory--------")
        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to find duplicate files")
                print("This Script searches duplicate files and delete ")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryDuplicateRemoval_log_{timestamp}.txt for output or error messages...")
            else:
                  #Creates log file for script
                  logFileName=createLogFile(sys.argv[0],sys.argv[1])
                  #If valid number of args procced directory search
                  findAndRemoveDuplicateFiles(sys.argv[1],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Search directory for duplicate files and remove them
#-------------------------------------------------------------------------------         
def findAndRemoveDuplicateFiles(directoryName,logFileName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate directory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory travesal and duplicate logic
            directoryTravesalAndDeleteDuplicates(directoryName,logFileObj)
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in searchDirectory().:",Err)
#-------------------------------------------------------------------------------
# Retrieving all files and Duplicate logic using check sum
#-------------------------------------------------------------------------------
def directoryTravesalAndDeleteDuplicates(directoryName,logFileObj):
      try:  
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName):
                  #Create dictionary for checksum : filesNames[]
                  DuplicateDict={}
                  for fileName in fileNames: 
                        fileName=os.path.join(folderName,fileName)
                        checkSum=findCheckSum(fileName,logFileObj)
                        if(checkSum in DuplicateDict):
                              DuplicateDict[checkSum].append(fileName)     
                        else:
                              DuplicateDict[checkSum]=[fileName]
            findAndRemoveDuplicates(DuplicateDict,logFileObj)                  
                        
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in retrieveExtParticularFiles().:",Err)            
#------------------------------------------------------------------------------
# Find the name of the duplicate files and delete them
#------------------------------------------------------------------------------
def findAndRemoveDuplicates(DuplicateFileDict,logFileObj):
    try:
      #print(DuplicateFileDict)
      duplicateFileList=list(filter(lambda fileList:(len(fileList)>1),DuplicateFileDict.values()))
      totalDuplicateDeleted=0
      for fileNamesList in duplicateFileList:
            logFileObj.write(f"\nDuplicates Files:{fileNamesList}")
            count=0
            for fileName in fileNamesList:
                  logFileObj.write(f"\n\t\tFile Name:\t{fileName}") 
                  count=count+1
                  if(count>1):
                      os.remove(fileName)
                      totalDuplicateDeleted=totalDuplicateDeleted+1
                      logFileObj.write(f"\n\t\tDeleted File Name:\t{fileName}") 
            logFileObj.write("\n"+Border)
      logFileObj.write(f"\nTotal deleted duplicate files :{totalDuplicateDeleted}")
      logFileObj.write("\n"+Border)

    except Exception as err:
         logFileObj.write("Error in method:findDuplicates()",err)      
#-------------------------------------------------------------------------------
# This function calculates the checksum of the file
#-------------------------------------------------------------------------------
def findCheckSum(filePath,logFileObj):
     try:
            #Define buffer size
            BlockSize=1024
            #open file in binary mode
            fObj=open(filePath,"rb")
            #Use hashlib md5 algorithm to find checksum of file
            hobj=hashlib.md5()
            buffer=fObj.read(BlockSize) 
            while(len(buffer)>0):
                  hobj.update(buffer)
                  buffer=fObj.read(BlockSize) 
            fObj.close()   
     except Exception as errObj:
      logFileObj.write("Error while calculating checksum Method findCheckSum()",errObj)
     return hobj.hexdigest()
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
            logFileObj.write("\n"+Border)
            actualDirectoryName=os.path.basename(directoryName)
            logFileObj.write(f"\n\t\tThis is log file of '{progName}' program") 
            logFileObj.write(f"\n\t\tFind Duplicate files in the directory'{actualDirectoryName}' files ")
            logFileObj.write("\n"+Border)
            logFileObj.write(f"\n\t\tScript Date Created :{Module.formatDate()}")
            logFileObj.write(f"\n\t\tTime Created :{Module.getCurrFormattedTime()}")
            logFileObj.write(f"\n\t\tDirectory Name :{actualDirectoryName}")
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