"""-----------------------------------------------------------------------------------------------------
                          Assignment24_9
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Rename 'Math' column to 'Mathematics'
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
from Assignment24_5 import updateStatusColumn
import matplotlib.pyplot as plt

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Rename 'Math' column to 'Mathematics'
#---------------------------------------------------------------------------------------------------------
def renameColumn(dfStudent):
   #dfStudent.rename(columns={"Math":"Mathematics"})
   dfStudent.rename(columns={"Math": "Mathematics"},inplace=True)
   print(BORDER)
   print("\nUpdated Coulmn Name from 'Math' to 'Mathematics'")
   print(dfStudent)
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
    renameColumn(studentDF)
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()