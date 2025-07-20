"""-----------------------------------------------------------------------------------------------------
                          Assignment24_3
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks.Group students by 'Gender' and calculate Avg marks
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
#Group students by 'Gender' and calculate Avg marks
#---------------------------------------------------------------------------------------------------------
def calculateAvgByGroupBy(dfStudent):   #ColName='Gender'
    dfStudent=dfStudent.groupby('Gender')[['Math','Science','English']].mean()
    print(BORDER)
    print("Group by 'Gender' and Calculated Avg of each column")
    print(dfStudent)
    print(BORDER)
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    studentDF=updateDataFrame(studentDF,colName="Gender")
    #Group data frame by 'Gender' and calculate Average
    calculateAvgByGroupBy(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()