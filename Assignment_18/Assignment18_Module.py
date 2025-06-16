"""-----------------------------------------------------------------------------------------------------
                          Assignment18_Module
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement :This file coniatins all common functions used in Assignment 15
---------------------------------------------------------------------------------------------------------"""
import os
#-------------------------------------------------------------------
#Invalid command line arguments message
#-------------------------------------------------------------------
def invalidArgsMsg():
    print("Invalid number of command line arguments....")
    print("use the given flags as :")
    print("--h : Used to display the help")
    print("--u : Used to display the usage")        
#-------------------------------------------------------------------
#This function checks if file exists in the current directory
#-------------------------------------------------------------------
def checkIfFileExists(FileName):
    try:
        Border="-"*55
        #Gets current working directory path
        currentWorkingDirectory=os.getcwd()
        print(f"\n{Border}")
        print("Absolute Path:",currentWorkingDirectory)
        print(f"\n{Border}")

        #Traverse current working directory
        fileExists= os.path.exists(FileName)
    except Exception as exeObj:
        print("\nException in method checkFileIfFileExists()",exeObj)   
    return fileExists,currentWorkingDirectory

#-------------------------------------------------------------------
# This function opens the given file and reads its contents
#-------------------------------------------------------------------
def checkIfFileNotEmpty(fileName):
    try:
        #print(Border)
        #Finding absolute file path
        absfileName=os.path.abspath(fileName)
        #print(absfileName)
        #Check the size of the file
        fileSize=os.path.getsize(absfileName)
        #File empty message
        if(fileSize==0):
            print(f"File Name :'{fileName}'\nFile size is :0 bytes.")
            return True
        else:
            print(f"File Name :'{fileName}'\nFile size is :{fileSize} bytes.")
            return False
    except Exception as exeObj:
        print("\nExecption in checkIfFileNotEmpty() method.",exeObj)
    
#-------------------------------------------------------------------
