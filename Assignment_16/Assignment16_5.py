"""-----------------------------------------------------------------------------------------------------
                          Assignment16_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1.  Read file line by line
                    2.  Display only those files which contains more than 5 words
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
            print(Border+"\n") 
            #Calling function to count number of words in a line         
            countWordsAndDisplayLine(fileName)  
            print(Border+"\n")             
    except Exception as errObj:
        print("\nError while reading file:",errObj)           
#--------------------------------------------------------------------------------------
# This function counts number of words on a line and display line if word count is > 5
#--------------------------------------------------------------------------------------     
def countWordsAndDisplayLine(fileName):
    try:    
        dataCount=0
        print("Printing lines with word count > 5")
        print(Border+"\n") 
        #Open file in read mode
        fileObj=open(fileName,"r")
        #Read file content
        fileLine=fileObj.readline()
        while fileLine:
            wordList=str(fileLine).split()
            if(len(wordList)>5):
                print(fileLine)
                dataCount=dataCount+1
            fileLine=fileObj.readline()
        if(dataCount==0):
            print("No lines found with given condition...Exiting program")

        #Closing file object    
        fileObj.close()  
    except UnicodeDecodeError as errObj:
        print("\nInvalid File type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj) 

#--------------------------------------------------------------------------------------
# This is main function accepts inputs from the user
#------------------------------------------------------------------------------------
def main():
    #Accepting file name
    fileName=input("Enter the file name:")
    checkFileInPath(fileName)

#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------