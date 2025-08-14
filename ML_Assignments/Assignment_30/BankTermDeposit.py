"""-----------------------------------------------------------------------------------------------------
                          Assignment 30
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:A Portuguese bank conducted marketing campaigns to promote term deposit subscriptions. The goal is to
predict whether a client will subscribe (yes or no) to a term deposit based on their profile and campaign
interaction details.
--------------------------------------------------------------------------------------------------------"""
######################################################################################################
#   Required Python Packages
######################################################################################################
import pandas as pd
from matplotlib.pyplot import figure,show
import matplotlib.pyplot as plt
from seaborn import countplot
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,roc_auc_score
)
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.pipeline import Pipeline
from pathlib import Path
import numpy as np
import joblib   #preserve model
######################################################################################################
#   File paths and constants
######################################################################################################
INPUT_FILE="bank-full.csv"
BORDER="-"*65
TEST_SIZE=0.2
RANDOM_STATE=42
TARGET_COLNAME='y'
BANKDETAILS=Path("BANK_TERM_DEPOSIT_MODELS")
BANKDETAILS.mkdir(exist_ok=True)
"""Classification model list"""
CLF_MODELS=  {"Logistic Regression":LogisticRegression(),
             "KNN": KNeighborsClassifier(),
             "Random Forest":RandomForestClassifier()}
######################################################################################################
#   Function Name   :    loadDataFile
#   Description     :    This method loads the data set from 'diabetes.csv' file
#   Input params    :    Data file path
#   Output          :    Data frame
######################################################################################################
def loadDataFile(dataFilePath):
    try:
        """Step-1.0  Load And read CSV data file
        ------------------------------------------------"""
        dfBank=pd.read_csv(dataFilePath,sep=";")
        print(BORDER)
        """Step 1.1 Display the first 5 rows.
        ------------------------------------------------""" 
        print("Bank Term deposit susbsciprtion prediction data set loaded successfully...")
        print(BORDER)
        print(dfBank.head())
        print(dfBank.shape)
        print(BORDER)
        return dfBank
    except FileNotFoundError as ex:
        print(f"File not found {dataFilePath}")
        exit()
######################################################################################################
#   Function Name   :   displayDatasetStatistics
#   Description     :   This method loads the data set information
#   Input params    :   Data frame
#   Output          :   Data statistics
######################################################################################################
def displayDatasetStatistics(dfBank):
    """ Show column info and check for null values
    ------------------------------------------------""" 
    print("Data set columns details...")
    print(BORDER)
    print(dfBank.columns)
    print(BORDER)
    """ Display basic statistics using .describe()
    ------------------------------------------------"""
    print("Bank details ststistics")
    print(BORDER)
    print(dfBank.describe())
    print(BORDER)
    return dfBank
######################################################################################################
#   Function Name   :   unknownValProcessing
#   Describe        :   Check and handle missing or unknown values in columns
#   Input params    :   dfBank(Data frame set)
#   Output          :   Updated data frame
######################################################################################################
def unknownValProcessing(dfBank):
    print("\t\tunknown values in column report")
    print(BORDER)
    colUnknown=[]
    colZero=[]
    unknownZeroValuesDF={"ColName":[],"Unknown Value Count":[],"Zero Value Count":[]}
    for colName in dfBank.columns:
        unknownValCount=(dfBank[colName]=='unknown').sum()
        unknownZeroValuesDF['ColName'].append(colName)
        unknownZeroValuesDF["Unknown Value Count"].append(unknownValCount)

        zeroValCount=(dfBank[colName]==0).sum()
        unknownZeroValuesDF["Zero Value Count"].append(zeroValCount)

        """Unknown values in column add colName in a list"""
        if unknownValCount > 0:
            colUnknown.append(colName)
        if zeroValCount > 0:
            colZero.append(colName)
    
    unknownZeroValuesDF=pd.DataFrame(unknownZeroValuesDF)
    
    print(BORDER)
    print("Column statitics for 'unknown' and '0' values")
    print(BORDER)

    print(unknownZeroValuesDF)
    print(BORDER)

    """Replace unknown and zero values with mean() """
    #colZero=['balance','duration',previous']
    #colUnknown=['job','education','contact','poutcome']
    print(BORDER)
    print("Col Name with 0 values :",colZero)
    print("Col Name with 'unknown' values :",colUnknown)
    print(BORDER)
    """Replacing 0 values with mean() of the column"""
    for colName in colZero:
        dfBank[colName]=dfBank[colName].replace(0,dfBank[colName].mean())
    """Different method 'unknown' values"""
    for colName in colUnknown:
        categoryList=dfBank[colName].value_counts().index.tolist()
        print(f"Col name 2 :{colName}")
        print(f"categoryList :{categoryList}")
        if(categoryList[0]!='unknown'):
            unknownCategoryName=categoryList[0]
        if(categoryList[0]=='unknown'):
            unknownCategoryName=categoryList[1]
        print(f"Col Name 2: {colName} Unknown Category Name  :{unknownCategoryName}")
        dfBank[colName]=dfBank[colName].replace('unknown',unknownCategoryName)

    print(BORDER)
    print("\nUpdated Data set values are stored in csv 'replacedUnknownValues.csv'")
    print(dfBank)
    dfBank.to_csv("replacedUnknownValues.csv")
    print(dfBank.shape)
