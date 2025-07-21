"""-----------------------------------------------------------------------------------------------------
                          Assignment25_3
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Apply label encoding to 'City' coulmn
---------------------------------------------------------------------------------------------------------"""                  
from sklearn import preprocessing
import pandas as pd
BORDER="-"*60
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------

def labelEncoding():
    data={'City':['Pune','Mumbai','Delhi','Pune','Delhi']}
    dfCity=pd.DataFrame(data)
    print(BORDER)
    print("Data before encoding")
    print(BORDER)

    print(dfCity)
    print(BORDER)

    labelEncoder = preprocessing.LabelEncoder()
    dfCity['City']=labelEncoder.fit_transform(dfCity['City'])
    dfCity['City'].unique()
    print(BORDER)
    print("Data after encoding")
    print(BORDER)

    print(dfCity)
    print(BORDER)
#---------------------------------------------------------------------------------
#  Main function calls labelEncoding() 
#---------------------------------------------------------------------------------------------------------
def main():
    labelEncoding()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()