"""-----------------------------------------------------------------------------------------------------
                          Assignment23_4
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 
                   4. Display student who has scored more than 85 marks in Science
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF

BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Display Students who has scored more than 85 marks in Science
#---------------------------------------------------------------------------------------------------------
def displayStudents85MarksInScience(df_student,subName,subMarks):
    print(BORDER)            
    print(f"\tStudents details : {subName} Marks  > {subMarks}")
    print(BORDER)            
    for cnt in df_student.index:
        sciMarks=df_student[subName].iloc[cnt]
        if(sciMarks>subMarks):
            print(df_student.iloc[cnt])
            print(BORDER)
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Display Students with maximum marks in science
    displayStudents85MarksInScience(studentDF,subName='Science',subMarks=85)

#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()