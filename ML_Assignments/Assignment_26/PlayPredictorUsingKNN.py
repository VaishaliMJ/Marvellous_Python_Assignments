"""-----------------------------------------------------------------------------------------------------
                          Assignment26
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about "Weather" and "Temperature"
                  Based On this information decide whether to Play or not
---------------------------------------------------------------------------------------------------------"""                  
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="PlayPredictor.csv"
TARGET_COl="Play"
#####################################################################################################
#   Function Name   :   loadDataSet
#   Description     :   This method loads the data set from 'PlayPredictor.csv' file
#   Input params    :    -
#   Output          :   Data frame
#####################################################################################################
def loadDataSet():
    #Read csv file
    dfPlayPredictor=pd.read_csv(FILENAME)
    
    print(BORDER)
    print("Play data loaded Successfully...")
    print(dfPlayPredictor.head())
    print(dfPlayPredictor.shape)
    print(BORDER)
    return dfPlayPredictor
#####################################################################################################
#   Function Name   :   cleanDataSet
#   Description     :   This method cleans data frame
#   Input Params    :   dFPlay(Play data frame)
#   Output          :   Removes unwanted data and coulmns from data frame
#####################################################################################################
def cleanDataSet(dfPlayPredictor):
    #Drop unwanted coulmns : 'Unnamed: 0'
    dfPlayPredictor.drop(columns=['Unnamed: 0'],inplace=True)
    #Remove unwanted data
    dfPlayPredictor.dropna(inplace=True)
    print(BORDER)
    print("Play data set after removing column")
    print(dfPlayPredictor.head())
#####################################################################################################
#   Function Name   :   prepareDataset
#   Description     :   Prepare data by applying label encoding
#   Input params    :   dFPlay(Play data frame)
#   Output          :   Creating encoded csv file for refernce with name 'PlayPredictorEncoded.csv' 
#####################################################################################################
def prepareDataset(dFPlay):
    #Label enconding for all data set coulmns
    for colName in dFPlay.select_dtypes(include=['object']).columns:
        #print(colName)
        labelEncoder = preprocessing.LabelEncoder()
        dFPlay[colName]=labelEncoder.fit_transform(dFPlay[colName])
        dFPlay[colName].unique()
    print(BORDER)
    print("Creating encoded csv file for refernce with name 'PlayPredictorEncoded.csv'")
    dFPlay.to_csv("PlayPredictorEncoded.csv")
    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(dFPlay.head())
    print(BORDER)
    #return dFPlay
#####################################################################################################
#   Function Name   :   trainDataSet
#   Description     :   Train data set using KNN algorithm
#   Input params    :   xIndependent(Features : Whether,Temperature)
#                       yDependent(Label : Play)  
#   Output          :   Return model built                
#####################################################################################################
def trainDataSet(xIndependent,yDependent,KVal):
    #Using K neighbors algorithm with k as input value
    model=KNeighborsClassifier(n_neighbors=KVal)
    #Fit model
    model.fit(xIndependent,yDependent)
    return model
#####################################################################################################
#   Function Name   :   getIndepedentAndDependentCol
#   Description     :   Extracting Features/Independent and Label/Dependent variables
#   Input params    :   dFPlay(Play data Frame)
#   Output          :   xIndependent,yDependent variables
#####################################################################################################
def getIndepedentAndDependentCol(dFPlay):
    xIndependent=dFPlay.drop(columns=[TARGET_COl])
    yDependent=dFPlay[TARGET_COl]
    return xIndependent,yDependent
#####################################################################################################
#   Function Name   :   testData
#   Description     :   This method predicts the result
#   Input params    :   model  (Built model object)
#                       x_test (sample data set )
#   Output          :   y_predict (Predicted output values)
#####################################################################################################
def testData(model,x_test):
    #Predict the result
    y_predict=model.predict(x_test)  
    return y_predict   
##################################################################################################### 
#   Function Name   :   deocdeResultDataset
#   Description     :   This method Decodes result 
#   Input params    :   predictedResult (Predicted encode result values)
#   Output          :   predictedResult (Predicted decoded result values)
#####################################################################################################
def deocdeResultDataset(predictedResult): 
    #print("1",predictedResult)  
    resultMapping={1:"Yes",0:"No"}
    """Decoding of predicted values"""
    #predictedResult.replace({'PlayPredict':resultMapping},inplace=True)
    predictedResult['PlayPredict_Decode']=predictedResult['PlayPredict'].apply(lambda x: "Yes" if x==1 else "No")

    #print("\n",predictedResult)
    return predictedResult
