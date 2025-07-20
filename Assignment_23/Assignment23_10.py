"""-----------------------------------------------------------------------------------------------------
                          Assignment23_10
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks and print basic information like shape,coulmns 
                   and data types 
                   2. Print descriptive statistics using .describe()
                   3. Add a new coulmn "Total" to the dataFrame to calculate sum of all subjects
                   4. Display student who has scored more than 85 marks in Science
                   5. Replace "Pooja" with "Puja" in "Name" coulmn
                   6. Sort DataFrame by "Total" Marks in Descending order
                   7. Create a bar plot Student Name vs Total Marks
                   8. Plot a line chart for 'Amit' across all the subjects
                   9. Create a data frame with missing values and fill them with coulmn mean 
                   10. Drop 'English' coulmn from original data frame
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
import Assignment23_5 as replacedDF

BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Drop a specific column
#---------------------------------------------------------------------------------------------------------
def dropColumn(df_student,columnName):
    df_student.drop(columns=[columnName],inplace=True)
    print(BORDER)
    print(f"\tDropped '{columnName}' from Student Details")
    print(BORDER)
    #Print data frame
    print(df_student.head())
    print(BORDER)  
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replacedDF.replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
    #Drop 'English' column from original data frame
    dropColumn(studentDF,columnName='English')

#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()