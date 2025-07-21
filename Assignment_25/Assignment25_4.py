"""-----------------------------------------------------------------------------------------------------
                          Assignment25_4
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Apply one-hot encoding to a 'Department' column
---------------------------------------------------------------------------------------------------------"""                  
import pandas as pd
BORDER="-"*60
#---------------------------------------------------------------------------------
# This method converts categorical data into seperate binary coulmn
# Creates  a separate binary column for each category. 
# Creates seperate coulmn for HR,IT,Finanace with binary values
#---------------------------------------------------------------------------------

def oneHotEncoding():
    data={'Department':['HR','IT','Finance','HR','IT']}
    dfDept=pd.DataFrame(data)
    print(BORDER)
    print("Data before One-Hot encoding")
    print(BORDER)

    print(dfDept)
    print(BORDER)
    #One hot encoding method in pandas
    encodedDF=pd.get_dummies(dfDept,dtype="int")
    print(BORDER)
    print("Data after One-Hot encoding")
    print(BORDER)

    print(encodedDF)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls oneHotEncoding() 
#---------------------------------------------------------------------------------------------------------
def main():
    oneHotEncoding()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()