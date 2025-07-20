"""-----------------------------------------------------------------------------------------------------
                          Assignment23_7
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 
                   7. Create a bar plot Student Name vs Total Marks

---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import matplotlib.pyplot as plt
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
import Assignment23_5 as replacedDF

BORDER="-"*50

#---------------------------------------------------------------------------------------------------------
# Create a bar plot Student Name vs Total Marks
#---------------------------------------------------------------------------------------------------------
def plotStudentNameVsTotalMarks(df_student):
    plt.figure(figsize=(8,6))
    plt.bar(df_student["Name"],height=df_student["Total"],width=0.2,edgecolor='k',color="cyan")
    plt.title("Student Total Marks Graph")
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.grid(True)
    plt.show()
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replacedDF.replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
    
    #Plot a Graph
    plotStudentNameVsTotalMarks(studentDF)

#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()