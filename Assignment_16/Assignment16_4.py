"""-----------------------------------------------------------------------------------------------------
                          Assignment16_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create a text file named "numbers.txt" 
                    2. Accept 10 numbers from user
                    3. Write these numbers in file "numbers.txt"
                    4. Each number should be on new line
---------------------------------------------------------------------------------------------------------"""
import os,sys
from Assignment16_Module import checkIfFileExists,acceptInputElements
#-------------------------------------------------------------------------
# This function checks input file exists or not and gets the mode of file
#--------------------------------------------------------------------------
def fileValidation(fileName):
    fileMode=""
    #Checking if file exsists in current directory
    fileExists,currentDirectory=checkIfFileExists(fileName)
    if(fileExists):
        print(f"'{fileName}' already exists in the current '{currentDirectory}'")
        print("\nDo you want to overwrite file or append the data?")
        fileMode=input("\nPress 'O' for Overwrite or 'A' for Append:")
        if(fileMode.lower()=="o"):
            fileMode="w"
        else:
            fileMode="a"
    else:
        #File does not exists, so open in write mode 
        fileMode="w"   
    return fileMode      
#--------------------------------------------------------------------------------------
# This function creates the Data file
#--------------------------------------------------------------------------------------            
def createNumbersDataFile(fileName,fileMode,numberList):
    #Creating file
    try:
        #Opening file
        fileObj=open(fileName,fileMode)
        #Writing data to the file
        for nums in numberList:
            fileObj.write(nums+"\n")
        print(f"\nNumbers updated successfully in file '{fileName}'")
        fileObj.close()
    except Exception as errObj:
        print("Exception while creating file ---> Method createNumbersDataFile():",errObj)            
#--------------------------------------------------------------------------------------
# This is main function accepts inputs from the user
#------------------------------------------------------------------------------------
def main():
    #Acceptiong file name
    fileName=input("Enter the file name:")     #Numbers.txt
    fileMode=fileValidation(fileName)   #If file already exists find mode to open the file
    #Accept Numbers from user 
    numberList=acceptInputElements("Number")
    #Create new file
    createNumbersDataFile(fileName,fileMode,numberList)
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------