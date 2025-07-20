"""-----------------------------------------------------------------------------------------------------
                          Assignment23_8
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 8. Plot a line chart for 'Amit' across all the subjects

---------------------------------------------------------------------------------------------------------"""                  
import matplotlib.pyplot as plt
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
import Assignment23_5 as replacedDF
import seaborn as sns
BORDER="-"*50

#---------------------------------------------------------------------------------------------------------
# Plot line chart for particular student
#---------------------------------------------------------------------------------------------------------
def plotLineChartForParticularStudent(df_student,nameCol,studentName):
    specificStudent=df_student[df_student[nameCol].str.contains(studentName)]
    print(f"'{studentName}'s' data:",specificStudent)
    xCoordinates=[specificStudent['Math'].name,specificStudent['Science'].name,specificStudent['English'].name]
    yCoordinates=[specificStudent['Math'][0],specificStudent['Science'][0],specificStudent['English'][0]]
    
    plt.figure(figsize=(8,6))
    plt.title(f"'{studentName}'s' subject wise mark analysis")
    plt.plot(xCoordinates,yCoordinates)
    plt.xlabel("Subject Name")
    plt.ylabel("Marks Obtained")
    plt.grid(True)
    plt.show()

    #plt.plot()
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replacedDF.replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
    
    #Plot a line chart for student "Amit" across all subjects
    plotLineChartForParticularStudent(studentDF,nameCol='Name',studentName="Amit")
#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()