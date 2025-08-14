"""-----------------------------------------------------------------------------------------------------
                          Assignment 31
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement: Based on given information find whether given tumor is malignant or benign
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    roc_auc_score,
    roc_curve,auc,
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    recall_score,
    f1_score,
    precision_score)
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.pipeline import Pipeline
from pathlib import Path
import joblib   #preserve model
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="breast-cancer-wisconsin.csv"
TEST_SIZE=0.2
RANDOM_STATE=42
ENSEMBLE=Path("ENSEMBLE_VotingClassifier")
ENSEMBLE.mkdir(exist_ok=True)
#MODEL_PATH=ARTIFACTS / 'diabetes_pipeline.joblib'
TARGET_COLNAME="CancerType"
"""Classification model list"""
CLF_MODELS=  {"Decision Tree":DecisionTreeClassifier(),
             "Random Forest":RandomForestClassifier(),
             "Gradient Boosting":GradientBoostingClassifier()}
#####################################################################################################
#   Function Name   :   LoadAndExploreDataset()
#   Description     :   Load and explore data set
#                       Load data using pandas
#                       Handle missing or unknown values
#                       Display basic statistics and visualise class distibution
#   Input Params    :   -
#   Output          :   Data Frame
#####################################################################################################
def LoadAndExploreDataset():
    """Step 1.1.Load the dataset using pandas"""
    df=pd.read_csv(FILENAME)
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(df)
    return df
#####################################################################################################
#   Function Name   :   displayDatasetStatistics
#   Description     :   This method loads the data set information
#   Input params    :   Data frame
#   Output          :   Data statistics
#####################################################################################################
def displayDatasetStatistics(df):
    """Step 1.2 Show column info and check for null values
    ------------------------------------------------""" 
    print("Data set columns details...")
    print(BORDER)
    print(df.columns)
   
    df.dropna(inplace=True)

    print(BORDER)
    """Step 1.3 Display basic statistics using .describe()
    ------------------------------------------------"""
    print("Data Frame details statistics")
    print(BORDER)
    print(df.describe())
    print(BORDER)
    return df
#####################################################################################################
#   Function Name   :   preprocessDataSet
#   Description     :   Convert categorical variables using Label Encoding or One-Hot Encoding.
#                       Scale numeric features (e.g., using StandardScaler)
#   Input Params    :   Data Frame
#   Output          :   Scaled data set
#####################################################################################################
def preprocessDataSet(df):
     """Encode Data set"""
     EncodeDataSet(df)
     print(df.head())
     """load co-relation matrix"""
     displayCorrelationMatrix(df)
     """Mapping target column to 1 and 0 values"""
     df[TARGET_COLNAME].replace({2:0,4:1},inplace=True)
     return df 
#####################################################################################################
#   Function Name   :   EncodeDataSet
#   Description     :   Prepare data by applying label encoding
#   Input params    :   data frame
#   Output          :   Creating encoded csv file for refernce with name 'DataEncoded.csv' 
#####################################################################################################
def EncodeDataSet(df):
    #Label enconding for all data set coulmns
    for colName in df.select_dtypes(include=['object']).columns:
        #print(colName)
        labelEncoder = LabelEncoder()
        df[colName]=labelEncoder.fit_transform(df[colName])
        df[colName].unique()
    print(BORDER)
    print("Creating encoded csv file for refernce with name 'DataEncoded.csv'")
    df.to_csv("DataEncoded.csv")
    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(df.head())
    print(BORDER)
    return df
#####################################################################################################
#   Function name    :  build_Pipeline
#   Description      :  Build a pipeline
#   Input Params     :  colTransformer,clf_Name
#   Output           :  Return pipeline object
#####################################################################################################
def build_Pipeline(clf_Name):
    pipe=Pipeline(steps=[
         ("scalar",StandardScaler()),
         ("clf",clf_Name),
    ])
    return pipe
#####################################################################################################
#   Function Name   :   displayCorrelationMatrix
#   Description     :   Plot the Co-relation matrix
#   Input Params    :   Data frame   
#   Output          :   Co-relation Matrix
#####################################################################################################
def displayCorrelationMatrix(df):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()
#####################################################################################################
#   Function Name   :  findFeaturesAndTarget
#   Description     :  Finds Target and Features
#   Input Params    :  Data Frame
#   Output          :  Features and Targets  
#####################################################################################################
def findFeaturesAndTarget(df):
    features=df.drop(columns=[TARGET_COLNAME])
    target=df[TARGET_COLNAME]
    return features,target    
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

    print("Classification report...")
    print(BORDER)
    confusionMatrixReport=classification_report(yTestDS,yPredictOutput)
    print(confusionMatrixReport)
#####################################################################################################
#   Function Name   :  plotAndCompareConfusionMatrixROC
#   Description     :  Plotting various graphs
#   Input           :  algorithmCompareDF(Information of details of algorithm)
#                      actualVsPredicted(Actual vs prected output)
#   Output          :  Plot of Accuracy,confusion matrix             
#####################################################################################################
def plotAndCompareConfusionMatrixROC(algorithmCompareDF,actualVsPredicted):
    print(BORDER)
    print("\t\tComparision matrix for algorithm....")
    print(BORDER)
    print(algorithmCompareDF)
    print(BORDER)

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
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()

    print(BORDER)
    print("Actual VS Predicted results model wise")
    print(BORDER)

    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("TestResults.csv")


    """ROC Curve using sub plots"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5)) 

    for algoCnt in range(len(algorithmCompareDF)):
        algoName=algorithmCompareDF['Algorithm Name'][algoCnt]
       
        falsePositiveRate, truePositiveRate, threshold = roc_curve(actualVsPredicted['Actual'], actualVsPredicted[algoName])
        
        rocAuc = auc(falsePositiveRate, falsePositiveRate)
       
        axes[algoCnt].plot(falsePositiveRate,truePositiveRate,label=f"{algoName} (ROC-AUC Score {rocAuc})")
        axes[algoCnt].plot([0, 1], [0, 1], color="Red", label='Base Line',linestyle='--')

        axes[algoCnt].set_xlabel('False Positive Rate')
        axes[algoCnt].set_ylabel('True Positive Rate')
        axes[algoCnt].set_title('ROC Curves : Decision Tree and Random Forest')
        #confuMatrix.plot(ax=axes[algoName])
        axes[algoCnt].set_title(algorithmCompareDF["Algorithm Name"][algoCnt])
        axes[algoCnt].legend()

    plt.tight_layout()
    plt.show()

    """ROC-AUC Curve"""
    plt.figure(figsize=(10, 6))
    
    for algoName in algorithmCompareDF['Algorithm Name']:
        falsePositiveRate, truePositiveRate, threshold = roc_curve(actualVsPredicted['Actual'], actualVsPredicted[algoName])
        rocAuc = auc(falsePositiveRate, truePositiveRate)
        plt.plot(falsePositiveRate,truePositiveRate,label=f"{algoName} (ROC-AUC Score {rocAuc})")
    plt.plot([0, 1], [0, 1], color="Red", label='Base Line',linestyle='--')

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves : Decision Tree and Random Forest')
    plt.legend()
    plt.show()   
