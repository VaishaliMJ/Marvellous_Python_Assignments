"""-----------------------------------------------------------------------------------------------------
                          Assignment16_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    Write a python script to count the number of lines,words and characters in a given file
------------------------------------------------------------------------------------------------------------"""
import os,sys
from Assignment16_Module import checkIfFileExists,invalidArgsMsg
Border="-"*57
#------------------------------------------------------------------------
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        print(Border)
        print("Display Number of lines,words and characters from the file")
        print(Border)    #Logic
       
        if(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to print following details.\nNumber of lines\nNumber of Words\nNumber of Characters")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  FileName")  
                print("Please provide valid absolute path....")
            else:
                validateAndReadFile(sys.argv[1])      
        else:
            invalidArgsMsg()
        print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)
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
            #Open file in read mode
            countNumberOfLinesWordChar(fileName)
            #print(Border+"\n")     
    except UnicodeDecodeError as errObj:
        print("\nInvalid FIle type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)          
#--------------------------------------------------------------------------------------
#This function counts number of lines,words and characters of file
#--------------------------------------------------------------------------------------
def countNumberOfLinesWordChar(fileName):
    try:
        fileObj=open(fileName,"r")
        #Read file content
        fileData=fileObj.readlines()
        print(Border+"\n") 
        print("Number of lines,words and character in the file")  
        print(Border+"\n") 
        #print(fileData)
        lineCount=len(fileData)
        wordCount=0
        charCount=0
        for lineData in fileData:
            #print(lineData.strip())
            #lineCount=lineCount+1
            wordList=str(lineData).split()
            wordCount=wordCount+ len(wordList) 
            for charList in wordList: 
                charCount=charCount+len(charList)
        print(f"Number of Lines      : {lineCount}")
        print(f"\nNumber of Words      : {wordCount}")
        print(f"\nNumber of Characters : {charCount}")
        #Closing file object    
        fileObj.close()  
    except UnicodeDecodeError as errObj:
        print("\nInvalid FIle type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)      
#--------------------------------------------------------------------------------------
# This is main function initialise script
#-------------------------------------------------------------------------------------
def main():
    #init Script
    initScript()
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------