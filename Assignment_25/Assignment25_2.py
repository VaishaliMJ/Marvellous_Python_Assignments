"""-----------------------------------------------------------------------------------------------------
                          Assignment25_2
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Detect column data type and convert 'Age' from float to int
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
BORDER="-"*50
#---------------------------------------------------------------------------------
#     Detect column data type and convert 'Age' from float to int
#---------------------------------------------------------------------------------
def findAndConvertColDataType():
    data={'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}
    dataFrame=pd.DataFrame(data)
    print(BORDER)
    print("Column Data Types")
    print(dataFrame.dtypes)
    print(BORDER)
    print("Original Data Frame")
    print(dataFrame)
    print(BORDER)

    
    dataFrame=dataFrame.astype({'Age': int})
    print(BORDER)
    print("Column After changing data type")
    print(BORDER)
    print(dataFrame)
    print(BORDER)
#---------------------------------------------------------------------------------
#  Main function calls findAndConvertColDataType() 
#---------------------------------------------------------------------------------------------------------
def main():
    findAndConvertColDataType()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()