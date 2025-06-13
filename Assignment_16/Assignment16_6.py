"""-----------------------------------------------------------------------------------------------------
                          Assignment16_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accept two file names from user
                    2. Source.txt and Destination.txt
                    3. Copy content of Source.txt to Destination.txt
---------------------------------------------------------------------------------------------------------"""
from Assignment16_Module import checkIfFileExists,checkIfFileNotEmpty

#--------------------------------------------------------------------------------------
#Validate the source and destination file
#--------------------------------------------------------------------------------------
def validateFiles(srcFile,destFile):
    try:
        srcExists,currDirectory=checkIfFileExists(srcFile)
        destExists,currDirectory=checkIfFileExists(destFile)
        if(not(srcExists)):
            print(f"\nSource file :'{srcFile}' not found....")
        else:    
            print(f"\nSource file :'{srcFile}' Found....")
            srcEmpty=checkIfFileNotEmpty(srcFile)
            #Source file is valid,start destination file validation
            if(not(srcEmpty)):
                fileMode="w"
                #Check if Destination file is already exists
                if(destExists):
                    overWrite=input(f"'{destFile}' already exists...Overwrite(o) or Append(A)...choose(O/A):")
                    if(overWrite.lower()=="o"):
                        fileMode="w"
                    else:
                        fileMode="a"  
                #copies data from source file to destination file         
                copyFile(srcFile,destFile,fileMode)
            else:
                print(f"\nCopy file not possible.As source file '{srcFile}' is empty")    
    except Exception as excObj:
        print("Exception in ValidateFiles():",excObj)
#--------------------------------------------------------------------------------------
#This function copies data from source file to destination file
#--------------------------------------------------------------------------------------

def copyFile(srcFile,destFile,fileMode):
    try:
        print(fileMode)
        #Check if Destination file is already exists
        srcObj=open(srcFile,"r")
        destObj=open(destFile,fileMode)
        srcData=srcObj.read()
        #print(srcData)
        destObj.write(srcData)
        print(f"\nSuccessfuly copied data from '{srcFile} to '{destFile}'")
        srcObj.close()
        destObj.close()         
    except Exception as exc:
        print("Exception in file:",exc)            

#--------------------------------------------------------------------------------------
# This is main function calls accepts input file names
#-------------------------------------------------------------------------------------
def main():
    sourceFile=input("\nEnter Source file name:")
    destinationFile=input("\nEnter Target file name:")
    #Validate files
    validateFiles(sourceFile,destinationFile)

#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------