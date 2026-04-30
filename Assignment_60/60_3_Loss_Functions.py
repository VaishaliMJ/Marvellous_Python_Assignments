
"""-----------------------------------------------------------------------------------------------------
                    Loss Functions Calculations
                    (Student name - Vaishali Jorwekar)
--------------------------------------------------------------------------------------------------------
Problem statement: Write a program to calculate loss manually(MSE,MAE,Binary Cross Entropy)
--------------------------------------------------------------------------------------------------------"""
import random,math
import numpy as np
import matplotlib.pyplot as plt
BORDER="-"*65
#####################################################################################################
#   Function Name   :   Calculate_MSE
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Mean Squared Error Calculations
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Calculate_MSE(yTrue,yPred):
    total_loss=0
    outputLen=len(yTrue)
    for i in range(outputLen):
        error=yTrue[i]-yPred[i]
        total_loss+=error**2
    mse = total_loss / outputLen   
    return round(mse,2)

#####################################################################################################
#   Function Name   :   Calculate_BinaryCrossEntropy
#   Input Params    :   
#   Output Params   :   Binary Cross Entropy
#   Description     :   Binary Cross Entropy calculations
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Calculate_BinaryCrossEntropy():
    yTrue=np.array([random.randint(0,1),
                     random.randint(0,1),
                     random.randint(0,1)])
    
    yPred=np.array([round(random.uniform(0,1),2),
                     round(random.randint(0,1),2),
                     round(random.randint(0,1),2)])
    print(f"y and y^ values for Binary Cross Entropy")
    print(BORDER)
    print(f"y   :   {yTrue}")
    print(f"y^  :   {yPred}")
    print(BORDER)
    outputLen=len(yTrue)
    total_loss =0
    for i in range(outputLen):
        y = yTrue[i]
        p = yPred[i] 
        #Avoid 0
        p = max(min(p, 0.999), 0.001)
        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss 
    bceLoss= total_loss/outputLen     
    return round(bceLoss,2)

#####################################################################################################
#   Function Name   :   Calculate_MAE
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Mean Absolute Error Calculations
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Calculate_MAE(yTrue,yPred):
    total_loss=0
    outputLen=len(yTrue)
    for i in range(outputLen):
        error=abs(yTrue[i]-yPred[i])
        total_loss+=error
    mae = total_loss / outputLen   
    return round(mae,2)
#####################################################################################################
#   Function Name   :   generategenerateData
#   Input Params    :   None
#   Output Params   :   inputs,weights,bias
#   Description     :   Genrates inputs,wts and bias randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateData():
    actualOutput=np.array([random.randint(10,20),
                     random.randint(20,30),
                     random.randint(1,10)])
    
    predictedOutput=np.array([random.randint(10,20),
                     random.randint(20,30),
                     random.randint(1,10)])
    return actualOutput,predictedOutput
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    actualOutput,predictedOutput=generateData()
    print(BORDER)
    print(f"y and y^ values for MSE and MAE")
    print(BORDER)
    print(f"y   :   {actualOutput}")
    print(f"y^  :   {predictedOutput}")
    print(BORDER)
    mse=Calculate_MSE(actualOutput,predictedOutput)
    mae=Calculate_MAE(actualOutput,predictedOutput)
    
    print("Loss Values MSE and MAE")
    print(BORDER)

    print(f"MSE :   {mse}")
    print(f"MAE :   {mae}")
    
    print(BORDER)
    bce=Calculate_BinaryCrossEntropy()
    print(f"Binary Cross Entropy :   {bce}")
    print(BORDER)
    
    print("Summary")
    print("MSE and MAE :    Regression Problems")
    print("Binary Cross Entropry:   Binary Classification Problems")
    print(BORDER)


#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    

