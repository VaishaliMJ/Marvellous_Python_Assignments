"""-----------------------------------------------------------------------------------------------------
                          Assignment22_1
                      DuplicateFileRemoval.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Automation script  : DuplicateFileRemoval.py
                   1.Design Automation script Which accepts directory name,duration,email from command line
                   2.Display duplicate files and delete them from the directory use checksum
                   3.Create a directory named "Marvellous" which contains log files
                   4.Name of log file :Date and time of creation of file
                   5.After specified duration delete the duplicate files from the directory
                   6.Make a log entry for deleted files
                   7.Send this log file as an attachment to the fiven email id
                   8.Mail Body: Starting time of scanning
                                Total number of files scanned
                                Total number of duplicate files found 
--------------------------------------------------------------------------------------------------------"""
import Assignment22_Module as Module
import time,os,sys,schedule,hashlib
from dotenv import load_dotenv, dotenv_values 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript(ScriptStartTime):
    try:
        #print(Border)
        print("-----Find Duplicate files and remove from the directory,Create a log of it --------")
        print("\n---Send log file as an attchment to user.Run to delete files periodically--------")
        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application used to find duplicate files")
                print("This Script searches duplicate files,delete and calculates execution time ")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  directoryName schedulatTime Receiver emailId")  
                print("Please provide valid absolute path....")
                print("\nRefer Marvellous/DuplicateFileRemoval_log_{timestamp}.txt for output or error messages...")
            else:
                Module.invalidArgsMsg()
        elif(len(sys.argv)==4):
                  scheduleTaskDeleteDuplicateFiles(ScriptStartTime)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj) 
#-------------------------------------------------------------------------------
# This method schedule tasks
#-------------------------------------------------------------------------------
def scheduleTaskDeleteDuplicateFiles(ScriptStartTime):
    try:
        schedule.every(int(sys.argv[2])).minutes.do(findAndDeleteDuplicateFiles,ScriptStartTime)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except ValueError as valErr:
        print("\nNumber expected...",valErr)
    except Exception as excObj:
        print("\nException in schedule task scheduleDeleteFileTask()")

#-------------------------------------------------------------------------------
#This function first creates log file,then find duplicates from directory
#-------------------------------------------------------------------------------
def findAndDeleteDuplicateFiles(ScriptStartTime):
    try:
        
        directoryName=sys.argv[1]
        #Create log file and folder
        logFileName=createLogFolderAndFile(sys.argv[0],directoryName)#Program name and directory name
        logFileObj=open(logFileName,"a")
        #Validate directory name
        directoryName=Module.validateDirectory(directoryName,logFileObj)
        #Directory travesal and duplicate logic
        scannedFile,duplicateDeleted=directoryTravesalAndDeleteDuplicates(directoryName,logFileObj)
       
        #executionTime=time.time()-ScriptStartTime
        #logFileObj.write(f"\n\nTotal Execution time is :{executionTime}")
        logFileObj.close()
        sendEmail(logFileName,scannedFile,duplicateDeleted,ScriptStartTime)
        
    except FileExistsError as fileErr:
        logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
    except FileNotFoundError as fileErr:
        logFileObj.write(f"{directoryName} not found..:{fileErr}")    
    except Exception as Err:
        logFileObj.write(f"Exception occured in findAndRemoveDuplicateFiles().:{Err}")
#-------------------------------------------------------------------------------
# This method sends an email after creation of log file
#-------------------------------------------------------------------------------
def sendEmail(outputFileName,scannedFile,duplicateDeleted,ScriptStartTime):
    try:        
        receiverEmailId=sys.argv[3]
        # message to be sent
        subject = "Process log file created..."

        body = "Hi,\nDeleted duplicate files log.\n" \
                 f"Execution start time : {ScriptStartTime}\n" \
                 f"Total number of files scanned:{scannedFile}\n" \
                 f"Total number of Duplicate files found:{duplicateDeleted}"
        

    # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = os.getenv("SENDER_EMAIL_ID")
        message["To"] = receiverEmailId
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))


        # Open the file in binary mode
        with open(outputFileName, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
           # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

         # Add header as key/value pair to attachment part
        part.add_header("Content-Disposition", f"attachment; filename= {outputFileName}")

        # Add attachment to message
        message.attach(part)
        # Send the email
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("PORT"))) as server:
            server.starttls()
            server.login(os.getenv("LOGIN"), os.getenv("SENDER_PASSWORD"))
            server.sendmail(os.getenv("SENDER_EMAIL_ID"), receiverEmailId, message.as_string())

        print(f"Email sent successfully to '{receiverEmailId}'")
        
    except Exception as errObj:
         print("\nExeception in sendEmail() method:",errObj)        
