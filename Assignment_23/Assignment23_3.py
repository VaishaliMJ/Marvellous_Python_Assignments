"""-----------------------------------------------------------------------------------------------------
                          Assignment23_3
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 3. Add a new coulmn "Total" to the dataFrame to calculate sum of all subjects
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import Assignment23_1 as studDF
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Calculate total marks
#---------------------------------------------------------------------------------------------------------
def updateDataFrame(df_student):
    df_student["Total"]=df_student.sum(axis=1,numeric_only=True)
    print("\t\tTotal Marks of Students")
    print(BORDER)
    print(df_student.head())
    print(BORDER)
    return df_student
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.createStudentData()
    #Calculate total marks
    studentDF=updateDataFrame(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()