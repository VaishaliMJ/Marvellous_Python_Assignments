"""-----------------------------------------------------------------------------------------------------
                          Assignment15_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accepts file names  and Search String from the user
                    2. If Search String found in the file display its frequency
---------------------------------------------------------------------------------------------------------"""
from Assignment15_Module import checkIfFileExists,checkIfFileNotEmpty
Border="-"*55
#------------------------------------------------------------------------
# Read input file and find string occurance in the file
#------------------------------------------------------------------------

def readInputFile(fileName,searchString):
    try:
        strCount=0
        #Open file in read mode
        fileObj=open(fileName,"r")
        #Fetch file data
        fileData=fileObj.read()
        #Split File data by WHITE SPACES
        inputStrList=fileData.split()
        for inputStr in inputStrList:
            #print(inputStr)
            if(inputStr.lower()==searchString.lower()):
                strCount+=1
        print(Border,"\n")
        print(f"'{searchString}' frequency in file :{strCount} times ")
        print(Border,"\n")    
    except FileExistsError as fileErr:
        print("File Exists Error:",fileErr)  
    except FileNotFoundError as FileErr:
        print("File Not found:",fileErr) 
    except Exception as exc:
        print("Exception reading file:",exc)    
    finally:
        fileObj.close()     
#------------------------------------------------------------------------
# This function finds input String in file
#---------------------------------------------------------------------
def findFreqInFile(fileName,searchString):
    print(f"Finding {searchString}' occurence in '{fileName}'......")

    #Check if file exists
    isExists,currentDir=checkIfFileExists(fileName)
    #File found
    if(isExists):
        #Check if file is not empty
        isEmpty=checkIfFileNotEmpty(fileName)
        if(not(isEmpty)):
            readInputFile(fileName,searchString)
        else:
            print(f"File Name :'{fileName}' EMPTY.")
            return
    else:    
        print(f"'{fileName}' file not found...") 
#--------------------------------------------------------------------------------------
# This is main function accepts input
#-------------------------------------------------------------------------------------
def main():
    try:
        print("\nEnter file name and String to be searched .....")
        fileName=input("\nEnter the file Name:")
        searchString=input("\nEnter the String to be searched:")
        findFreqInFile(fileName,searchString)
    except Exception as exeObj:
        print("\nException in method main()",exeObj)   
    
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------