"""-----------------------------------------------------------------------------------------------------
                          Assignment 29
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains some medical parameters based on that predict 
                 for diabetes positive or negative
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
from matplotlib.pyplot import figure,show
import matplotlib.pyplot as plt
from seaborn import countplot
import seaborn as sns
from numpy import nan
from sklearn.model_selection import train_test_split

import matplotlib as mlt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
from sklearn.metrics import precision_score,recall_score,f1_score
from sklearn.preprocessing import StandardScaler

BORDER="-"*65
"""---------------------------------------------------------------------------------
#  Step - 1.1
#  This method loads the data set from 'diabetes.csv' file
#  Input params : Data file path
#  Output       : Data frame
#---------------------------------------------------------------------------------"""
def loadDataFile(dataFilePath):
    """Step-1.0  Load And read CSV data file
    ------------------------------------------------"""
    dfDiabetes=pd.read_csv(dataFilePath)
    print(BORDER)
    """Step 1.1 Display the first 5 rows.
    ------------------------------------------------""" 
    print("Diabetes prediction data loaded successfully...")
    print(BORDER)
    print(dfDiabetes.head())
    print(dfDiabetes.shape)
    print(BORDER)
    return dfDiabetes

"""---------------------------------------------------------------------------------
#  Step - 1.2, 1.3, 
#  This method loads the data set information
#  Input params : Data frame
#  Output       : Data statistics
#---------------------------------------------------------------------------------"""
def displayDatasetStatistics(dfDiabetes):
    
    """Step 1.2 Show column info and check for null values
    ------------------------------------------------""" 
    print("Diabetes dataset coulmns")
    print(BORDER)
    print(dfDiabetes.columns)
   
    dfDiabetes.dropna(inplace=True)

    print(BORDER)
    """Step 1.3 Display basic statistics using .describe()
    ------------------------------------------------"""
    print("Diabetes dataset Statistics")
    print(BORDER)
    print(dfDiabetes.describe())
    print(BORDER)
    
    return dfDiabetes
"""---------------------------------------------------------------------------------
Step 1.4 Plot the distribution of the target variable (Outcome).
#---------------------------------------------------------------------------------"""
def plotTargetVarDistribution(dfDiabetes):
    target="Outcome"
    countplot(data=dfDiabetes,x=target,width=0.4).set_title("Diabetic VS Non-Diabetic")
    show()
