"""-----------------------------------------------------------------------------------------------------
                          Assignment28
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about Wine type based on some features
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from seaborn import countplot
from matplotlib.pyplot import figure,show
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="WinePredictor.csv"
TARGET_COl="Class"
#####################################################################################################
#   Function Name   :   loadCSVData()
#   Description     :   Loads the data set from 'WinePredictor.csv' file
#   Input params    :   -
#   Output          :   Data frame
#####################################################################################################
def loadCSVData():
    """Read csv file"""
    dfWineClass=pd.read_csv(FILENAME)
    print(BORDER)
    print("Wine prediction data loaded successfully...")
    print(BORDER)
    """Printing shape and first few records"""
    print(dfWineClass.head())
    print(dfWineClass.shape)
    print(BORDER)
    return dfWineClass
#####################################################################################################
#   Function Name   :   cleanWineDataSet
#   Description     :   This method cleans data frame
#   Input Params    :   dfWineClass(wine classification data frame)
#   Output          :   Removes unwanted data from data frame
#####################################################################################################
def cleanWineDataSet(dfWineClass):
    #Remove unwanted data
    dfWineClass.dropna(inplace=True)
    print(BORDER)
    print("Wine class prediction data set after removing column")
    print(dfWineClass.head())
#####################################################################################################
#   Function Name   :   prepareDataset
#   Description     :   Prepare data by applying scalar transformation
#   Input params    :   dfWineClass(Wine classification data frame)
#   Output          :   Extracted Features and Labels
#####################################################################################################
def prepareDataset(dfWineClass):
    xFeatures=dfWineClass.drop(columns=[TARGET_COl])
    yLabel=dfWineClass[TARGET_COl]
    scalar=StandardScaler()
    x_scale=scalar.fit_transform(xFeatures)
    return x_scale,yLabel
#####################################################################################################
#  Function Name    :   TrainAndTestDataSet
#  Description      :   Train data set using Logistic regression algorithm
#  Input params     :   xIndependent(Features),yDependent(Label : Class)  
#  Output           :   Return model built                
#####################################################################################################
def TrainAndTestDataSet(xIndependent,yDependent):
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xIndependent,yDependent,test_size=0.3,random_state=42)
    """Build model using logistic regression"""
    model=LogisticRegression()
    """Fit model """
    model.fit(xTrainDS,yTrainDS)
    print("Model build successfully......")

    """Predict labels/Dependent variable"""
    yPredicted=model.predict(xTestDS)


    """Calculate Accuracy"""
    accuracy=metrics.accuracy_score(yTestDS,yPredicted)
    print(BORDER)

    print("Accuracy of Logistic Regression is ",accuracy*100)

    """Display confusion matrix"""
    confu_matrix=metrics.confusion_matrix(yTestDS,yPredicted)

    print("\n\nConfusion matrix:\n",confu_matrix)
    
    report=metrics.classification_report(yTestDS,yPredicted)
    print("\n\nClassification report is:")
    print(report)
    print(BORDER)

    return model
#####################################################################################################
#   Function Name   :   displayReport
#   Description     :   Features and label correlation
#   Input Params    :   dfWineClass
#   Output          :   Co-relation matrix
#####################################################################################################
def displayReport(dfWineClass):

    plt.figure(figsize=(10,6))
    sns.heatmap(dfWineClass.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature correclation heatmap")
    plt.show()
####################################################################################################
#   Function Name   :  testTrainedModelAndDisplay
#   Description     :  test and display results for individual models 
#   Input Params    :  dfWineClass Data Frame,model
#####################################################################################################
def testTrainedModelAndDisplay(dfWineClass,model):
    sampleTestData =dfWineClass.sample(n=1)
    print(BORDER)
    print(f"Selected sample data for testing is \n: {sampleTestData}")
    print(BORDER)

    result=['Class 1','Class 2','Class 3']
    predictedResult=model.predict(sampleTestData.drop(columns=[TARGET_COl]))
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)

#####################################################################################################
#   Function Name   :   predictWineClass
#   Description     :   Perform : Data loading,cleaning,Training and testing steps
#   Input Params    :   -
#   Output          :   Prediction of wine class
#####################################################################################################
def predictWineClass():

    """Step-1 : Get the data
    ------------------------------------------------------"""
    dfWineClass=loadCSVData()
    
    """Step-2 : Clean,Prepare and Manipulate the data
    #-----------------------------------------------------"""
    """clean,Prepare and Manipulate data
    Clean Data : drop unwanted columns"""
    cleanWineDataSet(dfWineClass)
    """Prepare Data set
    Extracting Independent and dependent variables"""

    xIndependent,yDependent=prepareDataset(dfWineClass)

    """Step-3 : Train and test data
    #--------------------------------------
    #Train data set """
    model=TrainAndTestDataSet(xIndependent,yDependent)

    """Display Actual Vs Predicted values"""
    displayReport(dfWineClass)
    """TestModel on sample data"""
    testTrainedModelAndDisplay(dfWineClass,model)

#####################################################################################################
#  Main function 
#####################################################################################################
def main():
    predictWineClass()
#####################################################################################################
#Main entry point of the program
#####################################################################################################
if __name__=="__main__":
    main()