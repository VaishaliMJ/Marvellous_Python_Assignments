"""-----------------------------------------------------------------------------------------------------
                          Assignment24_10
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Plot a boxPlot for English Marks to check distribution and outliers
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
from Assignment24_5 import updateStatusColumn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Plot a boxPlot for English Marks to check distribution and outliers
#---------------------------------------------------------------------------------------------------------
def plotBoxPlot(dfStudent):
    plt.figure(figsize=(6, 4))
    sns.boxplot(x="Name",y="English",data=dfStudent)
    #plt.boxplot(dfStudent['English'])
    plt.title('Box Plot of English Data')
    plt.ylabel('Value')
    plt.grid(True)
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
    #Plot Box Plot
    plotBoxPlot(studentDF)
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()