"""-----------------------------------------------------------------------------------------------------
                          Assignment 31
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement: Based on given information find whether given tumor is malignant or benign
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score,roc_curve,auc,accuracy_score,\
    classification_report,confusion_matrix,ConfusionMatrixDisplay,\
    recall_score,f1_score,precision_score
from sklearn.preprocessing import StandardScaler,LabelEncoder


BORDER="-"*60
"""--------------------------------------------------------------------------------------------------------
Tasks : 1. Load and explore data set
        1.1 Load data using pandas
        1.2 Handle missing or unknown values
        1.3 Display basic stats and visualise class distibution
--------------------------------------------------------------------------------------------------------"""
def LoadAndExploreDataset():
    """Step 1.1.Load the dataset using pandas"""
    df=pd.read_csv("breast_cancer.csv")
    #dataSet=datasets.load_breast_cancer()
    #print("target:",target)
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(df)
    
    """1.3 Check and handle missing or unknown values in columns"""      
    #unknownValProcessing(df)
    return df
"""---------------------------------------------------------------------------------
#  Step - 1.2, 1.3, 
#  This method loads the data set information
#  Input params : Data frame
#  Output       : Data statistics
#---------------------------------------------------------------------------------"""
def displayDatasetStatistics(df):
    """Step 1.2 Show column info and check for null values
    ------------------------------------------------""" 
    print("Data set columns details...")
    print(BORDER)
    print(df.columns)
   
    #dfBank.dropna(inplace=True)

    print(BORDER)
    """Step 1.3 Display basic statistics using .describe()
    ------------------------------------------------"""
    print("Bank details ststistics")
    print(BORDER)
    print(df.describe())
    print(BORDER)
    return df
"""---------------------------------------------------------------------------------
Task 2 : 2.1 Convert categorical variables using Label Encoding or One-Hot Encoding.
         2.2 Scale numeric features (e.g., using StandardScaler).
#---------------------------------------------------------------------------------"""
def preprocessDataSet(dfBank):
     """Encode Data set"""
     EncodeDataSet(dfBank)
     print(dfBank.head())
     """load co-relation matrix"""
     displayCorrelationMatrix(dfBank)
     """Extracting Independent and dependent variables"""
     xIndependent,yDependent=prepareDataset(dfBank)
     return xIndependent ,yDependent
"""---------------------------------------------------------------------------------
# Task 2.2 Prepare data by applying scalar transformation
#  Input params: dfBank data frame
#---------------------------------------------------------------------------------"""
def prepareDataset(dfBank):
    xFeatures=dfBank.drop(columns=['diagnosis'])
    yLabel=dfBank['diagnosis']
    scalar=StandardScaler()
    x_scale=scalar.fit_transform(xFeatures)
    return x_scale,yLabel
"""---------------------------------------------------------------------------------
# Prepare data by applying label encoding
# Input params: dfBank(Bank data frame)
# Creating encoded csv file for refernce with name 'DataEncoded.csv' 
#---------------------------------------------------------------------------------"""
def EncodeDataSet(dfBank):
    #Label enconding for all data set coulmns
    for colName in dfBank.select_dtypes(include=['object']).columns:
        #print(colName)
        labelEncoder = LabelEncoder()
        dfBank[colName]=labelEncoder.fit_transform(dfBank[colName])
        dfBank[colName].unique()
    print(BORDER)
    print("Creating encoded csv file for refernce with name 'DataEncoded.csv'")
    dfBank.to_csv("DataEncoded.csv")
    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(dfBank.head())
    print(BORDER)
    return dfBank