#-------------------------------------------------------------------------------
#This function traverse dirctory file
#------------------------------------------------------------------------------
def directoryTravesalAndDeleteDuplicates(directoryName,logFileObj):
    try:
        totalfileCount=0
        for folderName, SubFolderNames, fileNames in os.walk(directoryName):
        #Create dictionary for checksum : filesNames[]
            DuplicateDict={}
            for fileName in fileNames: 
                totalfileCount=totalfileCount+1
                fileName=os.path.join(folderName,fileName)
                checkSum=findCheckSum(fileName,logFileObj)
                if(checkSum in DuplicateDict):
                        DuplicateDict[checkSum].append(fileName)     
                else:
                        DuplicateDict[checkSum]=[fileName]
            totalDuplicateDeleted=findAndRemoveDuplicates(DuplicateDict,logFileObj)                  
        logFileObj.write("\n"+Border)
        logFileObj.write(f"\nTotal scanned files :{totalfileCount}")
        logFileObj.write("\n"+Border)
                
    except FileExistsError as fileErr:
        logFileObj.write(f"{directoryName} does not exists..:{fileErr}")    
    except FileNotFoundError as fileErr:
        logFileObj.write(f"{directoryName} not found..:{fileErr}")    
    except Exception as Err:
        logFileObj.write(f"Exception occured in directoryTravesalAndDeleteDuplicates().:{Err}")            
    return totalfileCount,totalDuplicateDeleted
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
         logFileObj.write(f"\nError in method:findAndRemoveDuplicates():{err}")  
    return totalDuplicateDeleted       
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
      logFileObj.write(f"\nError while calculating checksum Method findCheckSum():{errObj}")
     return hobj.hexdigest()

#-------------------------------------------------------------------------------    
#This function creates log file
#-------------------------------------------------------------------------------
def createLogFolderAndFile(progName,directoryName):
    try:
        #Store log folder name in env file
        logFolderName=os.getenv("LOG_FOLDER")
        if(not(os.path.exists(logFolderName))):
            os.mkdir(logFolderName)
        #generate log file name
        logFileName=Module.generateLogFileName(progName)
        logFileName=os.path.join(logFolderName,logFileName)
        #Creates log file for script
        logFileObj=open(logFileName,'w')
        logFileObj.write("\n"+Border)
        logFileObj.write(f"\n\t\tThis is log file of '{progName}' script") 
        logFileObj.write(f"\n\t\tScript to delete duplicate files in Directory") 
        logFileObj.write(f"\n\t\tInput Directory:'{directoryName}'")
        logFileObj.write("\n"+Border)
        logFileObj.write(f"\n\t\tDate File Created :{Module.formatDate()}")
        logFileObj.write(f"\n\t\tTime File Created :{Module.getCurrFormattedTime()}\n")
        logFileObj.write(Border+"\n")
        logFileObj.close()
    except FileExistsError as fileErr:
        print(f"{logFileName} does not exists..:{fileErr}")    
    except FileNotFoundError as fileErr:
        print(f"{logFileName} not found..:{fileErr}")    
    except Exception as Err:
        print(f"Exception occured in createLogFile().:{Err}")  
    return logFileName           

#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# This function main function initialises script
#------------------------------------------------------------------------------
def main():
    try:
        ScriptStartTime=Module.getCurrFormattedTime()
        print(ScriptStartTime)
    # loading variables from .env file
        load_dotenv()  
        #Initialise script
        initScript(ScriptStartTime)
    except Exception as Err:
      print(f"Exception occured in main().:",Err)  
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------