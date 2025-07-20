"""-----------------------------------------------------------------------------------------------------
                          Assignment24_4
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks.
                    Plot a pie chart of subject marks for 'Sagar'
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
from Assignment24_2 import updateDataFrame
import matplotlib.pyplot as plt

import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
#  Plot pie chart for specific student
#---------------------------------------------------------------------------------------------------------
def plotPieChart(dfStudent): 
    specificStudent=dfStudent[dfStudent['Name']=='Sagar'].iloc[0]
   
    print(BORDER)
    print(specificStudent)
    print(BORDER)

    subNames=['Math','Science','Science']
    subMarks=[specificStudent['Math'],specificStudent['Science'],specificStudent['English']]

    fig,ax=plt.subplots()
    ax.pie(subMarks,labels=subNames,autopct='%1.1f%%')
    plt.title("Sagar's Subject Marks")

    plt.show()
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    studentDF=updateDataFrame(studentDF,colName="Gender")
    #Plot a pie chart for student 'Sagar'
    plotPieChart(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()