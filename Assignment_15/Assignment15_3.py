"""-----------------------------------------------------------------------------------------------------
                          Assignment15_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accepts file name from the user
                    2. Create the file named as Demo.txt
                    3. Copy content from existing file into Demo.txt
                    4. Input e.g.:ABC.txt
                    5. Output e.g.: Create new file as Demo.txt ,Copy content of ABC.txt into Demo.txt
                    6. Accept input from command line
---------------------------------------------------------------------------------------------------------"""
import os,sys
from Assignment15_Module import checkIfFileExists,checkIfFileNotEmpty,invalidArgsMsg

Border="-"*55
#-------------------------------------------------------------------
# This function creates new file 
#-----------------------------------------------------------     
def createNewFile(existingFileName,newFileName):
    print(f"New File to be created:{newFileName}")
    print(f"File to be copied:{existingFileName}")
    #Check if file to be copied exists in the current directory
    print(f"Checking file to be copied '{existingFileName}' exists or not")
    print(f"\nCopy File Details '{existingFileName}'.....")
    copyFileExists,currentWorkingDirectory=checkIfFileExists(existingFileName)
    #print(copyFileExists,"\n\n",currentWorkingDirectory)
    #Check if file to be copied exists or not
    if(copyFileExists):
        #If Copy file exists then check if file is not empty
        isEmpty=checkIfFileNotEmpty(existingFileName)
        if(isEmpty):
            print(f"\nFile to be copied '{existingFileName}' is Empty")
            print("\nExiting Copy Process...")

            return
        else:
            checkNewFile(newFileName,existingFileName)     
    else:
        print(f"\nFile to be copied '{existingFileName}' does not exists.\nLocation :{currentWorkingDirectory}")
        print("\nExiting Copy Process...")
        return
#-----------------------------------------------------------------------------------
# This function checks validity of new file copies content from exisiting file
#------------------------------------------------------------------------------
def checkNewFile(newFileName,existingFileName):
    #Check if new file name already exists
    print(f"\n\nChecking for file to be created '{newFileName}'")
    newFileExists,currentWorkingDirectory=checkIfFileExists(newFileName)
    if(newFileExists):    
        print(f"\nNew File with name {newFileName}' already exists at '{currentWorkingDirectory}' location....")
        overwrite=input(f"Do yo want to overwrite existing '{newFileName}'?(Yes/No):")
        if(overwrite.lower()=="yes" or overwrite.lower()=="y"):
            print(f"Overwriting content of '{newFileName}'....")
            copyFileDetails(newFileName,existingFileName)
        else:
            print(f"\nExiting process...Enter other new file Name....")  
    else:
        print(f"Copying content of '{existingFileName}' to '{newFileName}'....")
        copyFileDetails(newFileName,existingFileName)             
             
#-------------------------------------------------------------------
# This function copies file details to new file
#------------------------------------------------------------------
def copyFileDetails(newFileName,existingFileName):
    try:
        newFileobj=open(newFileName,"w")
        existingFileObj=open(existingFileName,"r")
        copyData=existingFileObj.read()
        #print(copyData)
        newFileobj.write(copyData)   
    except Exception as exeObj:
        print("\nException while copying file content in method copyFileDetails()",exeObj)
    finally:
        newFileobj.close()
        existingFileObj.close()
             
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        print(Border)
        print("---------------Create and Copy File Content---------------")
        print(Border)    #Logic
        
        if(len(sys.argv)==1):
            invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform Create a new file")
                print("This Script copy content of a existing file into newly created file ")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  existingFileName newFileName")  
                print("Please provide valid absolute path....")
            else:
                invalidArgsMsg()       
     
        elif(len(sys.argv)==3):
            createNewFile(sys.argv[1],sys.argv[2])
        else:
            invalidArgsMsg()
        print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)
#--------------------------------------------------------------------------------------
# This is main function calls initScript()
#-------------------------------------------------------------------------------------
def main():
    #Initialise Script
    initScript()
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------