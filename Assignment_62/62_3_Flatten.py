"""-----------------------------------------------------------------------------------------------------
                          Assignment 62-3
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Write a python program to show flattening
                   Tasks:
                   1.   Take a 2D Matrix
                   2.   Convert it into 1D vector
                   3.   Pass it to fully connected layer
                   4.   Calculate final output manually
                   5.   Explain the role of flatten layer in CNN
--------------------------------------------------------------------------------------------------------"""
import numpy as np
import random
BORDER="-"*65
####################################################################################################
#   Function Name   :   get2D_Data
#   Input Params    :   None
#   Output Params   :   2D Data
#   Description     :   2D Data display
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def get2D_Data():
    two_D_Data=np.array([
        [6,4],
        [8,6]
    ])
    print(BORDER)
    print("2D Data")
    print(BORDER)
    print(two_D_Data)
    
    flatData = two_D_Data.flatten()
    print(BORDER)
    print("Flattened 1D Data")
    print(BORDER)
    print(flatData)
    
    
    return flatData
#####################################################################################################
#   Function Name   :   generateWeights
#   Input Params    :   size of array
#   Output Params   :   weights
#   Description     :   Genrates weights randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################

def generateWeights(size):
    weights = np.round(np.random.uniform(0,1,size=(size,)),1)
   
    print(BORDER)
    print(f"\n\nRandom weigths:{weights}")
    return weights
#####################################################################################################
#   Function Name   :   generateBias
#   Input Params    :   None
#   Output Params   :   bias
#   Description     :   Genrates bias randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateBias():
    bias=round(random.uniform(-1, 1),1)    
    print(f"\n\nBias:{bias}")
    print(BORDER)
    return bias
####################################################################################################
#   Function Name   :   process_FC_Layer
#   Input Params    :   1D data
#   Output Params   :   output
#   Description     :   Fully connected layer output
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def process_FC_Layer(flat_Data):
    print(BORDER)
    print("Process Fully Connected Layer")
    
    weights=generateWeights(flat_Data.size)
    bias=generateBias()
    
    multiplication = flat_Data * weights
    result = np.sum(multiplication) + bias

    print("Input * Weights + bias:")

    print(f"\n\n{flat_Data}*{weights} = {np.sum(multiplication)}")
    print("\n\nFinal Output")

    print(f"\n{flat_Data} * {weights} + ({bias}) = {round(result,2)}")

    print(BORDER)


#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    flat_Data=get2D_Data()

    process_FC_Layer(flat_Data)
    




#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    
