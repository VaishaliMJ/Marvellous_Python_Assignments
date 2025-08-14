"""-----------------------------------------------------------------------------------------------------
                          Assignment 32
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Predict whether a news article is Fake or Real using text classification technique.
                  This assignment dmonstrates the power of ensemble learning using a voting classifier 
                  with models like Logistic Regression ,Decision tree 
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
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
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from pathlib import Path
import joblib   #preserve model
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
TRUE_FILENAME="True.csv"
FAKE_FILENAME="Fake.csv"
DROP_COLUMNS=['subject','date']
TRANSFORM_FEATURE='text'
TEST_SIZE=0.2
RANDOM_STATE=42
NEWS_VALIDITY=Path("NEWS_VALIDITY")
NEWS_VALIDITY.mkdir(exist_ok=True)
VECTORIZER_NAME="Tf-IDF_Vectorizer_Module"
TARGET_COLNAME="label"
"""Classification model list"""
CLF_1=DecisionTreeClassifier()
CLF_2=LogisticRegression()
CLF_MODELS=  {"Decision Tree":CLF_1,
             "Logistic Regression":CLF_2,
             "Voting Classifier Hard":VotingClassifier(
                                estimators=[
                                    ('dt',CLF_1),
                                    ('lr',CLF_2)],
                                    voting="hard"),
             "Voting Classifier Soft":VotingClassifier(
                                 estimators=[
                                    ('dt',CLF_1),
                                    ('lr',CLF_2)],
                                    voting="soft")}
#####################################################################################################
#   Function Name   :   loadDataFile()
#   Description     :   Load and explore data set set from 'True.csv' and 'Fake.csv' files
#                       Load data using pandas.Add 'label' column to both dataFrames Fake=0, True=1
#                       Combine both datasets
#   Input Params    :   Data file paths
#   Output          :   Data Frame
#####################################################################################################
def loadDataFile():
    """Step-1.1  Load And read CSV data file
    ------------------------------------------------"""
    dfTrue=pd.read_csv(TRUE_FILENAME)
    dfFake=pd.read_csv(FAKE_FILENAME)
    """Step 1.2 Add 'label' column to both dataFrames Fake=0, True=1
    ------------------------------------------------""" 
    dfTrue['label']=1
    dfFake['label']=0  
    print(BORDER)
    """Step 1.1 Display the first 5 rows.
    ------------------------------------------------""" 
    print("True and Fake news data set loaded successfully...")
    print(BORDER)
    print(dfTrue.head())
    print(dfTrue.shape)

    print(BORDER)

    print(dfFake.head())
    print(dfFake.shape)
    print(BORDER)
    """Step 1.3 Combine both datasets
    ------------------------------------------------"""  
    dfNews=pd.concat([dfTrue,dfFake],axis=0)
    print(dfNews.shape)
    return dfNews
#####################################################################################################
#   Function Name   :   displayDatasetStatistics
#   Description     :   This method loads the data set information
#                       Use only the relevent columns
#   Input params    :   Data frame
#   Output          :   Data statistics
#####################################################################################################
def displayDatasetStatistics(dfNews):
    
    """Step 1.2 Show column info and check for null values
    ------------------------------------------------""" 
    print("Data set columns details...")
    print(BORDER)
    print(dfNews.columns)
    print(dfNews.isnull().sum())
    """Drop 'na' value rows"""
    dfNews.dropna(inplace=True)
    """Drop date and subject coulmn""" 
    dfNews.drop(columns=DROP_COLUMNS,inplace=True) 
    print(BORDER)
    """ Display basic statistics using .describe()
    ------------------------------------------------"""
    print("News Statistics")
    print(BORDER)
    print(dfNews.describe())
    print(dfNews.head())
    print(dfNews.shape)
    print(BORDER)
    return dfNews
#####################################################################################################
#   Function Name   :   LoadAndExploreDataset()
#   Description     :   Load both fake.csv and True.csv
#                       Add 'Label' column to both 
#                       Combine both datasets
#                       Use only the relevent columns
#   Input Params    :   -
#   Output          :   Data Frame
#####################################################################################################
def LoadAndExploreDataset():
    """Step 1.1 Load the dataset using pandas"""
    dfNews=loadDataFile()
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(dfNews)
    return dfNews
#####################################################################################################
#   Function Name   :   featureExtraction
#   Description     :   Converting text into number format using TF-IDF method
#   Input Params    :   Data Frame
#   Output          :   Transformed Feature
#####################################################################################################
def featureExtraction(dfNews):
    vectorizer = TfidfVectorizer()
    transformedFeatures=vectorizer.fit_transform(dfNews[TRANSFORM_FEATURE])
    featursNames = vectorizer.get_feature_names_out()

    """Save Vectorizer Model"""
    saveVectorizer(vectorizer)
    return transformedFeatures

#####################################################################################################
#   Function name    :  saveVectorizer
#   Description      :  Save the vectorizer model
#   Input Params     :  vectorizer
#   Output           :  -
#####################################################################################################
def saveVectorizer(vectorizer):
    path=VECTORIZER_NAME+".joblib"
    path=NEWS_VALIDITY/path
    joblib.dump(vectorizer,path)
    print(f"Vectorizer saved to path :{path}") 
#####################################################################################################
#   Function name    :  loadVectorizer
#   Description      :  Load the vectorizer model
#   Input Params     :  -
#   Output           :  model
#####################################################################################################
def loadVectorizer():
    path=VECTORIZER_NAME+".joblib"
    path=NEWS_VALIDITY/path
    model = joblib.load(path)
    print(f"Vectorizer loaded from the path :{path}")
    return model    
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
#   Function Name   :   split_DataSet
#   Description     :   This method splits the data set into training and testing sets
#   Input           :   data frame
#   Output          :   Testing and Training features and Target       
#####################################################################################################
def split_DataSet(features,target):
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(features,target,
                                                           test_size=TEST_SIZE,
                                                           random_state=RANDOM_STATE)
    print(f"x Train Shape : {xTrainDS.shape}")
    print(f"y Train Shape : {yTrainDS.shape}")
    print(f"x Test Shape : {xTestDS.shape}")
    print(f"y Test Shape : {yTestDS.shape}")

    return xTrainDS,xTestDS,yTrainDS,yTestDS    
#####################################################################################################
#   Function name    :  trainModel
#   Description      :  Train a Model
#   Input Params     :  pipeline,xTrain,yTrain data set
#   Output           :  Return pipeline object
#####################################################################################################
def trainModel(model,xTrain,yTrain):
    model.fit(xTrain,yTrain)
    return model   
#####################################################################################################
#   Function name    :  saveTrainedModel
#   Description      :  Save the trained model
#   Input Params     :  model,modelName
#   Output           :  -
#####################################################################################################
def saveTrainedModel(model,modelName):
    path=modelName+".joblib"
    path=NEWS_VALIDITY/path
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
    path=NEWS_VALIDITY/path
    model = joblib.load(path)
    print(f"Model loaded from the path :{path}")
    return model    
#####################################################################################################
#   Function Name   :   modelTraining
#   Description     :   Spilt the data set into tarining and testing data
#                       Train model using 'Logistic Regression','Decision Tree Classifier',Voting Classifier
#   Input Params    :   xIndependent,yDependent(Features and Targets)
#      
#####################################################################################################
def modelTraining(xIndependent,yDependent,algorithmCompareDF,actualVsPredicted):
    #Split data set into training and testing set
    xTrainDS,xTestDS,yTrainDS,yTestDS=split_DataSet(xIndependent,yDependent) 
    actualVsPredicted["Actual"]=yTestDS
    for clf_Name,clfModel in CLF_MODELS.items():
            
        trainedModel=trainModel(clfModel,xTrainDS,yTrainDS)
        print(f"Trained model for {clf_Name}: {trainedModel}")
        # result prediction and accuracy calculations        
        yPredict=trainedModel.predict(xTestDS)

        actualVsPredicted[clf_Name]=yPredict

        algorithmCompareDF["Algorithm Name"].append(clf_Name)

        algorithmCompareDF["Training Accuracy"].\
        append(accuracy_score(yTrainDS,trainedModel.predict(xTrainDS))*100)

        """Accuracy Calculations"""
        accuracyCalculations(yTestDS,yPredict,algorithmCompareDF)  

         # 7. Save the model(pipeline) using joblib
        saveTrainedModel(trainedModel,clf_Name)
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
    As we used 4 algorithms use Subplots to plot 3 confusion matrix"""
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(22, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()
    print(BORDER)
    print("Actual VS Predicted values")
    print(BORDER)

    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("TestResults.csv")
#####################################################################################################
#   Function Name   :  findFeaturesAndTarget
#   Description     :  Finds Target and Features
#   Input Params    :  Data Frame
#   Output          :  Features and Targets  
#####################################################################################################
def findFeaturesAndTarget(df):
    """Feature extraction and Target"""
    features=featureExtraction(df)
    target=df[TARGET_COLNAME]
    return features,target  
#####################################################################################################
#   Function name    :  testSampleDataOnTrainedModel
#   Description      :  This method selects a random sample from data and displays result
#   Input Params     :  model,sampleData
#   Output           :  -
#####################################################################################################
def testSampleDataOnTrainedModel(model,sampleData):
    textNews=sampleData[TRANSFORM_FEATURE]
    vectorizer=loadVectorizer()
    feature = vectorizer.transform(textNews)
    print(f"News Is  : {textNews}")
    result=["Fake News","True News"]
    predictedResult=model.predict(feature)
    print(f"Loaded model prediction for randomly selected test sample :{result[predictedResult[0]]}")
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
############################################################################################################
#   Function Name   :   newsValidityPrediction
#   Description     :   Data Preprocessing,Feature Extraction,
#                       Model Training,Evaluation
#
############################################################################################################
def newsValidityPrediction():
    """1.Load and explore data set"""
    dfNews=LoadAndExploreDataset()
    """2.Use TF-IDF vectorization to convert text into numerical features  """
    features,target=findFeaturesAndTarget(dfNews)
    algorithmCompareDF={"Algorithm Name":[],"Training Accuracy":[],"Accuracy Score":[],"Confusion Matrix":[]}
    actualVsPredicted={}
    """Model Training"""
    modelTraining(features,target,algorithmCompareDF,actualVsPredicted)
    """Test the trained models"""
    testTrainedModelAndDisplay(dfNews,algorithmCompareDF,actualVsPredicted) 
    plotAndCompareConfusionMatrixROC(pd.DataFrame(algorithmCompareDF),pd.DataFrame(actualVsPredicted))        

############################################################################################################
#  Main function 
############################################################################################################
def main():
    newsValidityPrediction()
############################################################################################################
#Main entry point of the program
############################################################################################################
if __name__=="__main__":
    main()