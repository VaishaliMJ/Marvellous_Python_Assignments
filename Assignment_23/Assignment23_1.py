"""-----------------------------------------------------------------------------------------------------
                          Assignment23_1
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks and print basic information like shape,columns 
                   and data types 
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
BORDER="-"*50

#---------------------------------------------------------------------------------------------------------
#This function creates a student data frame
# Frame structure
# Data={'Name':['Amit','Sagar','Pooja'],
#       'Math':[85,90,78],
#       'Science':[92,88,80],
#       'English':[75,85,82]}
#---------------------------------------------------------------------------------------------------------
def createStudentData():

    studentDetails={'Name':['Amit','Sagar','Pooja'],
                       'Math':[85,90,78],'Science':[92,88,80],
                       'English':[75,85,82]}
    studentDF=pd.DataFrame(data=studentDetails)
    print(BORDER)
    print("Created Data Frame:")
    print(BORDER)

    print(studentDF)
    print(BORDER)
    return studentDF
#---------------------------------------------------------------------------------------------------------
#   This function displays all details of the created data frame
#---------------------------------------------------------------------------------------------------------
def displayStudentDFDetails(studentDF):

    print(f"Shape of Data Frame:{studentDF.shape}")
    print(BORDER)

    print(f"Data frame coulmns are:{studentDF.columns}")
    print(BORDER)

    print(f"Data types are:\n{studentDF.dtypes}")
    print(BORDER)
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    studentDF=createStudentData()
    displayStudentDFDetails(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()