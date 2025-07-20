"""-----------------------------------------------------------------------------------------------------
                          Assignment24_5
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Add a new Column "Status" where students with total >= 250 are 'Pass' ,else 'Fail'
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
import matplotlib.pyplot as plt

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Add a new Column "Status" 
# where students with total >= 250 are 'Pass' ,else 'Fail'
#---------------------------------------------------------------------------------------------------------
def updateStatusColumn(dfStudent):
    dfStudent['Total']=dfStudent.sum(axis=1,numeric_only=True)
    print(BORDER)
    print(dfStudent)
    print(BORDER)
    #With lambda
    dfStudent['Status']=dfStudent['Total'].apply(lambda x: "Pass" if x>=250 else "Fail")
    print(dfStudent)
    print(BORDER)
    print("\tUpdated Result")
    print(dfStudent)
    print(BORDER)
    return dfStudent       
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    studentDF=updateDataFrame(studentDF,colName="Gender")
    #Add 'Status' column
    studentDF=updateStatusColumn(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()