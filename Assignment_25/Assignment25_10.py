"""-----------------------------------------------------------------------------------------------------
                          Assignment25_10
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Split a DataFrame with mutiple features into train-test for supervised learning
---------------------------------------------------------------------------------------------------------"""                  
from sklearn.model_selection import train_test_split
import pandas as pd

BORDER="-"*50
#---------------------------------------------------------------------------------
# split Data Set
#---------------------------------------------------------------------------------
def splitDataSet():
    data={'Age':[25,20,45,35,22],'Salary':[50000,60000,80000,65000,45000],'Purchased':[1,0,1,0,1]}

    df=pd.DataFrame(data)
    print("\n Data Frame")
    print(BORDER)
    print(df)
    print(BORDER)
    xFeatures=df[['Age','Salary']]
    yLabel=df['Purchased']
    x_train,x_test,y_train,y_test=train_test_split(xFeatures,yLabel,test_size=0.2)


    print("\nInput Trained Data set:")
    print(BORDER)
    print(x_train)
    print(BORDER)

    print("\nOutput Data set:")
    print(BORDER)
    print(y_train)
    print(BORDER)

    print("\nTest Data set:")
    print(BORDER)
    print(x_test)
    print(BORDER)

    print("\nActual Output Data set:")
    print(BORDER)
    print(y_test)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls splitDataSet() 
#---------------------------------------------------------------------------------------------------------
def main():
    #split data set 
    splitDataSet()
    
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()