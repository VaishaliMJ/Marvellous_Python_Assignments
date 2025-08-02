"""-----------------------------------------------------------------------------------------------------
                          Assignment 30
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:A Portuguese bank conducted marketing campaigns to promote term deposit subscriptions. The goal is to
predict whether a client will subscribe (yes or no) to a term deposit based on their profile and campaign
interaction details.
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure,show
import matplotlib.pyplot as plt
from seaborn import countplot
import seaborn as sns
from numpy import nan
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
from sklearn.metrics import precision_score,recall_score,f1_score,roc_curve,auc,roc_auc_score
from sklearn.preprocessing import StandardScaler,LabelEncoder

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
"""---------------------------------------------------------------------------------
#  Step - 1.2, 1.3, 
#  This method loads the data set information
#  Input params : Data frame
#  Output       : Data statistics
#---------------------------------------------------------------------------------"""
def displayDatasetStatistics(dfBank):
    
    """Step 1.2 Show column info and check for null values
    ------------------------------------------------""" 
    print("Data set columns details...")
    print(BORDER)
    print(dfBank.columns)
   
    #dfBank.dropna(inplace=True)

    print(BORDER)
    """Step 1.3 Display basic statistics using .describe()
    ------------------------------------------------"""
    print("Bank details ststistics")
    print(BORDER)
    print(dfBank.describe())
    print(BORDER)
    return dfBank
"""---------------------------------------------------------------------------------
Step 1.3 Check and handle missing or unknown values in columns
Input params :  dfBank(Data frame set)
-----------------------------------------------------------------------------------"""
def unknownValProcessing(dfBank):
    print("\t\tunknown values in column report")
    print(BORDER)
    colUnknown=[]
    colZero=[]
    unknownZeroValuesDF={"ColName":[],"Unknown Value Count":[],"Zero Value Count":[]}
    #unknownZeroValuesDF={"ColName":[],"Unknown Value Count":[]}

    for colName in dfBank.columns:
        unknownValCount=(dfBank[colName]=='unknown').sum()
        unknownZeroValuesDF['ColName'].append(colName)
        unknownZeroValuesDF["Unknown Value Count"].append(unknownValCount)

        zeroValCount=(dfBank[colName]==0).sum()
        #unknownZeroValuesDF['ColName'].append(colName)
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

    #print(dfBank)

    #sns.countplot(dfBank['poutcome'])
    #sns.countplot(dfBank['job'])
    #sns.countplot(dfBank['education'])
    #sns.countplot(dfBank['contact'])

    print(dfBank)
    dfBank.to_csv("replacedUnknownValues.csv")
    print(dfBank.shape)
"""---------------------------------------------------------------------------------
Step 1.4 Plot the Co-relation matrix.
#---------------------------------------------------------------------------------"""
def displayCorrelationMatrix(dfBank):
    plt.figure(figsize=(10,6))
    sns.heatmap(dfBank.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()
"""---------------------------------------------------------------------------------
# Prepare data by applying label encoding
# Input params: dfBank(Bank data frame)
# Creating encoded csv file for refernce with name 'BankTermDataEncoded.csv' 
#---------------------------------------------------------------------------------"""
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
"""--------------------------------------------------------------------------------------------------------
Tasks : 1. Load and explore data set
        1.1 Load data using pandas
        1.2 Handle missing or unknown values
        1.3 Display basic stats and visualise class distibution
--------------------------------------------------------------------------------------------------------"""
def LoadAndExploreDataset():
    """Step 1.1.Load the dataset using pandas"""
    dfBankDeposit=loadDataFile("bank-full.csv")
    """Step 1.2 Handle missing or unknown values"""
    displayDatasetStatistics(dfBankDeposit)
    
    """1.3 Check and handle missing or unknown values in columns su"""      
    unknownValProcessing(dfBankDeposit)
    return dfBankDeposit

"""---------------------------------------------------------------------------------
# Task 2.2 Prepare data by applying scalar transformation
#  Input params: dfBank data frame
#---------------------------------------------------------------------------------"""
def prepareDataset(dfBank):
    xFeatures=dfBank.drop(columns=['y'])
    yLabel=dfBank['y']
    scalar=StandardScaler()
    x_scale=scalar.fit_transform(xFeatures)
    return x_scale,yLabel
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
"""---------------------------------------------------------------------------------------------------------
    Task 3.1 This function uses Logistic Regression algorithm
---------------------------------------------------------------------------------------------------------"""
def bankTermSubscriptionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Logistic Regression Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Logistic Regression")
    logModel=LogisticRegression()
    """Build the model"""
    logModel.fit(xTrainDS,yTrainDS)
    """Testing the model"""
    yPredictOutput=logModel.predict(xTestDS)

    """Positive Predictions"""
    y_predPositiveClassLR = logModel.predict_proba(xTestDS)[:, 1]
    """ROC-AUC Score"""
    aucScoreLR = roc_auc_score(yTestDS, y_predPositiveClassLR)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreLR)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)

    return yPredictOutput,y_predPositiveClassLR
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

