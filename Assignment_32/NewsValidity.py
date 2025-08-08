"""-----------------------------------------------------------------------------------------------------
                          Assignment 32
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Predict whether a news article is Fake or Real using text classification technique.
                  This assignment dmonstrates the power of ensemble learning using a voting classifier 
                  with models like Logistic Regression ,Decision tree 
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,\
      accuracy_score,f1_score,roc_auc_score,auc,recall_score,precision_score,ConfusionMatrixDisplay,roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
import matplotlib.pyplot as plt

BORDER="-"*50
"""---------------------------------------------------------------------------------
#  Step 1.1 This method loads the data set from 'True.csv' and 'Fake.csv' files
#  Step 1.2 Add 'label' column to both dataFrames Fake=0, True=1
#  Step 1.3 Combine both datasets
#  Input params : Data file paths
#  Output       : Data frame
#---------------------------------------------------------------------------------"""
def loadDataFile(trueNewsFilePath,fakeNewsFilePath):
    """Step-1.1  Load And read CSV data file
    ------------------------------------------------"""
    dfTrue=pd.read_csv(trueNewsFilePath)
    dfFake=pd.read_csv(fakeNewsFilePath)
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
"""---------------------------------------------------------------------------------
#  Step 1.3     Drop null values 
   Step 1.4    Use only the relevent columns
#  Input params : Data frame
#  Output       : Data statistics
#---------------------------------------------------------------------------------"""
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
    dfNews.drop(columns=['subject','date'],inplace=True) 
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
"""--------------------------------------------------------------------------------------------------------
Tasks : 1.1 Load both fake.csv and True.csv
        1.2 Add 'Label' column to both 
        1.3 Combine both datasets
        1.4 Use only the relevent columns
--------------------------------------------------------------------------------------------------------"""
def LoadAndExploreDataset():
    """Step 1.1 Load the dataset using pandas"""
    dfNews=loadDataFile("True.csv","Fake.csv")
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(dfNews)
    
    """1.3 Check and handle missing or unknown values in columns su"""      
    #unknownValProcessing(dfNews)
    return dfNews
"""--------------------------------------------------------------------------------------------------------
      Converting text into number format using TF-IDF method
--------------------------------------------------------------------------------------------------------"""
def featureExtraction(dfNews):
    vectorizer = TfidfVectorizer()
    #dfNews['combinedTitleText']=dfNews['title']+dfNews['text'] 
    transformedFeatures=vectorizer.fit_transform(dfNews['text'])
    featursNames = vectorizer.get_feature_names_out()
    #print(transformedData)
    #print(feature_names)
    #convertedTFIDF = pd.DataFrame(transformedFeatures.toarray(), columns=featursNames)  
    #convertedTFIDF.to_csv("ConvertedToTFIDF.csv")
    # Create a DataFrame to display the TF-IDF matrix
       #df_tfidf = pd.DataFrame(data=data_Matrix.toarray(), columns=feature_names)
    return transformedFeatures
"""---------------------------------------------------------------------------------
    This function uses 'Decision Tree' algorithm
---------------------------------------------------------------------------------------------------------"""
def newsPredictionUsingDecisionTree(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Decision Tree classifier Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Decision Tree")

    DTModel=DecisionTreeClassifier()
    """Bulding the model"""
    DTModel.fit(xTrainDS,yTrainDS)

    """Testing phase"""
    yPredictOutput=DTModel.predict(xTestDS)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput 
"""---------------------------------------------------------------------------------
    This function uses 'Logistic Regression' algorithm
---------------------------------------------------------------------------------------------------------"""
def newsPredictionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using 'Logistic Regression' classifier Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Logistic Regression")

    LRModel=LogisticRegression()
    """Bulding the model"""
    LRModel.fit(xTrainDS,yTrainDS)

    """Testing phase"""
    yPredictOutput=LRModel.predict(xTestDS)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput 
"""--------------------------------------------------------------------------------------------------------
      Voting classifier calculations
--------------------------------------------------------------------------------------------------------"""
def buildModelUsingVectorClassification(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,votingName):
    print(f"Calculations using {votingName} Voting classifier")
    print(BORDER)
    print(BORDER)
    name=votingName+" Voting Classifier"
    algorithmCompareDF["Algorithm Name"].append(name)
    LRModel=LogisticRegression()
    DTModel=DecisionTreeClassifier()
    KNNModel=KNeighborsClassifier(n_neighbors=5)
  
    votingClf=VotingClassifier(
        estimators=[
            ('lr',LRModel),
            ('dt',DTModel),
            ('knn',KNNModel)],
            voting=votingName)          
    votingClf.fit(xTrainDS,yTrainDS)

    yPredictVC=votingClf.predict(xTestDS)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictVC,algorithmCompareDF)  

    return yPredictVC
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

    print("Classification report...")
    print(BORDER)
    confusionMatrixReport=classification_report(yTestDS,yPredictOutput)
    print(confusionMatrixReport)

"""--------------------------------------------------------------------------------------------------------
Task 3: 3.1 Spilt the data set into tarining and testing data
        3.2 Train model using 'Logistic Regression' and 'Decision Tree Classifier'    
--------------------------------------------------------------------------------------------------------"""
def modelTrainingAndTesting(xIndependent,yDependent):
    """Step 3 Split data set into training and testing part"""
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xIndependent,yDependent,test_size=0.2,random_state=42)
    
    algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[]}
    
    """YPredictions Calculations using 'Logistic Regression' """
    yPredictedLR=newsPredictionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
   
    """YPredictions Calculations using 'Decision Tree' """
    yPredictedDT=newsPredictionUsingDecisionTree(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
   
    """Model training using ensemble method"""
  
    yPredictedVCHard=buildModelUsingVectorClassification(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,'hard')
    yPredictedVCSoft=buildModelUsingVectorClassification(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,'soft')

    actualVsPredicted={"Actual":yTestDS,
                       "DT_Predicted":yPredictedDT,
                       "LR_Predicted":yPredictedLR,
                       "HVC Predicted":yPredictedVCHard,
                       "SVC Predicted":yPredictedVCSoft}
    print(BORDER)
    print("\t\tComparision matrix for all algorithm....")
    print(BORDER)
    algoDetails=pd.DataFrame(algorithmCompareDF)
    print(algoDetails)
    print("Predicted....")
    predictedDF=pd.DataFrame(actualVsPredicted,)
    print(BORDER)
    """Plotting comparision"""
    plotAndCompareConfusionMatrixROC(algoDetails,predictedDF)
"""---------------------------------------------------------------------------------------------------------
    comparision based on accuracy
---------------------------------------------------------------------------------------------------------"""
def plotAndCompareConfusionMatrixROC(algorithmCompareDF,actualVsPredicted):
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
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(22, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()

    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("TestResults.csv")
"""--------------------------------------------------------------------------------------------------------
Tasks: Task 1 : Data Preprocessing
       Task 2 : Feature Extraction
       Task 3 : Model Training
       Task 4 : Evaluation
--------------------------------------------------------------------------------------------------------"""
def newsValidityPrediction():
    """1.Load and explore data set"""
    dfNews=LoadAndExploreDataset()
    """2.Use TF-IDF vectorization to convert text into numerical features  """
    features=featureExtraction(dfNews)
    target=dfNews['label']
    
    """Model Training"""
    modelTrainingAndTesting(features,target)
"""---------------------------------------------------------------------------------------------------------
  Main function 
---------------------------------------------------------------------------------------------------------"""
def main():
    newsValidityPrediction()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()