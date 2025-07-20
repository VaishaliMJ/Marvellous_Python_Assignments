"""-----------------------------------------------------------------------------------------------------
                          Assignment24_1
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks .Normalize the 'Math' scores using Min-Max Scaling
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
#  This function Normalise the 'Math' scores using Min-Max Scaling
#---------------------------------------------------------------------------------------------------------
def normaliseColumn(studentDF,colName):
    #studentDF['Math']=(studentDF['Math']-studentDF['Math'].min())/(studentDF['Math'].max()-studentDF['Math'].min())
    studentDF[colName]=(studentDF[colName]-studentDF[colName].min())/(studentDF[colName].max()-studentDF[colName].min())

    print(BORDER)
    print("Normalised Data Frame")
    print(studentDF)
    print(BORDER)
    #return studentDF
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    #Normalise Math column
    normaliseColumn(studentDF,colName='Math')
    print(studentDF)
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()