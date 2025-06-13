"""-----------------------------------------------------------------------------------------------------
                          Assignment16_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create a file marks.txt,with student name and marks
                    2. Then read the marks.txt and Display students name with marks > 75
---------------------------------------------------------------------------------------------------------"""
from Assignment16_Module import checkIfFileExists
Border="-"*57
#-------------------------------------------------------------------------------------------
# This Function accepts the Students details
#------------------------------------------------------------------------------------------
def acceptStudentDetails():
    noOfStudents=int(input(f"Enter the number of students:"))
    studentList = dict()
    print(f"Enter the {noOfStudents} students to be added in the list:")
    for count in range(noOfStudents):
        print(Border+"\n")
        print(f"Student ({count+1}) : ")
        studentName=input("Student Name:")
        studentMark=int(input("Student Marks:"))
        studentList.update({studentName:studentMark})
        #print(Border+"\n")
    #print(studentList) 
    return studentList
#-----------------------------------------------------------------------------------
# This function checks if file already exists
#--------------------------------------------------------------------------------------
def getFileWriteMode(studentFile):
    fileMode="w"
    try:
        fileExists,currentDict=checkIfFileExists(studentFile)
        if(fileExists):
            choice=input(f"'{studentFile}' already exists..Overwrite(o) or Append(A)...choose(O/A):")
            if(choice.lower()=="o"):
                fileMode="w"
            if(choice.lower()=="a"):
                fileMode="a"             
    except Exception as excObj:
        print("Exception occured in getFileWriteMode() :",excObj.with_traceback())
    return fileMode
#-----------------------------------------------------------------------------------
# This function writes data to file
#-----------------------------------------------------------------------------------
def writeDataToFile(fileName,fileMode,studentList):
    try:
        if(fileMode=="w"):
            studMarkObj=open(fileName,fileMode)
            studMarkObj.write(str(studentList))
            studMarkObj.close()
        if(fileMode=="a"):
            markObj=open(fileName,'r')
            #first read data from file
            studData = eval(markObj.read()) 
            #Iterate input student data list and add to existing students
            for studName,studMarks in studentList.items():  
                studData.update({studName:studMarks})    
            #print(studData)
            markObj.close()
            
            #Write updated student data to the file
            updatedStud=open(fileName,"w")
            updatedStud.write(str(studData))
            updatedStud.close()
        
    except FileExistsError as fileErr:
        print("File Not exists:",fileErr) 
    except Exception as excObj:
        print("Exception occured in writeDataToFile() :",excObj) 
#-------------------------------------------------------------------------------------
#         
#This method reads student data from txt file and display student marks > 75        
#-------------------------------------------------------------------------------------        
def fetchQualifiedStudentData(fileName):
    try:  
      studObj=open(fileName,'r')
      #Fetching data from file
      studData = eval(studObj.read()) 
      print(Border+"\n")
      print("Displaying Students with marks > 75")
      print(Border)
      #Iterate Dictionary data  
      for studName,studMarks in studData.items():
        if(studMarks>75):
            print(f"Student Name:{studName}\nMarks: {studMarks}")
            print(Border) 
    except FileExistsError as fileErr:
        print("File Not exists:",fileErr) 
    except FileNotFoundError as fileErr:
        print("File Not Found:",fileErr) 
    except Exception as excObj:
        print("Exception occured in fetchQualifiedStudentData() :",excObj)         
#-------------------------------------------------------------------------------------            
# This is main function calls accepts input from user
#-------------------------------------------------------------------------------------
def main():
    try:
        print("\nStudent details program...")
        fileName=input("Enter file name:")
        choice=0
        while(not(choice==3 or choice>3)):
            print(Border)
            print("\nStudents Details Options:")
            print("1.Add Students Details")
            print("2.Display Qualified Students")
            print("3.Exit")
            choice=int(input("Enter your choice:"))
            if(choice==1):
                #First check if file exists
                fileMode=getFileWriteMode(fileName)
                #Accept student details
                studentList=acceptStudentDetails()
                #Write Student name and marks to file
                writeDataToFile(fileName,fileMode,studentList)
            elif(choice==2):
                fileExists,currentDict=checkIfFileExists(fileName)
                if(fileExists):
                    #Read students details from file
                    fetchQualifiedStudentData(fileName)
                else:
                    print(f"\nStudent details file '{fileName}' does not exists.")    
    except ValueError as errObj:
        print("Error while accepting element:",errObj)   
    except Exception as excObj:
        print("Exception occured :",excObj)
    
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------