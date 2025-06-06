"""-----------------------------------------------------------------------------------------------------
                          Assignment14_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Student
                    2. Instance Variable : name,roll_no
                    3. Class Variable : school_name
                    4. Print student details and school name
                    5. Change the school name using class name
---------------------------------------------------------------------------------------------------------"""                    
class Student:
    #Class Variable
    school_name="Ryan"

    #Init method / Constructor
    def __init__(self):
        self.name=""
        self.roll_no=0

    #Accepting students details
    @staticmethod
    def acceptStudentDetails():
        try:
            studentName=input("Enter Student name:")
            studentRollNo=int(input("Enter Student Roll Number:"))


        except ValueError as errObj:
             print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nException occured in acceptStudentDetails :",excObj) 
        return studentName,studentRollNo  
    
    #setting Instance Variables
    def setStudentsDetails(self,studentName,studentRollNo):
        self.name=studentName
        self.roll_no=studentRollNo

    #Display Student details
    def displayStudentData(self):
        print("\nStudent's details are:")
        print("\n-------------------------------------------")   
        print("\nStudent Name        :"+self.name)
        print("\nStudent Roll number :",self.roll_no) 
        print("\nSchool Name         :"+Student.school_name)
        print("\n-------------------------------------------")   

    #Changing school name
    @classmethod
    def changeSchoolName(cls):
        newSchoolName=input("Enter New School Name:")
        print("\n-------------------------------------------")   

        cls.school_name=newSchoolName
         
#--------------------------------------------------------------------------------------------------------    
# This is main method creates Student object and sets student details
#--------------------------------------------------------------------------------------------------------
def main():
    studentObj=""
    try:
        #This function creates the Student class object
        studentObj=Student()
        studentName,studentRollNo = Student.acceptStudentDetails()
        #setter method
        studentObj.setStudentsDetails(studentName,studentRollNo)
        #Display Student details
        studentObj.displayStudentData()

        #Change School name
        Student.changeSchoolName()

        #Display New Student details
        studentObj.displayStudentData()
        
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       



#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
    

