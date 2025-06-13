"""-----------------------------------------------------------------------------------------------------
                          Assignment16_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1.  Read and display the content of file "Data.txt"
---------------------------------------------------------------------------------------------------------"""
import os
from Assignment16_Module import checkIfFileExists
Border="-"*57
#-------------------------------------------------------------------
#Check if file exists in the given path
#-------------------------------------------------------------------
def checkFileInPath(fileName):
    #Check if file exists in given path
    isExists,currentWorkingDirectory=checkIfFileExists(fileName)
    #If file exists then display its contents
    print(f"\nFinding file in '{currentWorkingDirectory}'")
    if(isExists==True):
        print(f"\n\nFile - '{fileName}' FOUND....")
        #If file exists then read its content
        readFileContent(fileName,currentWorkingDirectory)
    else:
        print(f"\n\nFile -'{fileName}' NOT FOUND.....")
    print(Border+"\n")    
#-------------------------------------------------------------------
# This function opens the given file and reads its contents
#-------------------------------------------------------------------
def readFileContent(fileName,currentWorkingDirectory):
    try:
        #print(Border)
        absDirectoryPath=os.path.abspath(currentWorkingDirectory)
        
        #Find absolute path of file
        absfileName=os.path.join(absDirectoryPath,fileName)
        #Check the size of the file
        fileSize=os.path.getsize(absfileName)
        print(f"File Name :'{fileName}'\nFile size:{fileSize} bytes")
        #File empty message
        if(fileSize==0):
            print(f"File contains no data...\nFile is Empty.")
        else:
            #Open file in read mode
            fileObj=open(fileName,"r")
            #Read file content
            fileData=fileObj.read()
            print(f"\nDisplaying '{fileName}' contents.......")   
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
# This is main function accepts inputs from the user
#------------------------------------------------------------------------------------
def main():
    try:
        #Accepting file name
        fileName=input("Enter the file name:")
        checkFileInPath(fileName)
    except Exception as errObj:
        print("\nException in main():",errObj) 
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------