#####################################################################################################  
#   Function Name   :   decodePredictedResult
#   Description     :   This method decodes the predicted result values
#   Input Params    :   y_predict      (Predicted y values)
#                       sampleTestData (Sample test data set)  
#####################################################################################################
def decodePredictedResult(y_predict,sampleTestData):
    sampleTestData['PlayPredict']=y_predict
    #print("Created data frame for predicted result :")
    #print(predictDataFrame)
    """Decode predicted result """
    predictedResult=deocdeResultDataset(sampleTestData)
    #for cnt in predictedResult.index:
        #print("Predicted answer is :",predictedResult['PlayPredict'][cnt])
    print(BORDER)    
    print("Predicted Results for Sample data are:")
    print(BORDER)    
    print(predictedResult)
    print(BORDER)    
  
#####################################################################################################
#   Function Name   :   checkAccuracy
#   Description     :   This method checks the accuracy of the model for various 'K' values
#   Input Params    :   dFPlay(Play Data Frame)
#####################################################################################################

def checkAccuracy(dFPlay):
    print("Checking model accuracy......")
    print("Dividing Data set int 50% Train And 50% Test data set")
    print(BORDER)
    """Extracting featues and labels"""
    xIndependent,yDependent=getIndepedentAndDependentCol(dFPlay)
    """Splitting the data set in Training : 50% Test : 50%"""
    x_train,x_test,y_train,y_test=train_test_split(xIndependent,yDependent,test_size=0.5,random_state=42)
        
    """Creating dictionary for {k,Accuracy} values"""
    accuracyScoreDict={'k':[],'accuracy':[]}
    """Selcting range values for 'k'"""
    k_range=range(1,16)
    for k in k_range:
        
        """Build model for various values of K"""
        model=trainDataSet(x_train,y_train,k)
        """Predicting test data values"""
        y_predict=testData(model,x_test)
        """Calculating Accuracy Values"""
        accuracy=accuracy_score(y_test,y_predict)
        """Storing 'k' and 'Accuracy' values in dictionary"""
        accuracyScoreDict['k'].append(k)
        accuracyScoreDict['accuracy'].append(accuracy*100)
        
    print(BORDER)    
    print("Accuracy Scores are :")
    print(BORDER)    
    accuracyDF=pd.DataFrame(accuracyScoreDict)
    print(accuracyDF)

    best_k=k_range[accuracyScoreDict["accuracy"].index(max(accuracyScoreDict["accuracy"]))]
    print("Best value of k is :",best_k) 

    cm=confusion_matrix(y_test,y_predict)
    print("Confusion matrix :\n",cm)
   
    """Plot accuracy points"""
    plotAccuracyGraph(accuracyDF)

#####################################################################################################
#   Function Name   :   plotAccuracyGraph
#   Description     :   Plotting Accuracy VS 'K' value model
#   Input Params    :   plotAccuracyGraph
#####################################################################################################  
def plotAccuracyGraph(accuracyDF):  
    plt.figure(figsize=(8,5))
    plt.plot(accuracyDF["k"],accuracyDF['accuracy'],marker='o',linestyle="--")

    plt.title("Accuracy VS K Value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(accuracyDF["k"])
    plt.show()
#####################################################################################################
#  Main function 
#####################################################################################################
def main():
    """Step-1 : Get the data
    -----------------------"""
    #Play predictor data set
    dFPlay=loadDataSet()

    """Step-2 : Clean,Prepare and Manipulate the data
    #--------------------------------------------------"""
    #Clean,Prepare and Manipulate data
    #Clean Data : drop unwanted columns
    cleanDataSet(dFPlay)
    #Prepare Data using label encoding
    prepareDataset(dFPlay)

    """Step-3 : Train and test data
    #-----------------------
    #Train data set 
    #Extracting Independent and dependent variables"""
    xIndependent,yDependent=getIndepedentAndDependentCol(dFPlay)
    """Training the model with whole data set and k value as 3"""
    model=trainDataSet(xIndependent,yDependent,3)
    print("Model build successfully......")

    """Step-4 : Test Data
    #-----------------------
    #Test Sample Data set and predict output
    #create sample test data
    # 1. Build data frame 
    # Selecting 5 random rows from CSV file as sample data"""
    sampleTestData = dFPlay.sample(n=5) 
    #sampleTestData=pd.DataFrame({'Whether':[0,1,2],'Temperature':[0,1,2]})
    print(BORDER)
    print("Testing model with small sample data set.....")
    print("Randomly selected 5 sample Test Data from CSV:")
    print(BORDER)

    print(sampleTestData)
    """2. Test model with sample test data"""
    y_predict=testData(model,sampleTestData.drop(columns=['Play']))
    """3. Decode predicted result """
    decodePredictedResult(y_predict,sampleTestData)

    """Step-5 : Calculate Accuracy
    #--------------------------------"""
    checkAccuracy(dFPlay)
########################################################################################################
#Main entry point of the program
########################################################################################################

if __name__=="__main__":
    main()
########################################################################################################
