"""-----------------------------------------------------------------------------------------------------
                          Assignment 62 - 1
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Write a python program to manually perform convolution
                  Tasks:
                  1.    Move kernel over image
                  2.    Perform muliplication and addition
                  3.    Generate feature map
                  4.    Print each region calculation
--------------------------------------------------------------------------------------------------------"""
import numpy as np

BORDER="-"*65

####################################################################################################
#   Function Name   :   generateImageData
#   Input Params    :   None
#   Output Params   :   Image Matrix
#   Description     :   Input image
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateImageData():
    image=np.array([
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ])
    print(BORDER)
    print("5*5 Image Data")
    print(BORDER)
    print(image)
    return image
####################################################################################################
#   Function Name   :   generateKernel
#   Input Params    :   None
#   Output Params   :   Kernel matrix
#   Description     :   Kernel Matrix
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateKernel():
    kernel=np.array([
        [-1,-1,-1],
        [0,0,0],
        [1,1,1]
    ])
    
    
    print(BORDER)
    print("3*3 Kernel Data")
    print(BORDER)
    print(kernel)    
    return kernel
####################################################################################################
#   Function Name   :   convolutionOperation
#   Input Params    :   image,kernel
#   Output Params   :   Feature Map
#   Description     :   Feature map is generated
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def convolutionOperation(image,kernel):
    #   Output Size = (Image Size-Kernel Size+1) x (Image Size-Kernel Size+1) 
    #               =  (5-3+1)*(5-3+1)=3*3
    imageSize=image.shape
    kernelSize=kernel.shape
    
    row=imageSize[0]-kernelSize[0]+1
    col=imageSize[1]-kernelSize[1]+1

    
    feature_map = np.zeros((row,col))
    regionResult=""
    #print(BORDER)
    #print("Calculations")
    #print(BORDER)
    for i in range(row):
        for j in range(col):

            # Extract 3x3 region
            region = image[i:i+3, j:j+3]
            
            #print(f"\nImage selected region ")
            #print(BORDER)
            #print(f"{region}")
            #print(BORDER)
            #regionResult=regionResult+f"{region[i][j]}*{kernel[i][j]} + "
            # Multiply and Sum
            result = np.sum(region * kernel)
            
            # Store result
            feature_map[i][j] = result  
        #print(f"{regionResult.rstrip(" + ")}={result}")     
        #print()    
    return feature_map

####################################################################################################
#   Function Name   :   matrix_multiplication_Display
#   Input Params    :   image,kernel
#   Output Params   :   multiplication
#   Description     :   Result of matrix multiplication
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def matrix_multiplication_Display(image,kernel):
    pass
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    image=generateImageData()
    kernel=generateKernel()
    feature_map=convolutionOperation(image,kernel)
    
    print(BORDER)
    print("\nFeature Map (Detected Edge)")
    print(BORDER)
    print(feature_map)
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    
