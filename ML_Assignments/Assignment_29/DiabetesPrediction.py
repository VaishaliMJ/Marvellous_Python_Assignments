"""-----------------------------------------------------------------------------------------------------
                          Assignment 29
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains some medical parameters based on that predict 
                 for diabetes positive or negative
                 Algorithms Used : Decision Tree,KNN and Logistic Regression
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

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
ARTIFACTS=Path("diabetes_sample_all")
ARTIFACTS.mkdir(exist_ok=True)
#MODEL_PATH=ARTIFACTS / 'diabetes_pipeline.joblib'

"""Classification model list"""
CLF_MODELS=  {"Logistic Regression":LogisticRegression(),
             "KNN": KNeighborsClassifier(),
             "Decision Tree":DecisionTreeClassifier()}
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
    #return algorithmCompareDF

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
    x=algorithmDetailsDF['Algorithm Name']
    y=algorithmDetailsDF['Accuracy Score']
    plt.bar(x,y,width=0.4)
    plt.title('Accuracy of algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.show()

    """Create the figure and subplots
    As we used 3 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for cnt in range(len(algorithmDetailsDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmDetailsDF["Confusion Matrix"][cnt], 
                                             display_labels=["Diabetic","Non Diabetic"])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmDetailsDF["Algorithm Name"][cnt])
    plt.tight_layout()
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
#   Input Params     :  clf_Name
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
    path=ARTIFACTS/path
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
    path=ARTIFACTS/path
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
    result=['Non Diabetic','Diabetic']
   
    predictedResult=model.predict(sampleData.drop(columns=['Outcome']))
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)

#####################################################################################################
#   Function name    :  plotFeatureImportance
#   Description      :  Plots feature importance
#   Input Params     :  model
#   Output           :  Plotted output
#####################################################################################################
def plotFeatureImportance(model,feature_names,modelName,featureImportanceList):
    importances=[]
    featureImportance={"Algorithm Name":"",
                       "Feature Names":[],
                       "Importances":[]}
    
    if hasattr(model,"named_steps") and "clf" in model.named_steps:
        clf=model.named_steps['clf']
        if hasattr(clf,"feature_importances_"):
            importances=(clf.feature_importances_)
        elif hasattr(clf,"coef_"):
             importances=clf.coef_[0] 
             importances=np.abs((importances))

    elif(hasattr(model,"feature_importances_")):
        importances=model.feature.importances_
    elif(hasattr(model,"coef_")):
         importances=model.coef_[0] 
         importances=np.abs((importances))
         #print(f"Importances :{importances}")
    else:
        print("Feature importance is not available for this model")
        return
    featureImportance["Algorithm Name"]=modelName
    featureImportance["Feature Names"]=feature_names
    featureImportance["Importances"]=importances
    featureImportanceList.append(featureImportance)
      

#####################################################################################################
#   Function name    :  DiabetesPrediction
#   Description      :  Loads ths Data,Preprocessing and Splitting and training of data set 
#   Input Params     :  -
#   Output           :  Accuracy,Confusion Matrix and classification Report 
#####################################################################################################
def DiabetesPrediction():
    #  Load Data set,Disaply dataset statistics and Missing value
    diabetesDF=LoadBasicInformationDataSet()
    #Created Dictionary for storing importtant values

    algorithmCompareDF={"Algorithm Name":[],
                        "Training Accuracy":[],
                        "Accuracy Score":[],
                        "Confusion Matrix":[],
                        "Precision":[],"Recall":[],"F1 Score":[]}
    actualVsPredicted={}
    """Train and save individual models"""
    TrainAndSaveModels(diabetesDF,algorithmCompareDF, actualVsPredicted)
    """Test the trained models"""
    testTrainedModelAndDisplay(diabetesDF, algorithmCompareDF, actualVsPredicted) 
#####################################################################################################
#   Function Name   :  TrainAndSaveModels
#   Description     :  Train and save individual models 
#   Input Params    :  diabetesDF Data Frame,Dictionaries for storing values 
#####################################################################################################
def TrainAndSaveModels(diabetesDF,algorithmCompareDF, actualVsPredicted):
    #Split data set into training and testing set
    xTrainDS,xTestDS,yTrainDS,yTestDS=split_DataSet(diabetesDF)
    actualVsPredicted["Y Actual"]=yTestDS
    featureImportanceList=[]
    """Creating pipelines for 3 models"""    
    for clf_Name,clfModel in CLF_MODELS.items():
        #3. Build and Train pipeline
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
         accuracyCalculations(yTestDS,yPredict,algorithmCompareDF)
         if(clf_Name!="KNN"):   
             featureName=diabetesDF.drop(columns='Outcome').columns
             #print(featureName)
             plotFeatureImportance(trainedModel,featureName,clf_Name,featureImportanceList)
         # 7. Save the model(pipeline) using joblib
         saveTrainedModel(trainedModel,clf_Name)
    print(f"featureImportanceList=[]:{featureImportanceList}")
    featureImportnancesModelWise(featureImportanceList)

#####################################################################################################
#   Function Name   :   featureImportnancesModelWise
#   Description     :   Plotting feature Importnace model wise for comparision
#   Input Params    :   featureImportanceList(Model wise)
# #####################################################################################################
def featureImportnancesModelWise(featureImportanceList):   

    """Create the figure and subplots
    As we used 3 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20,8)) 

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
####################################################################################################
#   Function Name   :  testTrainedModelAndDisplay
#   Description     :  test and display results for individual models 
#   Input Params    :  diabetesDF Data Frame,Dictionaries for storing values 
#####################################################################################################
def testTrainedModelAndDisplay(diabetesDF, algorithmCompareDF, actualVsPredicted):
    sampleTestData =diabetesDF.sample(n=1)
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
    plotBasedOnAccuracy(pd.DataFrame(algorithmCompareDF),pd.DataFrame(actualVsPredicted))    

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