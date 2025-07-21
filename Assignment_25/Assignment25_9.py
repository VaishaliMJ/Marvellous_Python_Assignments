"""-----------------------------------------------------------------------------------------------------
                          Assignment25_9
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Replace values in 'Marks' column less than 50 with 'Fail' using where()
---------------------------------------------------------------------------------------------------------"""                  
import numpy as np
import pandas as pd

BORDER="-"*50
#---------------------------------------------------------------------------------
# Create Marks data and replace using where() method
#---------------------------------------------------------------------------------
def replaceLessThan50Marks():
    data={'Marks':[45,67,88,32,76]}

    marksDF=pd.DataFrame(data)
    print("\n Data Frame")
    print(BORDER)
    print(marksDF)
    print(BORDER)
    
    marksDF.where(marksDF['Marks']>50,other="Fail",inplace=True)

    print("\nChanged Data Frame:")
    print(BORDER)
    print(marksDF)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls replaceLessThan50Marks() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Replace "Marks' Column values using where clause
    replaceLessThan50Marks()
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()