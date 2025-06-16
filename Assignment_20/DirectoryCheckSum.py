"""-----------------------------------------------------------------------------------------------------
                          Assignment20_1
                      DirectoryCheckSum.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script program :DirectoryCheckSum.py
                   Design Automation script Which accepts directory from command line
                   Display checksum of all files from the directory
---------------------------------------------------------------------------------------------------------""" 
import Assignment20_Module as Module
import hashlib
import sys,os
Border="-"*70
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Find Checksum of the files--------")
        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to find checksum of files")
                print("This Script finds checksum of input directory")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName")  
                print("Please provide valid absolute path....")
                print("\nRefer DirectoryCheckSum_log_{timestamp}.txt for output or error messages...")
            else:
                  #Creates log file for script
                  logFileName=createLogFile(sys.argv[0],sys.argv[1])
                  #If valid number of args procced directory search
                  calculateCheckSum(sys.argv[1],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Search directory logic and find checksum
#-------------------------------------------------------------------------------         
def calculateCheckSum(directoryName,logFileName):
      try:
            logFileObj=open(logFileName,"a")
            #Validate directory name
            directoryName=Module.validateDirectory(directoryName,logFileObj)
            #Directory Search logic
            directoryTravesalAndFindCheckSum(directoryName,logFileObj)
            logFileObj.close()
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in searchDirectory().:",Err)
#-------------------------------------------------------------------------------
# Retrieving all files and find checksum
#-------------------------------------------------------------------------------
def directoryTravesalAndFindCheckSum(directoryName,logFileObj):
      try:  
            fileCount=0
            for folderName, SubFolderNames, fileNames in os.walk(directoryName):
                  for fileName in fileNames: 
                        fileName=os.path.join(folderName,fileName)
                        checkSum=findCheckSum(fileName)
                        logFileObj.write("\n\n")
                        logFileObj.write(f"\nFile Name:{os.path.basename(fileName)}")
                        logFileObj.write(f"\nCheckSum :{checkSum}")
                        logFileObj.write(f"\nFile Location:'{os.path.join(folderName,fileName)}")
                        fileCount=fileCount+1
            logFileObj.write("\n"+Border)            
            logFileObj.write(f"\nTotal file count : {fileCount}")
            logFileObj.write("\n"+Border)            
      except FileExistsError as fileErr:
            logFileObj.write(f"{directoryName} does not exists..:",fileErr)    
      except FileNotFoundError as fileErr:
            logFileObj.write(f"{directoryName} not found..:",fileErr)    
      except Exception as Err:
            logFileObj.write(f"Exception occured in retrieveExtParticularFiles().:",Err)            
#-------------------------------------------------------------------------------
# This function calculates the checksum of the file
#-------------------------------------------------------------------------------
def findCheckSum(filePath):
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
            print(logFileName)
            #Creates log file for script
            logFileObj=open(logFileName,'w')
            logFileObj.write("\n"+Border)
            actualDirectoryName=os.path.basename(directoryName)
            logFileObj.write(f"\n\t\tThis is log file of '{progName}' program") 
            logFileObj.write(f"\n\t\tFind CheckSum of directory'{actualDirectoryName}' files ")
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