"""---------------------------------------------------------------------------------
Step 1.4 Plot the Co-relation matrix.
#---------------------------------------------------------------------------------"""
def displayCorrelationMatrix(dfBank):
    plt.figure(figsize=(10,6))
    sns.heatmap(dfBank.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()
"""---------------------------------------------------------------------------------
    This function uses 'Decision Tree' algorithm
---------------------------------------------------------------------------------------------------------"""
def predictionUsingDecisionTree(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Decision Tree classifier Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Decision Tree")

    DTModel=DecisionTreeClassifier()
    """Bulding the model"""
    DTModel.fit(xTrainDS,yTrainDS)

    """Testing phase"""
    yPredictOutput=DTModel.predict(xTestDS)
    
    """Positive y predictions"""
    yPredictPositiveDT=DTModel.predict_proba(xTestDS)[:,1]
    """ROC-AUC Score"""
    aucScoreDT = roc_auc_score(yTestDS, yPredictPositiveDT)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreDT)


    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput,yPredictPositiveDT 
"""---------------------------------------------------------------------------------
    This function uses 'Random Forest' algorithm
---------------------------------------------------------------------------------------------------------"""
def predictionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,xIndependent):
    print(BORDER)
    print("Calculations using Random Forest Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Random Forest")

    randomForestModel=RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)

    """Bulding the model"""
    randomForestModel.fit(xTrainDS,yTrainDS)
    """Testing phase"""
    yPredictOutput=randomForestModel.predict(xTestDS)

    """Positive predictions"""
    ypredPositiveRF = randomForestModel.predict_proba(xTestDS)[:,1]

    """ROC-AUC Score"""
    aucScoreRF = roc_auc_score(yTestDS,ypredPositiveRF)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreRF)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    """Feature importance"""
    importance=pd.Series(randomForestModel.feature_importances_,index=pd.DataFrame(xIndependent).columns)

    importance=importance.sort_values(ascending=False)

    print("Feature importance:")

    importance.plot(kind="bar",figsize=(10,6),title="Feature Importance")
    plt.show()

    return yPredictOutput,ypredPositiveRF  
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
    algorithmCompareDF["Recall"].append(recall_score(yTestDS,yPredictOutput))
    algorithmCompareDF["F1 Score"].append(f1_score(yTestDS,yPredictOutput))
    algorithmCompareDF["Precision"].append(precision_score(yTestDS,yPredictOutput))

    print("Classification report...")
    print(BORDER)
    confusionMatrixReport=classification_report(yTestDS,yPredictOutput)
    print(confusionMatrixReport)


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
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()


    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("TestResults.csv")


    """ROC Curve using sub plots"""
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5)) 

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
  
"""---------------------------------------------------------------------------------
Task 3 : Train and Test using classification algorithm
         3.1 Decision Tree
         3.2 Random Forest
#---------------------------------------------------------------------------------"""
def trainClassificationModels(data,target):
   
    """Step 3 Split data set into training and testing part"""
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(data,target,test_size=0.2)
    print(xTrainDS)
    print(xTestDS)
    print(yTrainDS)
    print(yTestDS)
    algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[],\
                        "ROC-AUC Score":[],"Recall":[],"F1 Score":[],"Precision":[]}

    """Y Predictions using 'Decision Tree"""
    yPredictionDT,yPredictPositiveDT=predictionUsingDecisionTree(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
    """Y Predictions using 'Random Forest"""
    yPredictionRF,yPredictPositiveRF=predictionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,data)

    actualVsPredicted={"Actual":yTestDS,
                       "DT_Predicted":yPredictionDT,
                       "RF_Predicted":yPredictionRF,
                       "Decision Tree":yPredictPositiveDT,
                       "Random Forest":yPredictPositiveRF}
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
"""--------------------------------------------------------------------------------------------------------
Tasks :       
       Task 1. Load and explore data set
       Task 2. Preprocess the Data
       Task 3. Split the Data
       Task 4. Train Classification Models
       Task 5. Evaluate the Models
       Task 6. Visualize Results
---------------------------------------------------------------------------------------------------------"""
def BCPrediction():
    """1.Load and explore data set"""
    df=LoadAndExploreDataset()
   
    """2. Preprocess Data set"""
    xIndependent,yDependent=preprocessDataSet(df)
    #displayCorrelationMatrix(df)
    """Split data set and Train Classification Models"""
    trainClassificationModels(xIndependent,yDependent)
#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    BCPrediction()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()