"""-----------------------------------------------------------------------------------------------------
                          Assignment23_5
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: 5. Replace "Pooja" with "Puja" in "Name" coulmn
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd

import Assignment23_3 as studDF
import Assignment23_1 as createStudDF
BORDER="-"*50
#---------------------------------------------------------------------------------------------------------
# Replace Student name with new name
#---------------------------------------------------------------------------------------------------------    
def replaceStudentName(df_student,oldName,newName):
    df_student['Name']=df_student["Name"].replace(oldName,newName)
    print("\t\tUpdated Student Name Details")
    print(BORDER)
    print(f"\nReplaced Student Name '{oldName}' with '{newName}'")
    print(BORDER)

    print(df_student)
    return df_student
#---------------------------------------------------------------------------------------------------------
#  Main function calls createStudentData() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Create student data frame
    studentDF=studDF.updateDataFrame(createStudDF.createStudentData())
    #Replace old Name with new name
    studentDF=replaceStudentName(studentDF,oldName="Pooja",newName="Puja")
#---------------------------------------------------------------------------------------------------------
# Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()