"""---------------------------------------------------------------------------------
Step 1.4 Plot the Co-relation matrix.
#---------------------------------------------------------------------------------"""
def displayCorrelationMatrix(dfDiabetes):
    plt.figure(figsize=(10,6))
    sns.heatmap(dfDiabetes.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature correclation heatmap")
    plt.show()

    
    plt.hist(dfDiabetes['Glucose'],bins=10,color="skyblue",edgecolor='black')
    plt.xlabel("Glucose")
    plt.ylabel("Frequncy")
    plt.title("Histogram for Glucose level")
    plt.show()

    #plt.figure()
    sns.pairplot(dfDiabetes,hue="Outcome")
    plt.show()

"""---------------------------------------------------------------------------------
Step : 2 Data Preprocessing
Input params :  dfDiabetes(Data frame set)
-----------------------------------------------------------------------------------"""
def dataPreProcessing(dfDiabetes):
    """Step 2.1 Check and handle missing or zero values"""
    missingValProcessing(dfDiabetes)
    """Step 2.2 Feature scaling using StandardScalar or minMaxScalar"""
    xIndependent,yDependent=scaleDataSet(dfDiabetes)
    return xIndependent,yDependent
"""---------------------------------------------------------------------------------
Step 2.1 Check and handle missing or zero values in columns like Glucose,blood pressure etc
Input params :  dfDiabetes(Data frame set)
-----------------------------------------------------------------------------------"""
def missingValProcessing(dfDiabetes):
    print("\t\tZero values in column report")
    print(BORDER)
    missingValuesDF={"ColName":[],"Missing Value Count":[]}
    for colName in dfDiabetes.columns:
        missingValCount=(dfDiabetes[colName]==0).sum()
        missingValuesDF['ColName'].append(colName)
        missingValuesDF["Missing Value Count"].append(missingValCount)
    
    print(pd.DataFrame(missingValuesDF))
    #dfDiabetes.drop(columns="Outcome",inplace=True)

    #dfDiabetes=dfDiabetes.replace(0,nan)
    #dfDiabetes.dropna(inplace=True)
    replaceZeroValCols=['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for colName in replaceZeroValCols:
        dfDiabetes[colName]=dfDiabetes[colName].replace(0,dfDiabetes[colName].mean())
    print(dfDiabetes)

    print(dfDiabetes.shape)
"""---------------------------------------------------------------------------------
    Standardising values using standard scalar
-----------------------------------------------------------------------------------"""
def scaleDataSet(dfDiabetes):
    x=dfDiabetes.drop(columns=['Outcome'])
    yDependent=dfDiabetes['Outcome']

    scalar=StandardScaler()
    x_scale=scalar.fit_transform(x)
    return x_scale,yDependent
#-----------------------------------------------------------------------------------
"""
Step-1
Exploratory Data Analysis (EDA):
    1.1 Load the dataset using pandas
    1.2 Show column info and check for null values
    1.3 Display basic statistics using .describe()
    1.4 Plot the distribution of the target variable (Outcome).
    1.5 Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
Step-2
    Data preprocessing
    2.1 Check and handle missing or zero values in columns like Glucose,blood pressure etc
    2.2 Apply feature scaling using standards scalar or min-max scalar
    2.3 Split the data set into features(x) and target(y)

"""
"""---------------------------------------------------------------------------------------------------------
This function perform EDA,pre-processing
---------------------------------------------------------------------------------------------------------"""

def GetBasicInformationDataSet():
    """Exploratory Data Analysis (EDA):
    Step 1.1.Load the dataset using pandas"""
    diabetesDF=loadDataFile("diabetes.csv")

    """Step 1.2,1.3 Get data set statistics """
    displayDatasetStatistics(diabetesDF)

    """Step 1.4 Plot the distribution of the target variable (Outcome).
    ------------------------------------------------"""
    plotTargetVarDistribution(diabetesDF)

    """Step 1.5 Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
    ------------------------------------------------"""
    displayCorrelationMatrix(diabetesDF)
    print(BORDER)

    """Step-2 Data preprocessing"""
    #"""Dropping columns 'BloodPressure' and 'SkinThickness' as they are less co-related"""
    #diabetesDF.drop(columns=['BloodPressure','SkinThickness'],inplace=True)

    xFeatures,yTarget=dataPreProcessing(diabetesDF)
    return diabetesDF,xFeatures,yTarget
"""---------------------------------------------------------------------------------------------------------
    This function uses 'Decision Tree Classifier' algorithm 
---------------------------------------------------------------------------------------------------------"""
def DiabetesPreditionUsingDecisionTreeAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Decision Tree Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Decision tree")

    #xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xFeatures,yTarget,test_size=0.2,random_state=42)
    decisionTreeModel=DecisionTreeClassifier()
    """Building the model"""
    decisionTreeModel.fit(xTrainDS,yTrainDS)
    """Predicted output """
    yPredictOutput=decisionTreeModel.predict(xTestDS)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput
"""---------------------------------------------------------------------------------------------------------
    This function uses does all accuracy calculations
    Input params : Test dataSet actual output,Predicted output,Dictionary for comparision
---------------------------------------------------------------------------------------------------------"""
def accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF):
    """Calculate Accuracy"""
   
    dsAccuracy=accuracy_score(yTestDS,yPredictOutput)
    print(BORDER)
    print("Accuracy is :",dsAccuracy)
    algorithmCompareDF["Accuracy Score"].append(dsAccuracy*100)

    """Calculate confusion Matrix """
    dsConfusionMatrix=confusion_matrix(yTestDS,yPredictOutput)
    print("Confusion Matrix is :\n",dsConfusionMatrix)
    algorithmCompareDF["Confusion Matrix"].append(dsConfusionMatrix)

    #precision    recall  f1-score   support
    print("Classification report...")
    print(BORDER)
    confusionMatrixReport=classification_report(yTestDS,yPredictOutput)
    print(confusionMatrixReport)
    #algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[],"Recall":[],"F1 Score":[]}
    algorithmCompareDF["Recall"].append(recall_score(yTestDS,yPredictOutput))
    algorithmCompareDF["F1 Score"].append(f1_score(yTestDS,yPredictOutput))
    algorithmCompareDF["Precision"].append(precision_score(yTestDS,yPredictOutput))

"""---------------------------------------------------------------------------------------------------------
    This function uses KNN algorithm
---------------------------------------------------------------------------------------------------------"""
def DiabetesPreditionUsingKNNAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,k=3):
    print(BORDER)
    print("Calculations using KNN Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("KNN")

    #xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xFeatures,yTarget,test_size=0.2,random_state=42)
    kNNModel=KNeighborsClassifier(n_neighbors=k)
    """Bulding the model"""
    kNNModel.fit(xTrainDS,yTrainDS)
    """Testing phase"""
    yPredictOutput=kNNModel.predict(xTestDS)
    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput
"""---------------------------------------------------------------------------------------------------------
    This function uses Logistic Regression algorithm
---------------------------------------------------------------------------------------------------------"""
def DiabetesPreditionUsingLogisticRegressionAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Logistic Regression Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Logistic Regression")

    #xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xFeatures,yTarget,test_size=0.2,random_state=42)
    logModel=LogisticRegression()
    """Build the model"""
    logModel.fit(xTrainDS,yTrainDS)
    """Testing the model"""
    yPredictOutput=logModel.predict(xTestDS)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)

    return yPredictOutput

