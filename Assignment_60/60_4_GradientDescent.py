
"""-----------------------------------------------------------------------------------------------------
                    Assigment 60-4
                    Gradient Descent Backpropogation
                    (Student name - Vaishali Jorwekar)
--------------------------------------------------------------------------------------------------------
Problem statement: Gradient Descent Backpropogation
--------------------------------------------------------------------------------------------------------"""
import random,math
import numpy as np
import matplotlib.pyplot as plt
BORDER="-"*65
TARGET=1.0
LEARNING_RATE=0.01
EPOCHS=10
#####################################################################################################
#   Function Name   :   sigmoid
#   Input Params    :   z
#   Output Params   :   max(0,z)
#   Description     :   sigmoid Activation function
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

#####################################################################################################
#   Function Name   :   Sigmoid_Derivative
#   Input Params    :   zoutput
#   Output Params   :   max(0,z)
#   Description     :   Derivative of sigmoid,
#                       If output = sigmoid(z), then derivative = output * (1 - output)
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Sigmoid_Derivative(output):
    return output * (1 - output)
#####################################################################################################
#   Function Name   :   Calculate_GD
#   Input Params    :   x1,x2,w1,w2,b
#   Output Params   :   MSE
#   Description     :   MSE calculations
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Calculate_GD(x1,x2,w1,w2,b):
    
    # =========================
    # Step 1: Forward Propagation
    # =========================

    # Weighted sum
    z = (x1 * w1) + (x2 * w2) + b
        
    output=sigmoid(z)
    # =========================
    # Step 2: Loss Calculation
    # =========================

    # Using Mean Squared Error for one sample
    # Loss = 0.5 * (target - output)^2
    loss = 0.5 * (TARGET - output) ** 2
        
    # =========================
    # Step 3: Backpropagation
    # =========================

    # Derivative of loss with respect to output
    # dL/doutput = output - target
    dL_doutput = output - TARGET
        
    # Derivative of output with respect to z
    # doutput/dz = sigmoid'(z) = output * (1 - output)
    doutput_dz = Sigmoid_Derivative(output)

    # Chain rule:
    # dL/dz = dL/doutput * doutput/dz
    dL_dz = dL_doutput * doutput_dz
    # Gradients with respect to weights and bias
    # z = x1*w1 + x2*w2 + b
    # dz/dw1 = x1
    # dz/dw2 = x2
    # dz/db = 1
    dL_dw1 = dL_dz * x1
    dL_dw2 = dL_dz * x2
    dL_db = dL_dz
        
    # =========================
    # Step 4: Gradient Descent
    # =========================

    # Update weights and bias
    w1 = w1 - (LEARNING_RATE * dL_dw1)
    w2 = w2 - (LEARNING_RATE * dL_dw2)
    b = b - (LEARNING_RATE * dL_db)
        
        
    # =========================
    # Display all values
    # =========================
    
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output :", round(output, 4))
    print("Target Output    :", TARGET)
    print("Loss             :", round(loss, 6))
    print("Gradient dL/dw1  :", round(dL_dw1, 6))
    print("Gradient dL/dw2  :", round(dL_dw2, 6))
    print("Gradient dL/db   :", round(dL_db, 6))
    print("Updated w1       :", round(w1, 6))
    print("Updated w2       :", round(w2, 6))
    print("Updated b        :", round(b, 6))
    print(BORDER)
    
    print("Final Trained Values")
    print("w1 =", round(w1, 6))
    print("w2 =", round(w2, 6))
    print("b  =", round(b, 6))    
    
#####################################################################################################
#   Function Name   :   generateWeights
#   Input Params    :   None
#   Output Params   :   weights
#   Description     :   Genrates weights randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateWeights():
    w1=round(random.uniform(-1,1),1)
    w2=round(random.uniform(-1,1),1)
    return w1,w2
#####################################################################################################
#   Function Name   :   generateBias
#   Input Params    :   None
#   Output Params   :   weights
#   Description     :   Genrates bias randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateBias():
    bias=round(random.uniform(-1, 1),1)
    return bias
#####################################################################################################
#   Function Name   :   generategenerateData
#   Input Params    :   None
#   Output Params   :   inputs,weights,bias
#   Description     :   Genrates inputs,wts and bias randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateInput():
    
    x1=random.randint(0,1)
    x2=random.randint(0,1)
    
    return x1,x2
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    x1,x2=generateInput()
    w1,w2=generateWeights()
    b=generateBias()
    print(BORDER)
    print("Initial Values")
    print(BORDER)
    print(f"x1  =   {x1}")
    print(f"x2  =   {x2}")
    print(f"w1  =   {w1}")
    print(f"w2  =   {w2}")
    print(f"b   =   {b}")
    Calculate_GD(x1,x2,w1,w2,b)
    print(BORDER)
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    

