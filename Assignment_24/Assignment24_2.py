"""-----------------------------------------------------------------------------------------------------
                          Assignment24_2
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a Dataframe for students marks.
                    Add a new Column 'Gender' and add one-hot encoding 
---------------------------------------------------------------------------------------------------------"""                  
from Assignment24_1 import createStudentData
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
#  This function Normalise the 'Math' scores using Min-Max Scaling
#  input parameters   :   Data Frame,New Column Name 
#---------------------------------------------------------------------------------------------------------
def updateDataFrame(dfStudent,colName):        #"colName=Gender"
    #Added new Coulmn
    dfStudent[colName]=['Male','Male','Female']
    print(BORDER)
    print("\tData Frame")
    print(dfStudent)
    #One Hot Encoding
    dfStudent[colName]=dfStudent[colName].map({'Male':1,'Female':2})   
    print(BORDER)
    print("\tUpdated Data Frame")
    print(dfStudent)
    print(BORDER)
    return dfStudent
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create data frame
    studentDF=createStudentData()
    #Add coulmn Gender
    studentDF=updateDataFrame(studentDF,colName="Gender")
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()