#####################################################################################################
#   Function Name   :   split_DataSet
#   Description     :   This method splits the data set into training and testing sets
#   Input           :   data frame
#   Output          :   Testing and Training features and Target       
#####################################################################################################
def split_DataSet(df):
    """Divide data set into features and target"""
    features,target=findFeaturesAndTarget(df)
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(features,target,
                                                           test_size=TEST_SIZE,
                                                           random_state=RANDOM_STATE)
    print(f"x Train Shape : {xTrainDS.shape}")
    print(f"y Train Shape : {yTrainDS.shape}")
    print(f"x Test Shape : {xTestDS.shape}")
    print(f"y Test Shape : {yTestDS.shape}")

    return xTrainDS,xTestDS,yTrainDS,yTestDS    
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
#   Function Name   :  TrainAndSaveModels
#   Description     :  Train and save individual models 
#   Input Params    :  df Data Frame,Dictionaries for storing values 
#####################################################################################################
def TrainAndSaveModels(df,algorithmCompareDF, actualVsPredicted):
    #Split data set into training and testing set
    xTrainDS,xTestDS,yTrainDS,yTestDS=split_DataSet(df)
    actualVsPredicted["Actual"]=yTestDS
    featureImportanceList=[]
    """Creating pipelines for 3 models"""    
    for clf_Name,clfModel in CLF_MODELS.items():
        # Build and Train pipeline
         pipeline=build_Pipeline(clfModel) 
         trainedModel=trainPipeline(pipeline,xTrainDS,yTrainDS)
         print(f"Trained pipeline for {clf_Name}: {trainedModel}")

         #5. Used 'Decision Tree','Random Forest' and 'Gradient Boosting'
         # result prediction and accuracy calculations        
         yPredict=trainedModel.predict(xTestDS)
         # Updating predicted results
         actualVsPredicted[clf_Name]=yPredict
         algorithmCompareDF["Algorithm Name"].append(clf_Name)

         algorithmCompareDF["Training Accuracy"].\
         append(accuracy_score(yTrainDS,trainedModel.predict(xTrainDS))*100)
        # 6. Accuracy calculations

         """Positive Predictions"""
         y_predPositiveClassLR = trainedModel.predict_proba(xTestDS)[:, 1]
         """ROC-AUC Score"""
         aucScoreLR = roc_auc_score(yTestDS, y_predPositiveClassLR)
         algorithmCompareDF["ROC-AUC Score"].append(aucScoreLR)
         actualVsPredicted[clf_Name]=y_predPositiveClassLR
         
         accuracyCalculations(yTestDS,yPredict,algorithmCompareDF) 
         featureName=df.drop(columns=TARGET_COLNAME).columns
             #print(featureName)
         plotFeatureImportance(trainedModel,featureName,clf_Name,featureImportanceList)
         # 7. Save the model(pipeline) using joblib
         saveTrainedModel(trainedModel,clf_Name)
    #print(f"featureImportanceList=[]:{featureImportanceList}")
    featureImportnancesModelWise(featureImportanceList)
