"""-----------------------------------------------------------------------------------------------------
                          Assignment23_2
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks and print basic information like shape,coulmns 
                   and data types 
                   2. Print descriptive statistics using .describe()
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import Assignment23_1 as studDF
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Displays descriptive statistics using .describe()
#---------------------------------------------------------------------------------------------------------
def displayStudentStatistics(df_student):
    print(BORDER)
    print("\tStudent Statistics Details")
    print(BORDER)
    print(df_student.describe())
    print(BORDER)
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    studentDF=studDF.createStudentData()
    displayStudentStatistics(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()