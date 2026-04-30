"""-----------------------------------------------------------------------------------------------------
                          Assignment 61 - 1
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Create a neural network model to predict whether a customer
                  will a service   
                  Tasks:
                  1.    Load and Create dataset
                  2.    Clean The dataset
                  3.    Apply Standard Scalar
                  4.    Train FNN model
                  5.    Evaluate Accuracy    
--------------------------------------------------------------------------------------------------------"""
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
# Features :  
# Age   Monthly Charges   Tenure      Number Of Complaints    
# Customer Support Calls
      X=[
            [25,500,12,1,2],
            [30,700,24,0,1],
            [45,1200,6,5,8],
            [50,1500,5,6,10],
            [28,600,18,1,1],
            [35,800,30,0,0],
            [48,1400,4,7,9],
            [52,1600,3,8,12],
            [27,550,20,0,1],
            [42,1300,8,4,7]  
      ]
      #     0     Customer will stay
      #     1     Customer will leave
      
      y=[ 0,0,1,1,0,0,1,1,0,1 ]

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
      columns = ['Age', 'Monthly_Spend', 'Tenure', 'Support_Calls', 'Complaints']
      df=pd.DataFrame(X,columns=columns)
      df["Target"]=y
      print(df)
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

    
    #y_train_scaled = scaler_y.fit_transform(yTrain).reshape(-1,1).ravel()
    #y_test_scaled  = scaler_y.transform(yTest).reshape(-1,1).ravel()
    
    #y_train_scaled = scaler_y.fit_transform(yTrain).reshape(-1, 1)
    #y_test_scaled  = scaler_y.transform(yTest).reshape(-1, 1)
    
    
    return X_train_scaled,X_test_scaled,scaler_X
      
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
            max_iter=1000,
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
    # New Customer Prediction
    # Age                     =     46
    # Monthly Charges         =     1450  
    # Tenure                  =     5      
    # Number Of Complaints    =     6    
    # Customer Support Calls  =     9
    # ----------------------------------------------------
    print(BORDER)
    print(f"Customer With Data Prediction:")
    print(BORDER)
    print(f"Age                     =     46")
    print(f"Monthly Charges         =     1450") 
    print(f"Tenure                  =     5")    
    print(f"Number Of Complaints    =     6")    
    print(f"Customer Support Calls  =     9")
    new_Customer = [[46,1450,5,6,9]]
    new_cust_scaled = scaler_X.transform(new_Customer)

    cust_Prediction = model.predict(new_cust_scaled)
    
    if(cust_Prediction[0]==0):
          result="Customer Will Stay"
    else:
          result="Customer Will Leave"
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
      #predictions=scaler_y.inverse_transform(pred_scaled.reshape(-1,1)).ravel()
    
      print("Customer Stay Actual    :", yTest)
      print("Predicted Customer Stay Prediction  :", predictions)
      # Error
      error = mean_absolute_error(yTest, predictions)
      print("\nAverage Error:", error)
      
      testNewData(scaler_X,yTrain,model)
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    
