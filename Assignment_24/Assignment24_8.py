"""-----------------------------------------------------------------------------------------------------
                          Assignment24_8
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Plot histogram for Maths Marks
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
from Assignment24_5 import updateStatusColumn
import matplotlib.pyplot as plt

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Export data frame to csv
#---------------------------------------------------------------------------------------------------------
def plotHistogram(dfStudent):
    plt.hist(dfStudent['Math'],bins=10,color="skyblue",edgecolor='black')
    plt.xlabel("Math")
    plt.ylabel("Frequncy")
    plt.title("Histogram for Math")
    plt.show()
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
    plotHistogram(studentDF)
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()