"""-----------------------------------------------------------------------------------------------------
                          Assignment25_1
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Detect 'Outliers' in the salary column using IQR method
---------------------------------------------------------------------------------------------------------"""                  
import numpy as np
import pandas as pd

BORDER="-"*50
#---------------------------------------------------------------------------------
# Create salary Data
#---------------------------------------------------------------------------------
def detectOutliers():
    data={'Salary':[25000,27000,29000,31000,50000,100000]}

    dfSalary=pd.DataFrame(data)

    Q1 = dfSalary['Salary'].quantile(0.25)
    Q3 = dfSalary['Salary'].quantile(0.75)
    #Calculate Interquartile Range (IQR)

    iqrSal = Q3 - Q1
    print("IQR Value:",iqrSal)

    below25Per = Q1 - 1.5*iqrSal
    above75Per = Q3 + 1.5*iqrSal
    
    lower_bound = dfSalary[dfSalary['Salary'] < below25Per]
    upper_bound = dfSalary[dfSalary['Salary'] > above75Per]

    print("Lower bound is:",below25Per)
    print("Upper Bound is :",above75Per)
    print(BORDER)
    print("\nOutliers are:")
    print(BORDER)

    print(lower_bound)
    print(upper_bound)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls detectOutliers() 
#---------------------------------------------------------------------------------------------------------
def main():
    #Detect outliers in data
    detectOutliers()
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()