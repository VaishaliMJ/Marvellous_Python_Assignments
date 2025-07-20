"""-----------------------------------------------------------------------------------------------------
                          Assignment24_6
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Count how many students are passed
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
from Assignment24_5 import updateStatusColumn
import matplotlib.pyplot as plt

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# count passed student
#---------------------------------------------------------------------------------------------------------
def countPassedStudents(dfStudent):
    dfStudent['Total']=dfStudent.sum(axis=1,numeric_only=True)
    print(BORDER)
    print(dfStudent)
    print(BORDER)
    #Passed Students
    passedStudentCnt=(dfStudent['Status']=="Pass").sum()
    print(dfStudent)
    print(BORDER)
    print("\tPassed Students are:",passedStudentCnt)
    print(BORDER)
           
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    studentDF=updateDataFrame(studentDF,colName="Gender")
    #Add 'Status' column
    studentDF=updateStatusColumn(studentDF)
    #Count passed Students
    countPassedStudents(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()