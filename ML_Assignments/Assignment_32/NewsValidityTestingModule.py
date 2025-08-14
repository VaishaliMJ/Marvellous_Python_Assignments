"""-----------------------------------------------------------------------------------------------------
                          Assignment 32
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Predict whether a news article is Fake or Real using text classification technique.
                  This assignment dmonstrates the power of ensemble learning using a voting classifier 
                  with models like Logistic Regression ,Decision tree 

                  Testing module
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
from pathlib import Path
import joblib   
################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
TRUE_FILENAME="True.csv"
FAKE_FILENAME="Fake.csv"
DROP_COLUMNS=['subject','date']
TRANSFORM_FEATURE='text'
NEWS_VALIDITY=Path("NEWS_VALIDITY")
NEWS_VALIDITY.mkdir(exist_ok=True)
VECTORIZER_NAME="Tf-IDF_Vectorizer_Module"

"""Classification model list"""
CLF_MODEL_NAMES=["Decision Tree","Logistic Regression","Voting Classifier Hard","Voting Classifier Soft"]
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
#   Function name    :  testSampleDataOnTrainedModel
#   Description      :  This method selects a random sample from data and displays result
#   Input Params     :  model,sampleData
#   Output           :  -
#####################################################################################################
def testSampleDataOnTrainedModel(model,sampleData):
    textNews=sampleData[TRANSFORM_FEATURE]
    """Load Vectorizer"""
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
def testTrainedModelAndDisplay(df):
    sampleTestData =df.sample(n=1)
    print(BORDER)
    print(f"Selected sample data for testing is \n: {sampleTestData}")
    print(BORDER)
    """Loading saved model and sample tetsing"""
    for clf_Name in CLF_MODEL_NAMES:
        print(f"Sample testing Using : {clf_Name}")  
        #8. Load the model and test a sample
        savedAndTrainedModel=loadTrainedModel(clf_Name)
        #9. Test Model on a random sample from data set
        testSampleDataOnTrainedModel(savedAndTrainedModel,sampleTestData)
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
############################################################################################################
#  Main function 
############################################################################################################
def main():
    df=loadDataFile()
    testTrainedModelAndDisplay(df)
############################################################################################################
#Main entry point of the program
############################################################################################################
if __name__=="__main__":
    main()    