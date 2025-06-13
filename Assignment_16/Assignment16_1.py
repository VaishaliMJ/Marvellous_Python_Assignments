"""-----------------------------------------------------------------------------------------------------
                          Assignment16_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create a text file named "Student.txt" 
                    2. Write the names of 5 students in "Student.txt"
                    3. Accepting file name and Student Name from user
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
        #File does not exists so open in write mode 
        fileMode="w"   
    return fileMode      
#--------------------------------------------------------------------------------------
# This function creates the Student Data file
#--------------------------------------------------------------------------------------            
def createStudentDataFile(fileName,fileMode,studentList):
    #Creating file
    try:
        #Opening file
        fileObj=open(fileName,fileMode)
        #Writing data to the file
        for studeName in studentList:
            fileObj.write(studeName+"\n")
        print(f"\nStudent data updated successfully in file '{fileName}'")
        fileObj.close()
    except Exception as errObj:
        print("Exception while creating file ---> Method createStudentDataFile():",errObj)            
#--------------------------------------------------------------------------------------
# This is main function accepts inputs from the user
#------------------------------------------------------------------------------------
def main():
    try:
        #Acceptiong file name
        fileName=input("Enter the file name:")     #Student.txt
        fileMode=fileValidation(fileName)   #If file already exists find mode to open the file
        #Accept student names
        studentList=acceptInputElements("Student")
        #Create new file
        createStudentDataFile(fileName,fileMode,studentList)
    except Exception as errObj:
        print("Exception in main():",errObj)

#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------