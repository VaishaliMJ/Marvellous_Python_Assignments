
"""-----------------------------------------------------------------------------------------------------
                    Assignment 60_1
                    Single Neuron Sigmoid Activation Function
                    (Student name - Vaishali Jorwekar)
--------------------------------------------------------------------------------------------------------
Problem statement: Write a program to simulate a Single Artificial Neuron
--------------------------------------------------------------------------------------------------------"""
import random,math
import numpy as np
import matplotlib.pyplot as plt
BORDER="-"*60
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
#   Function Name   :   plot_sigmoid
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   ReLu Activation function plot
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def plot_sigmoid():
    z_values=np.linspace(-10,10,200)
    sigmoidValues=1 / (1 + np.exp(-z_values))
    
    plt.figure(figsize=(8,5))
    plt.plot(z_values,sigmoidValues,label="Sigmoid Activation Function",linewidth=2,color="blue")
    
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    
    # Labels and title
    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Show graph
    plt.show()
#####################################################################################################
#   Function Name   :   generateInput
#   Input Params    :   None
#   Output Params   :   inputs,weights,bias
#   Description     :   Genrates inputs,wts and bias randomly
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def generateInput():
    x1=2
    x2=3
    w1=0.4
    w2=0.6
    b=0.5
    return x1,x2,w1,w2,b
#####################################################################################################
#   Function Name   :   main
#   Input Params    :   None
#   Output Params   :   None
#   Description     :   Main entry point of the program
#   Author          :   Vaishali M. Jorwekar             
#####################################################################################################
def main():
    x1,x2,w1,w2,b=generateInput()

    z = x1*w1+x2*w2+b
    
    y_hat=sigmoid(z)
    print(BORDER)
    print(f"Input \nx1  :   {x1} \nx2   :   {x2}")
    print(BORDER)
    print(f"Weights\nw1 :  {w1} \nw2    :   {w2}")
    print(BORDER)

    print(f"bias    :   {b}")
    print(BORDER)

    print(f"Weighted Sum (z=x1*w1+x2*w2+b)   :   {z}")
    print(f"Final Output    :{y_hat}")
    print(BORDER)
    if y_hat<0.5:
        print("Output is close to 0")
    else:
        print("Output is close to 1")   
    print(BORDER)    
    
#####################################################################################################    
if __name__ =="__main__":
    main()
#####################################################################################################    

