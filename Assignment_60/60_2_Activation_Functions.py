
"""-----------------------------------------------------------------------------------------------------
                    Assignment 60_2
                Different Activation Functions
                (Student name - Vaishali Jorwekar)
--------------------------------------------------------------------------------------------------------
Problem statement: Write a program to Demonstrate Different Actiavtion Functions
--------------------------------------------------------------------------------------------------------"""
import random,math
import numpy as np
import matplotlib.pyplot as plt
BORDER="-"*60
#####################################################################################################
#   Function Name   :   Relu
#   Input Params    :   z
#   Output Params   :   max(0,z)
#   Description     :   ReLu Activation function
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Relu(z):
    return np.maximum(0,z)
#####################################################################################################
#   Function Name   :   Tanh
#   Input Params    :   z
#   Output Params   :   (e^z-e^(-z))/(e^z+e^(-z))
#   Description     :   Tanh Activation function
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Tanh(z):
    numerator=np.exp(z)-np.exp(-z)
    denominator=np.exp(z)+np.exp(-z)
    return numerator/denominator
#####################################################################################################
#   Function Name   :   sigmoid
#   Input Params    :   z
#   Output Params   :   1 / (1 + exp(-z))
#   Description     :   sigmoid Activation function
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def Sigmoid(z):
    return 1 / (1 + np.exp(-z))
#####################################################################################################
#   Function Name   :   plot_all_functions
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   All Activation function plot
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def plot_all_functions():
    z_values=np.linspace(-10,10,200)
    sigmoidValues=Sigmoid(z_values)
    relu_values = Relu(z_values)
    tanh_values=Tanh(z_values)
    
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,8.5)) 
    #plot_axes_wise(axes,z_values,funValues,graphTitle,): 

    plot_axes_wise(axes[0][0],z_values,sigmoidValues,"Sigmoid")
    plot_axes_wise(axes[0][1],z_values,relu_values,"Relu")
    plot_axes_wise(axes[1][0],z_values,tanh_values,"Tanh")
    axes[1][1].text(0.05,0.9,f"Sigmoid:Used in output layer,Binary Classification problems")
    axes[1][1].text(0.05,0.7,f"Relu:Used in Hidden layer of Neural Network(CNN)")
    axes[1][1].text(0.05,0.5,f"Tanh:Used in Hidden layer of Neural Network(RNN)")

    """ 
    axes[0][0].plot(z_values, sigmoidValues, label="Sigmoid Activation Function",linewidth=2,color="blue")
    axes[0][0].axhline(y=0, color="black", linewidth=0.5)
    axes[0][0].axhline(y=1, color="black", linewidth=0.5)
    axes[0][0].axvline(x=0, color="gray", linestyle="--")
    axes[0][0].set_title("Sigmoid Activation Function",fontsize=14)
    axes[0][0].set_xlabel("Input (z)", fontsize=10)
    axes[0][0].set_ylabel("Output", fontsize=10)
    axes[0][0].grid()
    
    
   axes[0][1].plot(z_values, relu_values, label="Relu Activation Function",linewidth=2,color="blue")
    axes[0][1].axhline(y=0, color="black", linewidth=0.5)
    axes[0][1].axhline(y=1, color="black", linewidth=0.5)
    axes[0][1].axvline(x=0, color="gray", linestyle="--")
    axes[0][1].set_title("Relu Activation Function",fontsize=14)
    axes[0][1].set_xlabel("Input (z)", fontsize=10)
    axes[0][1].set_ylabel("Output", fontsize=10)
    axes[0][1].grid()
    
    axes[1][0].plot(z_values, tanh_values, label="Tanh Activation Function",linewidth=2,color="blue")
    axes[1][0].axhline(y=0, color="black", linewidth=0.5)
    axes[1][0].axhline(y=1, color="black", linewidth=0.5)
    axes[1][0].axvline(x=0, color="gray", linestyle="--")
    axes[1][0].set_title("Tanh Activation Function",fontsize=14)
    axes[1][0].set_xlabel("Input (z)", fontsize=10)
    axes[1][0].set_ylabel("Output", fontsize=10)
    axes[1][0].grid()"""
    
    plt.show()
#####################################################################################################
#   Function Name   :   plot_all_functions
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   ReLu Activation function plot
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def plot_axes_wise(axes,z_values,funValues,graphTitle,): 
   
    axes.plot(z_values, funValues, label=f"{graphTitle} Activation Function",linewidth=2,color="blue")
    axes.axhline(y=0, color="black", linewidth=0.5)
    axes.axhline(y=1, color="black", linewidth=0.5)
    axes.axvline(x=0, color="gray", linestyle="--")
    axes.set_title(f"{graphTitle} Activation Function",fontsize=12)
    axes.set_xlabel("Input (z)", fontsize=9)
    axes.set_ylabel("Output", fontsize=9)
    axes.grid()
    
    
                
    

#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    plot_all_functions()
       
    
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    

