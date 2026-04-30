"""-----------------------------------------------------------------------------------------------------
                          Assignment 62 - 2
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Write a python program to demonstrate ReLu and Max Pooling
                  Tasks:
                  1.    Create a feature map with positive and negative values
                  2.    Apply ReLu
                  3.    Apply 2*2 max pooling
                  4.    Display output after each step
                  5.    Explain why pooling reduces size  
--------------------------------------------------------------------------------------------------------"""
import numpy as np

BORDER="-"*65

####################################################################################################
#   Function Name   :   featureMap
#   Input Params    :   None
#   Output Params   :   Feature Map
#   Description     :   Feature map display
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def displayfeatureMap():
    featureMap=np.array([
        [ 3., 3.,  3.],
        [ 0.,  0.,  0.],
        [-3., -3., -3.]
        ])
    print(BORDER)
    print("Feature Map After Convolution Operation")
    print(BORDER)
    print(featureMap)
    return featureMap
####################################################################################################
#   Function Name   :   relu_activation
#   Input Params    :   featureMap
#   Output Params   :   Feature Map after relu
#   Description     :   Relu is applied on Feature map 
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def relu_activation(featureMap):
    print(BORDER)
    print("ReLu Activation Function")
    print(BORDER)

    relu_output = np.maximum(0, featureMap)

    print("Input to ReLU:")
    print(featureMap)
    print(BORDER)
    print("\nRule : ReLU(x) = max(0, x)")
    print("\nOutput after ReLU:")
    print(BORDER)

    print(relu_output)

    return relu_output
####################################################################################################
#   Function Name   :   max_pooling
#   Input Params    :   inputData
#   Output Params   :   Feature Map after relu
#   Description     :   Relu is applied on Feature map 
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def max_pooling(inputData):
    print(BORDER)
    print("Max Pooling Function")
    print(BORDER)
    row,col=inputData.shape
    outputRows = row // 2
    outputCols = col // 2

    outputPooling = np.zeros((outputRows, outputCols))
    
    rCnt = 0
    for i in range(0, row, 2):
        cCnt = 0
        for j in range(0, col, 2):

            block = inputData[i:i+2, j:j+2]

            # Skip incomplete blocks if any
            if block.shape != (2, 2):
                continue

            max_value = np.max(block)
            outputPooling[rCnt][cCnt] = max_value

            print(f"\nPooling Block position -> Row:{rCnt} Column:{cCnt}")
            print("\nSelected 2x2 Block:")
            print(block)

            print("\nMaximum value selected =", max_value)

            cCnt += 1
        rCnt += 1

    print("\nFinal Pooling Output:")
    print(outputPooling)

    return outputPooling
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    featureMap=displayfeatureMap()
    relu_output=relu_activation(featureMap)
    max_pooling(relu_output)
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    
