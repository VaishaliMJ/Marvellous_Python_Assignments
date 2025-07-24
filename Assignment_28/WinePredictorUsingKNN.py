"""-----------------------------------------------------------------------------------------------------
                          Assignment28
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about Wine type based on some features
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from seaborn import countplot
from matplotlib.pyplot import figure,show


BORDER="-"*65
"""---------------------------------------------------------------------------------
#  This method loads the data set from 'WinePredictor.csv' file
#  Input params : Data file path
#  Output : Data frame
#---------------------------------------------------------------------------------"""
def loadCSVData(dataFilePath):
    dfWineClass=pd.read_csv(dataFilePath)
    
    print(BORDER)
    print("Wine prediction data loaded successfully...")
    print(BORDER)
    print(dfWineClass.head())
    print(dfWineClass.shape)
    print(BORDER)
    return dfWineClass
"""---------------------------------------------------------------------------------
#  This method cleans data frame
#  input Params :  dfWineClass(wine classification data frame)
#  Removes unwanted data from data frame
#---------------------------------------------------------------------------------"""
def cleanWineDataSet(dfWineClass):
    #Remove unwanted data
    dfWineClass.dropna(inplace=True)
    print(BORDER)
    print("Wine class prediction data set after removing column")
    print(dfWineClass.head())
"""---------------------------------------------------------------------------------
# Prepare data by applying scalar transformation
# Input params: dfWineClass(Wine classification data frame)
#---------------------------------------------------------------------------------"""
def prepareDataset(dfWineClass):
    xFeatures=dfWineClass.drop(columns=['Class'])
    yLabel=dfWineClass['Class']
    scalar=StandardScaler()
    x_scale=scalar.fit_transform(xFeatures)
    return x_scale,yLabel
"""---------------------------------------------------------------------------------------------------------
#  Train data set using KNN algorithm
#  Input params : xIndependent
#                 yDependent(Label : Class)  
#  Output : Return model built                
#---------------------------------------------------------------------------------------------------------"""
def TrainAndTestDataSet(xIndependent,yDependent):
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xIndependent,yDependent,test_size=0.3,random_state=42)
    """Build model using KNN regression"""
    model=KNeighborsClassifier()
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

    return yTestDS,yPredicted

"""---------------------------------------------------------------------------------------------------------
# This method checks the accuracy of the model for various 'K' values
# Input Params : Features and Labels
#---------------------------------------------------------------------------------------------------------"""

def checkAccuracy(xIndependent,yDependent):
    print("Checking model accuracy......")
    print("Dividing Data set into train And Test data set")
    print(BORDER)
    
    """Splitting the data set in Training """
    x_train,x_test,y_train,y_test=train_test_split(xIndependent,yDependent,test_size=0.3,random_state=42)
        
    """Creating dictionary for {k,Accuracy} values"""
    accuracyScoreDict={'k':[],'accuracy':[]}
    """Selcting range values for 'k'"""
    k_range=range(1,22)
    for k in k_range:
        
        """Build model for various values of K"""
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)

        """Predicting test data values"""
        y_predict=model.predict(x_test)

        """Calculating Accuracy Values"""
        accuracy=metrics.accuracy_score(y_test,y_predict)
        """Storing 'k' and 'Accuracy' values in dictionary"""
        accuracyScoreDict['k'].append(k)
        accuracyScoreDict['accuracy'].append(accuracy*100)
        
    print(BORDER)    
    print("Accuracy Scores are :")
    print(BORDER)    
    accuracyDF=pd.DataFrame(accuracyScoreDict)
    print(accuracyDF)

    best_k=k_range[accuracyScoreDict["accuracy"].index(max(accuracyScoreDict["accuracy"]))]
    best_Accuracy=max(accuracyScoreDict["accuracy"])

    print("Best value of k is :",best_k) 
    print("Accuracy is  :",best_Accuracy) 
    cm=metrics.confusion_matrix(y_test,y_predict)
    print("Confusion matrix :\n",cm)
   
    """Plot accuracy points"""
    plotAccuracyGraph(accuracyDF)

"""#---------------------------------------------------------------------------------------------------------
#Plotting Accuracy VS 'K' value model
#---------------------------------------------------------------------------------------------------------"""  
def plotAccuracyGraph(accuracyDF):  
    plt.figure(figsize=(8,5))
    plt.plot(accuracyDF["k"],accuracyDF['accuracy'],marker='o',linestyle="--")

    plt.title("Accuracy VS K Value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(accuracyDF["k"])
"""---------------------------------------------------------------------------------------------------------
#   Features and label correlation
#---------------------------------------------------------------------------------------------------------"""
def displayReport(y_testDS,yPredicted,dfWineClass):

    plt.figure(figsize=(10,6))
    sns.heatmap(dfWineClass.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature correclation heatmap")
    plt.show()

"""---------------------------------------------------------------------------------------------------------
#   Perform : Data loading,cleaning,Training and testing steps
#----------------------------------------------------------------------------------------------------------"""
def predictWineClass():

    """Step-1 : Get the data
    ------------------------------------------------------"""
    dfWineClass=loadCSVData("WinePredictor.csv")
    
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
    yTestDS,yPredicted=TrainAndTestDataSet(xIndependent,yDependent)
    """Check Accuracy"""
    checkAccuracy(xIndependent,yDependent)

    """Display Actual Vs Predicted values"""
    displayReport(yTestDS,yPredicted,dfWineClass)
#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    predictWineClass()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()