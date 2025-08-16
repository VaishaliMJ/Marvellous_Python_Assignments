"""-----------------------------------------------------------------------------------------------------
                          Assignment27
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about Advertisement agenecy
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="Advertising.csv"
TARGET_COl="sales"
#####################################################################################################
#   Function Name   :   loadCSVData
#   Description     :   This method loads the data set from 'Advertising.csv' file
#   Input params    :    -
#   Output          :    Data frame
#####################################################################################################
def loadCSVData():
    dfSales=pd.read_csv(FILENAME)
    
    print(BORDER)
    print("Adverstise Sales data loaded successfully...")
    print(BORDER)
    print(dfSales.head())
    print(dfSales.shape)
    print(BORDER)
    return dfSales
#####################################################################################################
#   Function Name   :   cleanSalesDataSet
#   Description     :   This method cleans data frame
#   Input Params    :   dfSales(sales data frame)
#####################################################################################################
def cleanSalesDataSet(dfSales):
    #Drop unwanted coulmns : 'Unnamed: 0'
    dfSales.drop(columns=['Unnamed: 0'],inplace=True)
    #Remove unwanted data
    dfSales.dropna(inplace=True)
    print(BORDER)
    print("Sales data set after removing column")
    print(dfSales.head())
#####################################################################################################
#   Function Name   :   extractFeaturesAndLabel
#   Description     :   Extracting Features/Independent and Label/Dependent variables
#   Input params    :   dfSales(Sales data Frame)
#   Output          :   xIndependent,yDependent variables
#####################################################################################################
def extractFeaturesAndLabel(dfSales):
    xIndependent=dfSales.drop(columns=[TARGET_COl])
    yDependent=dfSales[TARGET_COl]
    return xIndependent,yDependent
#####################################################################################################
#   Function Name   :   TrainAndTestDataSet
#   Desription      :   Train data set using linear regression algorithm
#   Input params    :   xIndependent(Features : TV,Radio,NewsPapaer)
#                       yDependent(Label : sales)  
#   Output          :   Return model built                
#####################################################################################################
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
    return y_testDS,yPredicted,salesModel
#####################################################################################################
#   Function Name   :   displayPredictedVsActualSales
#   Description     :   Display Actual Result vs Predicted Result
#   Input Params    :   Actual and Predicted values
#####################################################################################################
def displayPredictedVsActualSales(y_testDS,yPredicted):
    print(BORDER)
    print("\t\tActual Vs Predicted Sales Values")
    dfTest=pd.DataFrame({"Actual Sale":y_testDS,"Predicted Sales":yPredicted})
    print(BORDER)
    print(dfTest)
    print(BORDER)
#####################################################################################################
#   Function Name   :   plotSalesReport
#   Description     :   Plot Actual Result vs Predicted Result
#   Input Params    :   Actual and Predicted values
#####################################################################################################
def plotSalesReport(y_testDS,yPredicted):
    plt.figure(figsize=(8,5))
    plt.scatter(y_testDS,yPredicted,color="blue")
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Advertising sales report")
    plt.grid(True)
    plt.show()
####################################################################################################
#   Function Name   :  testTrainedModelAndDisplay
#   Description     :  test and display results for individual models 
#   Input Params    :  dfSales Data Frame,model
#####################################################################################################
def testTrainedModelAndDisplay(dfSales,model):
    sampleTestData =dfSales.sample(n=1)
    print(BORDER)
    print(f"Selected sample data for testing is \n: {sampleTestData}")
    print(BORDER)
    predictedResult=model.predict(sampleTestData.drop(columns=[TARGET_COl]))
    print(f"Loaded model prediction for randomly selected test sample:{predictedResult[0]}")
    print(BORDER)    

#####################################################################################################
#   Function Name   :   AdvertiseSalesReport
#   Description     :   Perform : Data loading,cleaning,Training and testing steps
#   Input Params    :   -
#####################################################################################################
def AdvertiseSalesReport():
    """Step-1 : Get the data
    ------------------------------------------------------"""
    salesDF=loadCSVData()
    
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
    y_testDS,yPredicted,model=TrainAndTestDataSet(xIndependent,yDependent)
    """Displaying actual vs predicted sales report"""
    displayPredictedVsActualSales(y_testDS,yPredicted)
    """Plot Sales report"""
    plotSalesReport(y_testDS,yPredicted)
    """TestModel on sample data"""
    testTrainedModelAndDisplay(salesDF,model)
#####################################################################################################
#  Main function 
#####################################################################################################
def main():
    AdvertiseSalesReport()
#####################################################################################################
#Main entry point of the program
#####################################################################################################
if __name__=="__main__":
    main()