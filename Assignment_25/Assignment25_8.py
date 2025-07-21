"""-----------------------------------------------------------------------------------------------------
                          Assignment25_8
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Fill missing values in a numeric column using interpolation
---------------------------------------------------------------------------------------------------------"""                  
import numpy as np
import pandas as pd

BORDER="-"*50
#---------------------------------------------------------------------------------
# Create salary Data
#---------------------------------------------------------------------------------
def fillMissingValues():
    data={'Marks':[85,np.nan,90,np.nan,95]}

    marksDF=pd.DataFrame(data)
    print("\n Data Frame before interpolation:")
    print(BORDER)
    print(marksDF)
    print(BORDER)
    # Interpolate missing values
    marksDF_interpolated = marksDF.interpolate()

    print("\nInterpolated DataFrame:")
    print(BORDER)
    print(marksDF_interpolated)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls fillMissingValues() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Detect fill Missing Values in data
    fillMissingValues()
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()