"""---------------------------------------------------------------------------------------------------------
    This function uses KNN algorithm
---------------------------------------------------------------------------------------------------------"""
def bankTermSubscriptionUsingKNN(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,k=3):
    print(BORDER)
    print("Calculations using KNN Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("KNN")

    kNNModel=KNeighborsClassifier(n_neighbors=k)
    """Bulding the model"""
    kNNModel.fit(xTrainDS,yTrainDS)

    """Testing phase"""
    yPredictOutput=kNNModel.predict(xTestDS)
    
    """Positive y predictions"""
    yPredictPositiveKNN=kNNModel.predict_proba(xTestDS)[:,1]
    """ROC-AUC Score"""
    aucScoreKNN = roc_auc_score(yTestDS, yPredictPositiveKNN)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreKNN)


    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput,yPredictPositiveKNN 
"""---------------------------------------------------------------------------------------------------------
    This function uses Random Forest algorithm
---------------------------------------------------------------------------------------------------------"""
def bankTermSubscriptionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,xIndependent):
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
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt], 
                                             display_labels=["Subscribed","Non Subscribed"])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()


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
"""---------------------------------------------------------------------------------
Task 3 : Train and Test using classification algorithm
         3.1 Logistic Regression
         3.2 KNN Algorithm
         3.3 Random Forest
#---------------------------------------------------------------------------------"""
def trainClassificationModel(xIndependent,yDependent):

    """Step 3 Split data set into training and testing part"""
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xIndependent,yDependent,test_size=0.2,random_state=42)
    
    algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[],"ROC-AUC Score":[]}
    
    """YPredictions Calculations using 'Logistic Regression' """
    yPredictedLR,ypredPositiveLR=bankTermSubscriptionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
   
    """YPredictions using 'KNN """
    yPredictedKNN,yPredictPositiveKNN=bankTermSubscriptionUsingKNN(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,3)
   
    """Y Predictions using 'Random Forest"""
    yPredictionRF,yPredictPositiveRF=bankTermSubscriptionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,xIndependent)

    actualVsPredicted={"Actual":yTestDS,
                       "RF":yPredictionRF,
                       "KNN":yPredictedKNN,
                       "LR":yPredictedLR,
                       "Logistic Regression":ypredPositiveLR,
                       "KNN":yPredictPositiveKNN,
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
Tasks :Task 1. Load and explore data set
       Task 2. Preprocess the Data
       Task 3. Split the Data
       Task 4. Train Classification Models
       Task 5. Evaluate the Models
       Task 6. Visualize Results
--------------------------------------------------------------------------------------------------------"""
def BankTermDepositSubscriptionPrediction():
    """1.Load and explore data set"""
    dfBankDeposit=LoadAndExploreDataset()
    """2. Preprocess Data set"""
    xIndependent,yDependent=preprocessDataSet(dfBankDeposit)
    
    """Split data set and Train Classification Models"""
    trainClassificationModel(xIndependent,yDependent)

#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
    BankTermDepositSubscriptionPrediction()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()