"""---------------------------------------------------------------------------------------------------------
    comparision based on accuracy
---------------------------------------------------------------------------------------------------------"""
def plotBasedOnAccuracy(algorithmCompareDF,actualVsPredicted):
    x=algorithmCompareDF['Algorithm Name']
    y=algorithmCompareDF['Accuracy Score']
    plt.bar(x,y,width=0.4)
    plt.title('Accuracy of algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.show()

    """Create the figure and subplots
    As we used 3 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt], 
                                             display_labels=["Diabetic","Non Diabetic"])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()

    print(actualVsPredicted.head())
    actualVsPredicted.to_csv("ActualPredictedResult.csv")
    

"""---------------------------------------------------------------------------------------------------------
    Comparing Algorithms 
---------------------------------------------------------------------------------------------------------"""
def compareClassificationAlgorithms():
    diabetesDF,xFeatures,yTarget=GetBasicInformationDataSet()
    print("Updated dataset values....")
    print(BORDER)
    print(diabetesDF)
    print(diabetesDF.shape)
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xFeatures,yTarget,test_size=0.2,random_state=42)

    algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[], "Precision":[],"Recall":[],"F1 Score":[]}
    yPredictDT=DiabetesPreditionUsingDecisionTreeAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
    
    yPredictKNN=DiabetesPreditionUsingKNNAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,5)
    
    yPredictLR=DiabetesPreditionUsingLogisticRegressionAlgorithm(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
    actualVsPredicted={"Y Actual":yTestDS,
                       "Decision Tree Predicted":yPredictDT,
                       "KNN Predcited":yPredictKNN,
                       "Logistic Regression Predicted":yPredictLR}

    # actualVsPredicted["Y Actual"]=yTestDS
    # actualVsPredicted["Decision Tree Predicted"]=yPredictDT
    # actualVsPredicted["KNN Predcited"]=yPredictKNN
    # actualVsPredicted["Logistic Regression Predicted"]=yPredictLR


    #print(pd.DataFrame(algorithmCompareDF).to_csv("AlgorithmComparision.csv"))
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_colwidth', 5)

    print(BORDER)
    print("\t\tComparision matrix for all algorithm....")
    print(BORDER)
    algoDetails=pd.DataFrame(algorithmCompareDF)
    print(algoDetails)
    print("Predicted....")
    predictedDF=pd.DataFrame(actualVsPredicted)
    print(BORDER)
    """Plotting comparision"""
    plotBasedOnAccuracy(algoDetails,predictedDF)
    
#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    compareClassificationAlgorithms()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()