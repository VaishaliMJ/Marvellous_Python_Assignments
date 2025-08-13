"""-----------------------------------------------------------------------------------------------------
                          Assignment 29
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains some medical parameters based on that predict 
                 for diabetes positive or negative
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure,show
import matplotlib.pyplot as plt
from seaborn import countplot
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from pathlib import Path
import joblib   #preserve model
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="diabetes.csv"
TEST_SIZE=0.2
RANDOM_STATE=42
ARTIFACTS=Path("diabetes_sample")
ARTIFACTS.mkdir(exist_ok=True)
MODEL_PATH=ARTIFACTS / 'diabetes_pipeline.joblib'
#####################################################################################################
#  Function Name : load_Data_File
#  Description   : This method loads the data set from 'diabetes.csv' file
#  Input params  : Data file path
#  Output        : Data frame
#####################################################################################################
def load_Data_File(dataFilePath):
    try:
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
    except FileNotFoundError as ex:
        print(f"File not found {dataFilePath}")
        exit()
#####################################################################################################
#  Function Name : display_Dataset_Statistics
#  Description   : This method loads the data set information
#  Input params  : Data frame
#  Output        : Data statistics
#####################################################################################################
def display_Dataset_Statistics(dfDiabetes):
    
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
#####################################################################################################
#  Function Name : Plot_Features_Target_Distribution
#  Description   : Plot the distribution of the target variable (Outcome).
#  Input params  : Data frame
#  Output        : Displays the Diabetes vs Non diabetes
#####################################################################################################
def plot_Features_Target_Distribution(dfDiabetes):
    target="Outcome"
    countplot(data=dfDiabetes,x=target,width=0.4).set_title("Diabetic VS Non-Diabetic")
    show()
#####################################################################################################
#  Function Name :  display_Correlation_Matrix
#  Description   :  Plot the Co-relation matrix.
#  Input         :   Data Frame
#  Output        :   Displays Co-Relation of features and target 
#####################################################################################################
def display_Correlation_Matrix(dfDiabetes):
    plt.figure(figsize=(10,6))
    """Heat Map to show co-relation matrix"""
    sns.heatmap(dfDiabetes.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()

    sns.pairplot(dfDiabetes,hue="Outcome")
    plt.show()

#####################################################################################################
#   Function Name : dataPreProcessing
#   Dscription    : Data Preprocessing,like na and missing values
#   Input params  : dfDiabetes(Data frame set)
#   Output        : Updated Data frame
#####################################################################################################
def dataPreProcessing(dfDiabetes):
    """Step 2.1 Check and handle missing or zero values"""
    missingValProcessing(dfDiabetes)
    return dfDiabetes
#####################################################################################################
#  Function Name : missingValProcessing
#  Description   : Check and handle missing or zero values in columns
#  Input params  : dfDiabetes(Data frame set)
#  Output        : Replace '0' values with column mean
#####################################################################################################
def missingValProcessing(dfDiabetes):
    print("\t\tZero values in column report")
    print(BORDER)
    replaceZeroValCols=[]
    missingValuesDF={"ColName":[],"Missing Value Count":[]}
    for colName in dfDiabetes.drop(columns='Outcome').columns:
        missingValCount=(dfDiabetes[colName]==0).sum()
        missingValuesDF['ColName'].append(colName)
        missingValuesDF["Missing Value Count"].append(missingValCount)
        if(missingValCount>0):
            replaceZeroValCols.append(colName)
    """Displaying statistics of missing values count vs Column name"""
    missingValDataFrame=pd.DataFrame(missingValuesDF)
    print(missingValDataFrame)

    print("Column List with zero values")
    print(replaceZeroValCols)

    for colName in replaceZeroValCols:
        """Replace '0' with column mean"""
        dfDiabetes[colName]=dfDiabetes[colName].replace(0,dfDiabetes[colName].mean())
    print(dfDiabetes)

    print(dfDiabetes.shape)

#####################################################################################################
#   Function Name   :   LoadBasicInformationDataSet
#   Desccrption     :   Step-1
#                       Exploratory Data Analysis (EDA):
#                       1.1 Load the dataset using pandas
#                       1.2 Show column info and check for null values
#                       1.3 Display basic statistics using .describe()
#                       1.4 Plot the distribution of the target variable (Outcome).
#                       1.5 Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
#                       Step-2
#                       Data preprocessing
#                       2.1 Check and handle missing or zero values in columns like Glucose,blood pressure etc
#                       2.2 Apply feature scaling using standards scalar or min-max scalar
#                       2.3 Split the data set into features(x) and target(y)
#   Input Params    :   -
#   Output          :   Scaled,Preprocessed data frame
#####################################################################################################
def LoadBasicInformationDataSet():
    """Exploratory Data Analysis (EDA):
    Step 1.1.Load the dataset using pandas"""
    diabetesDF=load_Data_File(FILENAME)

    """Step 1.2,1.3 Get data set statistics """
    display_Dataset_Statistics(diabetesDF)

    """Step 1.4 Plot the distribution of the target variable (Outcome).
    ------------------------------------------------"""
    plot_Features_Target_Distribution(diabetesDF)

    """Step 1.5 Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.
    ------------------------------------------------"""
    display_Correlation_Matrix(diabetesDF)
    print(BORDER)

    """Step-2 Data preprocessing"""
    diabetesDF=dataPreProcessing(diabetesDF)
    return diabetesDF
#####################################################################################################
#  Function Name   :   accuracyCalculations
#  Description     :   This function does all accuracy calculations
#  Input params    :   yTestDS         : Test dataSet actual output,
#                      yPredictOutput  : Testing Predicted output,
#                      algorithmCompareDF :Dictionary for storing values
#  Output         :    Confusion Matrix display              
#####################################################################################################
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
    algorithmCompareDF["Recall"].append(recall_score(yTestDS,yPredictOutput))
    algorithmCompareDF["F1 Score"].append(f1_score(yTestDS,yPredictOutput))
    algorithmCompareDF["Precision"].append(precision_score(yTestDS,yPredictOutput))
    return algorithmCompareDF
#####################################################################################################
#   Function Name   :   DiabetesPreditionUsingLogisticRegression
#   Description     :   This function uses Logistic Regression algorithm
#   Input Params    :   xTrainDS(Training Features data set),
#                       yTrainDS(Expected output of training data set),
#                       xTestDS(Testing features data set),
#                       yTestDS(Expected output of testing data set),
#                       algorithmCompareDF(Dictionary of some stored values)
#   Output          :   Predicted results
#####################################################################################################
def DiabetesPreditionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Logistic Regression Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Logistic Regression")

    logModel=LogisticRegression()
    """Build the model"""
    logModel.fit(xTrainDS,yTrainDS)
    """Testing the model"""
    yPredictOutput=logModel.predict(xTestDS)
    algorithmCompareDF["labels"].append(logModel.classes_)
    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)

    return yPredictOutput

#####################################################################################################
#   Function Name   :  plotBasedOnAccuracy
#   Description     :  Plotting various graphs
#   Input           :  algorithmCompareDF(Information of details of algorithm)
#                      actualVsPredicted(Actual vs prected output)
#   Output          :  Plot of Accuracy,confusion matrix             
#####################################################################################################
def plotBasedOnAccuracy(algorithmDetailsDF,actualVsPredicted):
    print(BORDER)
    print("\t\tComparision matrix for algorithm....")
    print(BORDER)
    print(algorithmDetailsDF)
    #print("Predicted....")
    #print(actualVsPredicted.head())
    actualVsPredicted.to_csv("ActualPredictedResult.csv")
    print(BORDER)
    #Pltting accuracy plot of algorithm
    x=algorithmDetailsDF['Algorithm Name']
    y=algorithmDetailsDF['Accuracy Score']
    plt.bar(x,y,width=1)
    plt.title('Accuracy of algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.xlim(0,10)
    #plt.grid(True)
    plt.show()

    """Plotting confusion matrix for visualtisation"""
    confuMatrix = ConfusionMatrixDisplay(
                     confusion_matrix=algorithmDetailsDF["Confusion Matrix"][0], 
                    display_labels=algorithmDetailsDF["labels"][0])
    confuMatrix.plot()
    plt.show()
    
#####################################################################################################
#   Function Name   :   split_DataSet
#   Description     :   This method splits the data set into training and testing sets
#   Input           :   diabetesDF (Data frame)
#   Output          :   Testing and Training features and Targets data       
#####################################################################################################
def split_DataSet(diabetesDF):
    features=diabetesDF.drop(columns=['Outcome'])
    target=diabetesDF['Outcome']
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(features,target,
                                                           test_size=TEST_SIZE,
                                                           random_state=RANDOM_STATE)
    print(f"x Train Shape : {xTrainDS.shape}")
    print(f"y Train Shape : {yTrainDS.shape}")
    print(f"x Test Shape : {xTestDS.shape}")
    print(f"y Test Shape : {yTestDS.shape}")

    return xTrainDS,xTestDS,yTrainDS,yTestDS
#####################################################################################################
#   Function name    :  build_Pipeline
#   Description      :  Build a pipeline
#   Input Params     :  -
#   Output           :  Return pipeline object
#####################################################################################################
def build_Pipeline():
    pipe=Pipeline(steps=[
         ("scalar",StandardScaler()),
         ("clf",LogisticRegression(max_iter=1000)),
    ])
    return pipe

#####################################################################################################
#   Function name    :  trainPipeline
#   Description      :  Train a pipeline
#   Input Params     :  pipeline,xTrain,yTrain data set
#   Output           :  Return pipeline object
#####################################################################################################
def trainPipeline(pipeline,xTrain,yTrain):
    pipeline.fit(xTrain,yTrain)
    return pipeline
#####################################################################################################
#   Function name    :  saveTrainedModel
#   Description      :  Save the trained model
#   Input Params     :  model,MODEL_PATH
#   Output           :  -
#####################################################################################################
def saveTrainedModel(model,path=MODEL_PATH):
    joblib.dump(model,path)
    print(f"Model saved to path :{path}")

#####################################################################################################
#   Function name    :  loadTrainedModel
#   Description      :  Load the trained model
#   Input Params     :  path = MODEL_PATH
#   Output           :  model
#####################################################################################################
def loadTrainedModel(path=MODEL_PATH):
    model = joblib.load(path)
    print(f"Model loaded from the path :{path}")
    return model

#####################################################################################################
#   Function name    :  testSampleDataOnTrainedModel
#   Description      :  This methos selects a random sample from data and displays result
#   Input Params     :  model,dfDiabetes
#   Output           :  -
#####################################################################################################
def testSampleDataOnTrainedModel(model,dfDiabetes):
    result=['Non Diabetic','Diabetic']
    sample =dfDiabetes.sample(n=1)
    predictedResult=model.predict(sample.drop(columns=['Outcome']))
    print(BORDER)
    print(f"Selected sample data for testing is \n: {sample}")
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)

#####################################################################################################
#   Function name    :  plotFeatureImportance
#   Description      :  Plots feature importance
#   Input Params     :  model
#   Output           :  Plotted output
#####################################################################################################
def plotFeatureImportance(model,feature_names):
    importances=[]
    if hasattr(model,"named_steps") and "clf" in model.named_steps:
        clf=model.named_steps['clf']
        if hasattr(clf,"feature_importances_"):
            importances=(clf.feature_importances_)
        elif hasattr(clf,"coef_"):
             importances=clf.coef_[0] 
             importances=np.abs((importances))

    elif(hasattr(model,"feature_importances_")):
        importances=model.feature_importances_
    elif(hasattr(model,"coef_")):
         importances=model.coef_[0] 
         importances=np.abs((importances))
         #print(f"Importances :{importances}")
    else:
        print("Feature importance is not available for this model")
        return
    #print(f"Importances:{importances}")
    idx=np.argsort((importances))[::-1]
    #print(f"idx:{idx} features : {feature_names}")
    plt.figure(figsize=(8,4))
    plt.bar(range(len(importances)),importances[idx])
    plt.xticks(range(len(importances)),[feature_names[i] for i in idx],rotation =45,ha='right')
    plt.ylabel("Importance")
    plt.title("Feature Importance Plot")
    plt.tight_layout()
    plt.show()        

#####################################################################################################
#   Function name    :  DiabetesPrediction
#   Description      :  Loads ths Data,Preprocessing and Splitting and training of data set 
#   Input Params     :  -
#   Output           :  Accuracy,Confusion Matrix and classification Report 
#####################################################################################################
def DiabetesPrediction():
    # 1. Load Data set,Disaply dataset statistics and Missing value
    diabetesDF=LoadBasicInformationDataSet()
    
    # 2. Split data set into training and testing set
    xTrainDS,xTestDS,yTrainDS,yTestDS=split_DataSet(diabetesDF)
    
    #3. Build and Train pipeline
    pipeline=build_Pipeline() 
    trainedModel=trainPipeline(pipeline,xTrainDS,yTrainDS)
    print(f"Trained pipeline: {trainedModel}")

    #5. Used Logistic Regression for result prediction and accuracy calculations        
    yPredictLR=trainedModel.predict(xTestDS)

    
    actualVsPredicted={"Y Actual":yTestDS,
                       "Logistic Regression Predicted":yPredictLR}
    #4. Created Dictionary for storing importtant values
    algorithmCompareDF={"Algorithm Name":['Logistic Regression'],
                        "Training Accuracy":[accuracy_score(yTrainDS,trainedModel.predict(xTrainDS))*100],
                        "Accuracy Score":[],
                        "Confusion Matrix":[],
                        "labels":[trainedModel.classes_], 
                        "Precision":[],"Recall":[],"F1 Score":[]}
    
    # 5. Accuracy calculations
    algorithmCompareDF=accuracyCalculations(yTestDS,yPredictLR,algorithmCompareDF)
    # 6.Plotting comparision
    plotBasedOnAccuracy(pd.DataFrame(algorithmCompareDF),pd.DataFrame(actualVsPredicted))
    featureName=diabetesDF.drop(columns='Outcome').columns
    #print(featureName)
    plotFeatureImportance(trainedModel,featureName)
    # 7. Save the model(pipeline) using joblib
    saveTrainedModel(trainedModel,MODEL_PATH)
    #8. Load the model and test a sample
    savedAndTrainedModel=loadTrainedModel(MODEL_PATH)
    #9. Test Model on a random sample from data set
    testSampleDataOnTrainedModel(savedAndTrainedModel,diabetesDF)

#---------------------------------------------------------------------------------------------------------
#  Function Name    : main()
#  Description      : Main function from where execution starts
#---------------------------------------------------------------------------------------------------------
def main():
    DiabetesPrediction()
#---------------------------------------------------------------------------------------------------------
# Main entry point of the application
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()