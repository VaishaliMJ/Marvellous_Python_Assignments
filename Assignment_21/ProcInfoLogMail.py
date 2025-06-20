"""-----------------------------------------------------------------------------------------------------
                        Assignment21_4
                        ProcInfo.py
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 1.Design automation script which accepts directory name and email id from user.
                   2.Creates log file in the directory
                   3.Log file contains information of all running processes as its name,pid and username
                   4.After creating log file send email to mentioned email id
---------------------------------------------------------------------------------------------------------""" 
import Assignment21_Module as Module
import psutil,sys,os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

Border="-"*80
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        #print(Border)
        print("-----Display information of running processes--------")
        #print(Border)    #Logic
        #Less number of args
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This Script shows running process information")
                print("FolderName accepted from command line,which contains output log file")
            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  folderName")  
                print("\nRefer argv[1]/ProcInfoLog.txt for output or error messages...")
            else:
                Module.invalidArgsMsg()    
        elif(len(sys.argv)==3):
                  #Creates log file for script
                  logFileName=createLogFile(sys.argv[0])
                  #If valid number of args procced directory search
                  redirectOutputToFileAndSendMail(sys.argv[1],logFileName)
        else:
            Module.invalidArgsMsg()
       #print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)  
#-------------------------------------------------------------------------------
# Displays all running processes and redirect output to a file
#-------------------------------------------------------------------------------
def redirectOutputToFileAndSendMail(outputDirectoryName,logFileName):
    try:            
        if(not(os.path.exists(outputDirectoryName))):
            os.mkdir(outputDirectoryName)
        #output file name
        outputFileName=sys.argv[0].split(".")[0]+".txt"    
        outputFileName=os.path.join(outputDirectoryName,outputFileName)
        logFileObj=open(logFileName,"a")
        outputobj=open(outputFileName,"w")
        logFileObj.write(f"\nProcess output saved in :\n\t\t{outputFileName}\n\n") 

        for proc in psutil.process_iter():
            infoProc=proc.as_dict(attrs=['pid','name','username'])
            #logFileObj.write(str(infoProc))
            #Redirect output to file
            print(infoProc,file=outputobj) 
        
        outputobj.close()
    except Exception as Err:
        logFileObj.write(f"Exception occured redirectOutputToFile().:",Err)  
    finally:
         logFileObj.close() 
         sendEmail(outputFileName)   
#-------------------------------------------------------------------------------
# This method sends an email after creation of log file
#-------------------------------------------------------------------------------
def sendEmail(outputFileName):
    try:    
        #Receiver Email-id
        receiverEmailId=sys.argv[2]
       
        body = "Hi,\nAttached log file of currently running process log."

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = os.getenv("SENDER_EMAIL_ID")
        message["To"] = receiverEmailId
        message["Subject"] = "Process log file created..."

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
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("PORT")) as server:
            server.starttls()
            server.login(os.getenv("LOGIN"), os.getenv("SENDER_PASSWORD"))
            server.sendmail(os.getenv("SENDER_EMAIL_ID"), receiverEmailId, message.as_string())

        print(f"Process log mail successfully sent to :{sys.argv[2]}")
        
    except Exception as errObj:
         print("\nExeception in sendEmail() method:",errObj)
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
#------------------------------------------------------------------------------
#Main method,Initialise script and load env variables
#------------------------------------------------------------------------------
def main():
    try:
        # loading variables from .env file
        load_dotenv()  
        #Initialise Script
        initScript()
#------------------------------------------------------------------------------
    except Exception as excObj:
        print("Exception in main()")    
if __name__=="__main__":
    main()    