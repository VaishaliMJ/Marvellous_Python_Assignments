"""-----------------------------------------------------------------------------------------------------
                          Assignment15_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accepts file name from the user
                    2. Checks whether that file exists in current directory or not
---------------------------------------------------------------------------------------------------------"""
import os,sys
from Assignment15_Module import checkIfFileExists,invalidArgsMsg
Border="-"*55
#--------------------------------------------------------------------------------------
# This is main function checks if file exists in given path
#--------------------------------------------------------------------------------------
def checkFileInPath(FileName):
    Border="-"*55
    #Traverse current working directory
    isExists,currentWorkingDirectory= checkIfFileExists(FileName)
    print(f"\n{Border}")

    if(isExists==True):
        print(f"File - '{FileName}' is PRESENT in the current directory :\n'{currentWorkingDirectory}'")
    else:
        print(f"File -'{FileName}' DOES NOT exists in current directory: \n'{currentWorkingDirectory}'")
    print(f"\n{Border}")
#--------------------------------------------------------------------------------------
# This is main function accepts input
#------------------------------------------------------------------------------------
def main():
    try:
        fileName=input("\nEnter the file Name:")
        checkFileInPath(fileName)
    except Exception as exeObj:
        print("\nException in method main()",exeObj)   
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------