######################################################################################################
#   Function Name   :   displayCorrelationMatrix
#   Description     :   Plot the Co-relation matrix.
######################################################################################################
def displayCorrelationMatrix(dfBank):
    plt.figure(figsize=(10,6))
    sns.heatmap(dfBank.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()
######################################################################################################
#   Function Name   :   EncodeDataSet
#   Description     :   Prepare data by applying label encoding
#   Input params    :   dfBank(Bank data frame)
#                       Creating encoded csv file for refernce with name 'BankTermDataEncoded.csv' 
######################################################################################################
def EncodeDataSet(dfBank):
    #Label enconding for all data set coulmns
    for colName in dfBank.select_dtypes(include=['object']).columns:
        #print(colName)
        labelEncoder = LabelEncoder()
        dfBank[colName]=labelEncoder.fit_transform(dfBank[colName])
        dfBank[colName].unique()
    print(BORDER)
    print("Creating encoded csv file for refernce with name 'BankTermDataEncoded.csv'")
    dfBank.to_csv("BankTermDataEncoded.csv")
    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(dfBank.head())
    print(BORDER)
    return dfBank
######################################################################################################
#   Function Name   :   LoadAndExploreDataset
#   Description     :   Load and explore data set 
#                       Load data using pandas
#                       Handle missing or unknown values
#                       Display basic stats and visualise class distibution
#   Input Params    :   -
#   Output          :   Data frame
######################################################################################################
def LoadAndExploreDataset():
    """Step 1.1.Load the dataset using pandas"""
    dfBankDeposit=loadDataFile(INPUT_FILE)
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(dfBankDeposit)
    """1.3 Check and handle missing or unknown values in columns su"""      
    unknownValProcessing(dfBankDeposit)
    return dfBankDeposit

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
#   Input Params     :  model,modelName
#   Output           :  -
#####################################################################################################
def saveTrainedModel(model,modelName):
    path=modelName+".joblib"
    path=BANKDETAILS/path
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
    path=BANKDETAILS/path
    model = joblib.load(path)
    print(f"Model loaded from the path :{path}")
    return model
#####################################################################################################
#   Function name    :  testSampleDataOnTrainedModel
#   Description      :  This methos selects a random sample from data and displays result
#   Input Params     :  model,sampleData
#   Output           :  -
#####################################################################################################
def testSampleDataOnTrainedModel(model,sampleData):
    result=['Yes (Subscribe)','No(Not Subscribed)']
    predictedResult=model.predict(sampleData.drop(columns=['y']))
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)
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
                                             display_labels=["Subscribed","Non Subscribed"])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()

    print(BORDER)
    print("Acutal VS Predicted outputs ")
    print(BORDER)

    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("BankPredictedVsActualResults.csv")

    """ROC Curve using sub plots"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for algoCnt in range(len(algorithmCompareDF)):
        algoName=algorithmCompareDF['Algorithm Name'][algoCnt]
        #print(algoName)
        #print(f"{algoCnt}")
        #print(actualVsPredicted[algoName])
        falsePositiveRate, truePositiveRate, threshold = roc_curve(actualVsPredicted['Actual'], actualVsPredicted[algoName])
        
        rocAuc = auc(falsePositiveRate, falsePositiveRate)
       
        axes[algoCnt].plot(falsePositiveRate,truePositiveRate,label=f"{algoName} (ROC-AUC Score {rocAuc})")
        axes[algoCnt].plot([0, 1], [0, 1], color="Red", label='Base Line',linestyle='--')

        axes[algoCnt].set_xlabel('False Positive Rate')
        axes[algoCnt].set_ylabel('True Positive Rate')
        axes[algoCnt].set_title('ROC Curves : Logistice Regression,KNN and Random Forest')
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
    plt.title('ROC Curves : Logistice Regression,KNN and Random Forest')
    plt.legend()
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
#   Function Name   :   split_DataSet
#   Description     :   This method splits the data set into training and testing sets
#   Input           :   dfBank (Data frame)
#   Output          :   Testing and Training features and Targets data       
#####################################################################################################
def split_DataSet(dfBank):
    
    """Divide data set into features and target"""
    features,target=findFeaturesAndTarget(dfBank)
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(features,target,
                                                           test_size=TEST_SIZE,
                                                           random_state=RANDOM_STATE)
    print(f"x Train Shape : {xTrainDS.shape}")
    print(f"y Train Shape : {yTrainDS.shape}")
    print(f"x Test Shape : {xTestDS.shape}")
    print(f"y Test Shape : {yTestDS.shape}")

    return xTrainDS,xTestDS,yTrainDS,yTestDS  
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
#   Function Name   :   preprocessDataSet
#   Description     :   Convert categorical variables using Label Encoding or One-Hot Encoding.
#   Input Params    :   dfBank     
######################################################################################################
def preprocessDataSet(dfBank):
     """Encode Data set"""
     EncodeDataSet(dfBank)
     print(dfBank.head())
     """load co-relation matrix"""
     displayCorrelationMatrix(dfBank)
     
     return dfBank 
#####################################################################################################
#   Function Name   :   preprocessDataSet
#   Description     :   Load and explore data set
#                       Task 2. Preprocess the Data
#                       Task 3. Split the Data
#                       Task 4. Train Classification Models
#                       Task 5. Evaluate the Models
#                       Task 6. Visualize Results
#####################################################################################################
def BankTermDepositSubscriptionPrediction():
    """Load  CSV and explore data set"""
    dfBank=LoadAndExploreDataset()    
    #3. Created Dictionary for storing importtant values
    algorithmCompareDF={"Algorithm Name":[],"Training Accuracy":[],"Accuracy Score":[],
                        "Confusion Matrix":[],"ROC-AUC Score":[]}

    actualVsPredicted={}
    """Train and save individual models"""
    TrainAndSaveModels(dfBank,algorithmCompareDF, actualVsPredicted)
    """Test the trained models"""
    testTrainedModelAndDisplay(dfBank, algorithmCompareDF, actualVsPredicted) 

#####################################################################################################
#   Function Name   :  TrainAndSaveModels
#   Description     :  Train and save individual models 
#   Input Params    :  dfBank Data Frame,Dictionaries for storing values 
#####################################################################################################
def TrainAndSaveModels(dfBank,algorithmCompareDF, actualVsPredicted):
    """Preprocessing using label encoding"""
    dfBank=preprocessDataSet(dfBank)
    #Split data set into training and testing set
    xTrainDS,xTestDS,yTrainDS,yTestDS=split_DataSet(dfBank)
    actualVsPredicted["Actual"]=yTestDS
    featureImportanceList=[]
    """Creating pipelines for 3 models"""    
    for clf_Name,clfModel in CLF_MODELS.items():
        # Build and Train pipeline
         pipeline=build_Pipeline(clfModel) 
         trainedModel=trainPipeline(pipeline,xTrainDS,yTrainDS)
         print(f"Trained pipeline for {clf_Name}: {trainedModel}")

         #5. Used Logistic Regression,KNN,Decision Tree for 
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
         if(clf_Name=="Logistic Regression" or clf_Name=="Random Forest"):   
             featureName=dfBank.drop(columns='y').columns
             #print(featureName)
             plotFeatureImportance(trainedModel,featureName,clf_Name,featureImportanceList)
         # 7. Save the model(pipeline) using joblib
         saveTrainedModel(trainedModel,clf_Name)
    #print(f"featureImportanceList=[]:{featureImportanceList}")
    featureImportnancesModelWise(featureImportanceList)

#####################################################################################################
#   Function Name   :   featureImportnancesModelWise
#   Description     :   Plotting feature Importnace model wise for comparision
#   Input Params    :   featureImportanceList(Model wise)
# #####################################################################################################
def featureImportnancesModelWise(featureImportanceList):   

    """Create the figure and subplots
    As we used 2 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(18,8)) 

    for cnt in range(len(featureImportanceList)):
        modelName=featureImportanceList[cnt]["Algorithm Name"]
        feature_names=featureImportanceList[cnt]["Feature Names"]
        importances=featureImportanceList[cnt]["Importances"]
        idx=np.argsort((importances))[::-1]
        axes[cnt].bar(range(len(importances)),importances[idx])
        axes[cnt].set_xticks(range(len(importances)),[feature_names[i] for i in idx],rotation =50,ha='right')
        axes[cnt].set_ylabel("Importance")
        axes[cnt].set_title(f"Feature Importance Plot : {modelName}")
    plt.tight_layout()
    plt.show()            

#####################################################################################################
#   Function Name   :  testTrainedModelAndDisplay
#   Description     :  test and display results for individual models 
#   Input Params    :  dfBank Data Frame,Dictionaries for storing values 
#####################################################################################################
def testTrainedModelAndDisplay(dfBank, algorithmCompareDF, actualVsPredicted):
    sampleTestData =dfBank.sample(n=1)
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
######################################################################################################
#  Main function 
######################################################################################################
def main():
    BankTermDepositSubscriptionPrediction()
######################################################################################################
#Main entry point of the program
######################################################################################################
if __name__=="__main__":
    main()