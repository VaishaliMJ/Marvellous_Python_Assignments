"""-----------------------------------------------------------------------------------------------------
                          Assignment23_9
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 
                   9. Create a data frame with missing values and fill them with coulmn mean 
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
import Assignment23_5 as replacedDF

BORDER="-"*50


#---------------------------------------------------------------------------------------------------------
#  This function creates a data frame with missing values
#  Fills missing values with coulmn mean
#---------------------------------------------------------------------------------------------------------    
def createMissingValueDfFillWithMeanCol():
    #Create dictionary
    studentDict={'Name':['Amit','Sagar','Pooja'],'Math':[np.nan,76,88],'Science':[91,np.nan,85]}
    #create data frame using pandas DataFrame() method
    student_dataFrame=pd.DataFrame(data=studentDict)
    print(BORDER)
    print("\t\tSTUDENT DETAILS")
    print(BORDER)
    #Print data frame
    print(student_dataFrame.head())
    print(BORDER)  

    student_dataFrame['Math']=student_dataFrame['Math'].fillna(student_dataFrame['Math'].mean())
    student_dataFrame['Science']=student_dataFrame['Science'].fillna(student_dataFrame['Science'].mean())

    print(BORDER)
    print("\t\tUpdated Student Details")
    print(BORDER)
    #Print data frame
    print(student_dataFrame.head())
    print(BORDER)  
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replacedDF.replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
    
    #Create a second data frame with missing values and fill values with coulmn mean
    createMissingValueDfFillWithMeanCol()

#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()