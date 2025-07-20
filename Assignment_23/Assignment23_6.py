"""-----------------------------------------------------------------------------------------------------
                          Assignment23_6
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 
                   6. Sort DataFrame by "Total" Marks in Descending order
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
import Assignment23_5 as replacedDF

BORDER="-"*50


#---------------------------------------------------------------------------------------------------------
# Sort student details by 'Total' marks in descnding order
#---------------------------------------------------------------------------------------------------------
def sortStudentByTotalMarksDescending(df_student):
    df_student=df_student.sort_values(by="Total",ascending=False)
    print(BORDER)
    print("\tSorted 'Total' Marks descending order")
    print(BORDER)
    print(df_student)
    return df_student
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replacedDF.replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
    #Sort data frame by "Total" marks using Descending order
    sortStudentByTotalMarksDescending(studentDF)

#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()