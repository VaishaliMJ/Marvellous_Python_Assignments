"""-----------------------------------------------------------------------------------------------------
                          Assignment16_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Write a script to remove all blank lines from a file
                    2. Save cleaned output to a new file
---------------------------------------------------------------------------------------------------------"""                    
from Assignment16_Module import checkIfFileExists,checkIfFileNotEmpty
import time
Border="-"*57
#--------------------------------------------------------------------------------------
#This function read file
#--------------------------------------------------------------------------------------
def readAndCleanFile(fileName,currentDict):
    try:
        fileNamePrefix=fileName.split(".")
        updatedFileName=f"{fileNamePrefix[0]}_CLEAN.{fileNamePrefix[1]}"
        
        fileObj=open(fileName,"r")
        #Creating object for new file
        fileCleanDataObj=open(updatedFileName,"w")
        fileLineData=fileObj.readline()
        while(fileLineData):
            if(len(fileLineData)>1 and not(fileLineData.isspace())):
                #print(len(fileLineData))
                #Writing data to new file
                fileCleanDataObj.write(str(fileLineData))
            fileLineData=fileObj.readline()
        #Close file objects
        fileObj.close()
        fileCleanDataObj.close()  
        print(f"\nCleaned data copied to file :'{updatedFileName}'") 
        print(f"\nFile Location:{currentDict}") 
        print(Border)
    except FileExistsError as fileErr:
        print("File Not exists:",fileErr) 
    except FileNotFoundError as fileErr:
        print("File Not Found:",fileErr) 
    except Exception as excObj:
        print("Exception occured in readAndCleanFile() :",excObj)         
   
#--------------------------------------------------------------------------------------
# This is main function accept input
#------------------------------------------------------------------------------------
def main():
    try:
        print("\nThis is script for removing all blank lines from file")
        fileName=input("Enter file name :")
        fileExists,currentDict=checkIfFileExists(fileName)
        if(fileExists):
            print(Border)
            isEmpty=checkIfFileNotEmpty(fileName)
            print(Border)

            #File is not empty
            if(not(isEmpty)):
                readAndCleanFile(fileName,currentDict)
            else:
                print(f"\n'{fileName}' is Empty.Exiting process")

        else:
            print(f"\n'{fileName}' not found.Exiting process")

    except ValueError as errObj:
        print("Error while accepting element:",errObj)   
    except Exception as excObj:
        print("Exception occured :",excObj)   
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------