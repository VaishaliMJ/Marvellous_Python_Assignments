"""-----------------------------------------------------------------------------------------------------
                          Assignment15_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accepts file name from the user
                    2. Open that file
                    3. Display the contents of that file
---------------------------------------------------------------------------------------------------------"""
import os
from Assignment15_Module import checkIfFileExists

Border="-"*55   
#-------------------------------------------------------------------
#Check if file exists in the given path and then read it
#-------------------------------------------------------------------
def validateAndReadFile(fileName):
    #Check if file exists in given path
    isExists,currentWorkingDirectory=checkIfFileExists(fileName)
    #If file exists then display its contents
    print(f"\nDirectory:'{currentWorkingDirectory}'")
    if(isExists==True):
        print(f"File - '{fileName}' is PRESENT")
        #If file exists then read its content
        readFileContent(fileName,currentWorkingDirectory)
    else:
        print(f"File -'{fileName}' DOES NOT exists")
               
#-------------------------------------------------------------------
# This function opens the given file and reads its contents
#-------------------------------------------------------------------
def readFileContent(fileName,currentWorkingDirectory):
    try:
        #print(Border)
        absDirectoryPath=os.path.abspath(currentWorkingDirectory)
        #Open file in read mode
        fileObj=open(fileName,"r")
        #Find absolute path of file
        absfileName=os.path.join(absDirectoryPath,fileName)
        #Check the size of the file
        fileSize=os.path.getsize(absfileName)
        #fileSize=os.stat(fileName)
        #File empty message
        print(f"File Name :'{fileName}'\nFile size is :{fileSize} bytes")

        if(fileSize==0):
            print(f"\nNothing to display from file ,Empty file")
        else:
            #Read file content
            fileData=fileObj.read()
            print(f"\nDisplaying '{fileName}' contents:")   
            print(Border+"\n") 
            print(fileData)
        #Closing file object    
        fileObj.close()    
    except UnicodeDecodeError as errObj:
        print("\nInvalid FIle type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)          
    print(Border+"\n")  
#--------------------------------------------------------------------------------------
# This is main function accepts input
#-------------------------------------------------------------------------------------
def main():
    try:
        fileName=input("\nEnter the file Name:")
        validateAndReadFile(fileName)
    except Exception as exeObj:
        print("\nException in method main()",exeObj)   
    
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------