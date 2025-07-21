"""-----------------------------------------------------------------------------------------------------
                          Assignment25_5
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Create a DataFrame with 'Age' and 'Purchased' columns and split inti train/test sets
---------------------------------------------------------------------------------------------------------"""                  
from sklearn.model_selection import train_test_split
import pandas as pd
BORDER="-"*60
#---------------------------------------------------------------------------------
# Create a DataFrame with 'Age' and 'Purchased' columns 
#  split inti train/test sets
#---------------------------------------------------------------------------------

def dataProcessing():
    data={'Age':[22,25,47,52,46,56],'Purchased':[0,1,1,0,1,0]}
    dfPurchase=pd.DataFrame(data)

    x_independent=dfPurchase['Age']
    y_dependent=dfPurchase['Purchased']
    print(BORDER)
    print("Data Before spliting")
    print(dfPurchase)
    print(BORDER)
    
    print(BORDER)
    print("Data after spliting")
    print(BORDER)
    x_train,x_test,y_train,y_test=train_test_split(x_independent,y_dependent,test_size=0.2,random_state=42)
    print("Independent Input Train data set:")
    print(BORDER)
    print(x_train)
    print("Output Train data set:")
    print(y_train)
    print(BORDER)
    print("Test Data set:")
    print(x_test)
    print("Actual Output")
    print(y_test)
    print(BORDER)

#---------------------------------------------------------------------------------
#  Main function calls dataProcessing() 
#---------------------------------------------------------------------------------------------------------
def main():
    dataProcessing()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()