"""-----------------------------------------------------------------------------------------------------
                          Assignment 61 - 2
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Create a neural network model to predict loan Approval
                   Tasks:
                   1.   Preprocesses categorical values
                   2.   Apply Scaling
                   3.   Train FNN Model
                   4.   Evaluate Model
                   5.   Predict Approval for new applicant   
-------------------------------------------------------------------------------------"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_absolute_error
BORDER="-"*65
TEST_SIZE=0.25
RANDOM_STATE=42

####################################################################################################
#   Function Name   :   generateData
#   Input Params    :   None
#   Output Params   :   Features,Labels
#   Description     :   Genrates Features and Labels
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateData():
# Features :  "Applicant Income","Credit Score","Loan Amount",
#               "Existing EMI","Employement Status"
    X=[
        [25000,600,200000,10000,0],
        [40000,700,300000,8000,1],
        [60000,750,500000,12000,1],
        [20000,550,150000,15000,0],
        [80000,800,700000,10000,1],
        [35000,650,250000,9000,1],
        [18000,500,100000,12000,0],
        [90000,850,800000,15000,1],
        [30000,580,200000,14000,0],
        [70000,780,600000,10000,1]
    ]
    y=[0,1,1,0,1,
       1,0,1,0,1]
    return X,y
####################################################################################################
#   Function Name   :   displayInputData
#   Input Params    :   None
#   Output Params   :   Features,Labels
#   Description     :   Genrates Features and Labels
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def displayInputData(X,y):
      print(BORDER)
      print(f"\t\tInput data")
      print(BORDER)
      columns = ["Applicant Income","Credit Score","Loan Amount", "Existing EMI","Employement Status"]
      df=pd.DataFrame(X,columns=columns)
      df["Target"]=y
      print(df)
#####################################################################################################
#   Function Name   :   SplitDataset
#   Input Params    :   x,y
#   Output Params   :   inputs,weights,bias
#   Description     :   Split data set
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def SplitDataset(x,y):
    xTrain,xTest,yTrain,yTest=train_test_split(x, y, 
                                               test_size=TEST_SIZE, 
                                               random_state=RANDOM_STATE)
    return xTrain,xTest,yTrain,yTest   
#####################################################################################################
#   Function Name   :   SplitDataset
#   Input Params    :   xTrain,xTest,yTrain,yTest
#   Output Params   :   inputs,weights,bias
#   Description     :   Scale Data Set
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def scaleDataSet(xTrain,xTest):

    scaler_X = StandardScaler()
    #scaler_y = StandardScaler()

    X_train_scaled = scaler_X.fit_transform(xTrain)
    X_test_scaled  = scaler_X.transform(xTest)
    
    
    return X_train_scaled,X_test_scaled,scaler_X  
#####################################################################################################    
#   Function Name   :   createFNNModel
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Create FNN model
#   Author          :   Vaishali M. Jorwekar              
##################################################################################################### 
def createFNNModel():
      #Create the Feedforward Neural Network model
      model = MLPClassifier(
            hidden_layer_sizes=(5,),#hidden_layer_sizes=(5,)
            activation='relu',
            solver='adam',
            max_iter=2000,
            random_state=RANDOM_STATE
            )
      return model 
#####################################################################################################    
#   Function Name   :   BuildModel
#   Input Params    :   X_train_scaled,X_test_scaled,y_train_scaled,model
#   Output Params   :   None
#   Description     :   Create FNN model
#   Author          :   Vaishali M. Jorwekar              
##################################################################################################### 
def BuildModel(X_train_scaled,X_test_scaled,yTrain,model):

    # Train Model
    model.fit(X_train_scaled, yTrain)

    # Predict on test data
    pred_scaled = model.predict(X_test_scaled)
    return pred_scaled  
#####################################################################################################    
#   Function Name   :   testNewData
#   Input Params    :   scaler_X,model
#   Output Params   :   None
#   Description     :   Test New emp record
#   Author          :   Vaishali M. Jorwekar              
#####################################################################################################   
def testNewData(scaler_X,model):
    # ----------------------------------------------------
    # New Customer Loan Prediction
    # Applicant Income"     =   55000
    # "Credit Score"        =   720
    # "Loan Amount"         =   400000
    # "Existing EMI"        =   10000
    # "Employement Status"  =   1
    print(BORDER)
    print("Customer Data")
    print(BORDER)
    print("Applicant Income    =   55000")
    print("Credit Score        =   720")
    print("Loan Amount         =   400000")
    print("Existing EMI        =   10000")
    print("Employement Status  =   1")
    
    custData=[[55000,720,400000,10000,1]]
    new_cust_scaled = scaler_X.transform(custData)

    cust_Prediction = model.predict(new_cust_scaled)
    
    if(cust_Prediction[0]==0):
          result="Loan Rejected"
    else:
          result="Loan Approved"
    print(BORDER)              
    print(f"\nCustomer Stay Prediction:{result}")
    print(BORDER)
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
      # Generate Data
      X,y=generateData()
      #     Display Data set
      displayInputData(X,y)
      #     Split Data set
      xTrain,xTest,yTrain,yTest=SplitDataset(X,y)
      #     Scale Data set
      X_train_scaled,X_test_scaled,scaler_X=scaleDataSet(xTrain,xTest)
      #     Create FNN Model
       
      model=createFNNModel()
      #     Build And Predict Model
      predictions=BuildModel(X_train_scaled,X_test_scaled,yTrain,model)
      print("Actual Loan Approval Status   :", yTest)
      print("Predicted Loan Approval Status  :", predictions)
      
      # Error
      error = mean_absolute_error(yTest, predictions)
      print(f"\nAverage Error:{round(error,3)}")
      
      testNewData(scaler_X,model)
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    
