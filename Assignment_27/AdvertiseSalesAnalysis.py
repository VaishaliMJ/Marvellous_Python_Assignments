"""-----------------------------------------------------------------------------------------------------
                          Assignment27
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about Advertisement agenecy
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

BORDER="-"*60
"""---------------------------------------------------------------------------------
#  This method loads the data set from 'Advertising.csv' file
#  Input params : Data file path
#  Output : Data frame
#---------------------------------------------------------------------------------"""
def loadCSVData(dataFilePath):
    dfSales=pd.read_csv(dataFilePath)
    
    print(BORDER)
    print("Adverstise Sales data loaded successfully...")
    print(BORDER)
    print(dfSales.head())
    print(dfSales.shape)
    print(BORDER)
    return dfSales
"""---------------------------------------------------------------------------------
#  This method cleans data frame
#  input Params :  dfSales(sales data frame)
#  Removes unwanted data and coulmns from data frame
#---------------------------------------------------------------------------------"""
def cleanSalesDataSet(dfSales):
    #Drop unwanted coulmns : 'Unnamed: 0'
    dfSales.drop(columns=['Unnamed: 0'],inplace=True)
    #Remove unwanted data
    dfSales.dropna(inplace=True)
    print(BORDER)
    print("Sales data set after removing column")
    print(dfSales.head())
"""---------------------------------------------------------------------------------------------------------
# Extracting Features/Independent and Label/Dependent variables
# Input params: dfSales(Sales data Frame)
# Output : xIndependent,yDependent variables
#-------------------------------------------------------------------------------------------------------"""
def extractFeaturesAndLabel(dfSales):
    xIndependent=dfSales.drop(columns=['sales'])
    yDependent=dfSales['sales']
    return xIndependent,yDependent
"""---------------------------------------------------------------------------------------------------------
#  Train data set using linear regression algorithm
#  Input params : xIndependent(Features : TV,Radio,NewsPapaer)
#                 yDependent(Label : sales)  
#  Output : Return model built                
#---------------------------------------------------------------------------------------------------------"""
def TrainAndTestDataSet(xIndependent,yDependent):
    #Using Linear Regression algorithm
    salesModel=LinearRegression()
    #Fit model
    """Split data set """
    x_trainDS,x_testDS,y_trainDS,y_testDS=train_test_split(xIndependent,yDependent,test_size=0.5,random_state=42)
    """Training data set"""
    salesModel.fit(x_trainDS,y_trainDS)
    """Predict 'y:Sales Values"""
    yPredicted=salesModel.predict(x_testDS)
    """Calculate Mean squared error and model coefficient,intercept"""

    meanSquaredError=metrics.mean_squared_error(y_testDS,yPredicted)
    rootMeanSquaredError=np.sqrt(meanSquaredError)
    rSquare=metrics.r2_score(y_testDS,yPredicted)
    print(BORDER)
    print("\nDisplaying model details of Error,coefficient and intercept")
    print(BORDER)

    print("\n\nMean squared error:",meanSquaredError)
    print("\n\nRoot mean squared error:",rootMeanSquaredError)
    print("\n\nR Square:",rSquare)

    print("\n\nModel coefficent are:",salesModel.coef_)
    print("\n\nModel Intercept are:",salesModel.intercept_)
    print(BORDER)
    print("\nColumn wise model coefficient are:")
    print(BORDER)
    for col,coef in zip(xIndependent.columns,salesModel.coef_):
        print(f"\n{col} : {coef}")

    #print("\n\nIntercept :",salesModel.intercept_)
    return y_testDS,yPredicted
"""---------------------------------------------------------------------------------------------------------
#   Display Actual Result vs Predicted Result
#---------------------------------------------------------------------------------------------------------"""
def displayPredictedVsActualSales(y_testDS,yPredicted):
    print(BORDER)
    print("\t\tActual Vs Predicted Sales Values")
    dfTest=pd.DataFrame({"Actual Sale":y_testDS,"Predicted Sales":yPredicted})
    print(BORDER)
    print(dfTest)
    print(BORDER)
"""---------------------------------------------------------------------------------------------------------
#   Plot Actual Result vs Predicted Result
#---------------------------------------------------------------------------------------------------------"""
def plotSalesReport(y_testDS,yPredicted):
    plt.figure(figsize=(8,5))
    plt.scatter(y_testDS,yPredicted,color="blue")
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Advertising sales report")
    plt.grid(True)
    plt.show()
"""---------------------------------------------------------------------------------------------------------
#   Perform : Data loading,cleaning,Training and testing steps
#---------------------------------------------------------------------------------------------------------"""
def AdvertiseSalesReport():
    """Step-1 : Get the data
    ------------------------------------------------------"""
    salesDF=loadCSVData("Advertising.csv")
    
    """Step-2 : Clean,Prepare and Manipulate the data
    #-----------------------------------------------------"""
    """clean,Prepare and Manipulate data
    Clean Data : drop unwanted columns"""
    cleanSalesDataSet(salesDF)

    """Step-3 And Step 4 : Train and Test data
    ------------------------------------------------------
    Extracting Independent and dependent variables"""
    xIndependent,yDependent=extractFeaturesAndLabel(salesDF)
    """Train and Test data set"""
    y_testDS,yPredicted=TrainAndTestDataSet(xIndependent,yDependent)
    """Displaying actual vs predicted sales report"""
    displayPredictedVsActualSales(y_testDS,yPredicted)
    """Plot Sales report"""
    plotSalesReport(y_testDS,yPredicted)

#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    AdvertiseSalesReport()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()