#####################################################################################################
#   Function name    :  plotFeatureImportance
#   Description      :  Plots feature importance
#   Input Params     :  model
#   Output           :  Plotted output
#####################################################################################################
def plotFeatureImportance(model,feature_names,modelName,featureImportanceList):
    importances=[]
    if hasattr(model,"named_steps") and "clf" in model.named_steps:
        
        clf=model.named_steps['clf']
        if hasattr(clf,"feature_importances_"):   
            importances=clf.feature_importances_
        elif hasattr(clf,"coef_"):
             importances=clf.coef_[0] 
             importances=np.abs((importances))
        elif(hasattr(model,"feature_importances_")):
            print("1",importances)
            importances=model.feature_importances_
    elif(hasattr(model,"feature_importances_")):
        importances=model.feature_importances_
    elif(hasattr(model,"coef_")):
         importances=model.coef_[0] 
         importances=np.abs((importances))
         #print(f"Importances :{importances}")
    else:
        print("Feature importance is not available for this model")
        return
    featureImportance={}
    featureImportance["Algorithm Name"]=modelName
    featureImportance["Feature Names"]=feature_names
    featureImportance["Importances"]=importances
    featureImportanceList.append(featureImportance)

#####################################################################################################
#   Function Name   :   featureImportnancesModelWise
#   Description     :   Plotting feature Importnace model wise for comparision
#   Input Params    :   featureImportanceList(Model wise)
# #####################################################################################################
def featureImportnancesModelWise(featureImportanceList):   

    """Create the figure and subplots
    As we used 3 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10,10)) 

    for cnt in range(len(featureImportanceList)):
        modelName=featureImportanceList[cnt]["Algorithm Name"]
        feature_names=featureImportanceList[cnt]["Feature Names"]
        importances=featureImportanceList[cnt]["Importances"]
        idx=np.argsort((importances))[::-1]
        axes[cnt].bar(range(len(importances)),importances[idx])
        axes[cnt].set_xticks(range(len(importances)),[feature_names[i] for i in idx],rotation =30,ha='right')
        axes[cnt].set_ylabel("Importance")
        axes[cnt].set_title(f"Feature Importance Plot : {modelName}")
    plt.tight_layout()
    plt.show()            
#####################################################################################################
#   Function name    :  testSampleDataOnTrainedModel
#   Description      :  This methos selects a random sample from data and displays result
#   Input Params     :  model,sampleData
#   Output           :  -
#####################################################################################################
def testSampleDataOnTrainedModel(model,sampleData):
    result=['Yes(Cancerous)','No (Non-Cancerous)']
    predictedResult=model.predict(sampleData.drop(columns=[TARGET_COLNAME]))
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)
#####################################################################################################
#   Function Name   :  testTrainedModelAndDisplay
#   Description     :  test and display results for individual models 
#   Input Params    :  df Data Frame,Dictionaries for storing values 
#####################################################################################################
def testTrainedModelAndDisplay(df, algorithmCompareDF, actualVsPredicted):
    sampleTestData =df.sample(n=1)
    print(BORDER)
    print(f"Selected sample data for testing is \n: {sampleTestData}")
    print(BORDER)
    """Loading saved model and sample tetsing"""
    for clf_Name,clfModel in CLF_MODELS.items():  
        print(f"Sample testing Using : {clf_Name}")  
        #8. Load the model and test a sample
        savedAndTrainedModel=loadTrainedModel(clf_Name)
        #9. Test Model on a random sample from data set
        testSampleDataOnTrainedModel(savedAndTrainedModel,sampleTestData)
    #print(f"algorithmCompareDF:{algorithmCompareDF}")
    # 6.Plotting comparision
    plotAndCompareConfusionMatrixROC(pd.DataFrame(algorithmCompareDF),pd.DataFrame(actualVsPredicted))  
#####################################################################################################
#   Function name    :  saveTrainedModel
#   Description      :  Save the trained model
#   Input Params     :  model,modelName
#   Output           :  -
#####################################################################################################
def saveTrainedModel(model,modelName):
    path=modelName+".joblib"
    path=ENSEMBLE/path
    joblib.dump(model,path)
    print(f"Model saved to path :{path}")
#####################################################################################################
#   Function name    :  loadTrainedModel
#   Description      :  Load the trained model
#   Input Params     :  path = MODEL_PATH
#   Output           :  model
#####################################################################################################
def loadTrainedModel(modelName):
    path=modelName+".joblib"
    path=ENSEMBLE/path
    model = joblib.load(path)
    print(f"Model loaded from the path :{path}")
    return model
############################################################################################################
#   Function Name   :   BCPrediction
#   Description     :   Load and explore data set
#                       Preprocess the Data
#                       Split the Data
#                       Train Classification Models
#                       Evaluate the Models
#                       Visualize Results
############################################################################################################
def BCPrediction():
    """Load and explore data set"""
    df=LoadAndExploreDataset()
   
    """2. Preprocess Data set"""
    df=preprocessDataSet(df)
    
    #3. Created Dictionary for storing importtant values
    algorithmCompareDF={"Algorithm Name":[],"Training Accuracy":[],"Accuracy Score":[],
                        "Confusion Matrix":[],"ROC-AUC Score":[]}

    actualVsPredicted={}
    """Train and save individual models"""
    TrainAndSaveModels(df,algorithmCompareDF, actualVsPredicted)
    """Test the trained models"""
    testTrainedModelAndDisplay(df, algorithmCompareDF, actualVsPredicted) 
#---------------------------------------------------------------------------------------------------------
#  Function Name    : Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    BCPrediction()
#---------------------------------------------------------------------------------------------------------
#   Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()