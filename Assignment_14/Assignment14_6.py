"""-----------------------------------------------------------------------------------------------------
                          Assignment14_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Calculator
                    2. Accept inputs from user
                    3. Create methods add,subtract,multiply and divide
---------------------------------------------------------------------------------------------------------"""
class Calculator:
    #__init__ / constructor 
    def __init__(self):
        self.number1=0
        self.number2=0
        self.result=""

    #This method accepts numbers from user
    @staticmethod
    def acceptNumbers():
        try:
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the Second number:"))

        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
             print("\n\nExceptiom occured :",excObj)
        return num1,num2  

    #This method sets the instance variables
    def setVariables(self,num1,num2):
        self.number1=num1
        self.number2=num2
        self.result+="Result of Arithmetic Operations on "+str(self.number1)+ " and "+ str(self.number2)+" as follows :"
        self.result+="\n--------------------------------------------------------------------"

    #----------------------------------------------------------------------------------------
    # This function Adds two numbers
    #---------------------------------------------------------------------------------------
    def add(self):
        result=self.number1+self.number2
        self.result+="\nAddition : "+str(self.number1)+" + "+str(self.number2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function Subtract two numbers
    #---------------------------------------------------------------------------------------
    def subtract(self):
        result=self.number1-self.number2
        self.result+="\nSubtraction : "+str(self.number1)+" - "+str(self.number2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function multiply two numbers
    #---------------------------------------------------------------------------------------
    def multiply(self):
        result=self.number1*self.number2
        self.result+="\nMultiplication : "+str(self.number1)+" * "+str(self.number2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function divide two numbers
    #---------------------------------------------------------------------------------------
    def divide(self):
        result=0
        try:
            
            result=self.number1/self.number2

        except ZeroDivisionError as zobj:
            print("Exception occured due to second input ...",zobj)
            result=zobj
        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
             print("\n\nExceptiom occured :",excObj) 
        self.result+="\nDivision : "+str(self.number1)+" / "+str(self.number2)+" = "+str(result)
      
        return result  
    #----------------------------------------------------------------------------------------       
    #This method displays String representation of object
    #----------------------------------------------------------------------------------------
    def __str__(self):
        self.result+="\n-----------------------------------------------------------------"
        return self.result
    
    #----------------------------------------------------------------------------------------       
    #This method performs selected operations on input numbers
    #-----------------------------------------------------------------------------------------
    def calculatorMenu(self):
        print(f"\nPerforming following operations on {self.number1} and {self.number2}")

        choice=0
        while(choice!=5):
            print("\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
            choice=int(input(f"Enter the choice of operation to perform on {self.number1} and {self.number2}:"))
            if(choice==1):
                 result=self.add()
                 print(f"\n\nAddition: {self.number1} + {self.number2} = {result}")
            elif choice==2:
                 result=self.subtract()
                 print(f"\n\nSubtraction: {self.number1} - {self.number2} = {result}")

            elif choice==3:
                 result=self.multiply()
                 print(f"\n\nMultiplication: {self.number1} * {self.number2} ={ result}")

            elif choice==4:
                 result=self.divide()
                 print(f"\n\nDivision: {self.number1} / {self.number2} = {result}")         

#----------------------------------------------------------------------------------------------------------
# This function calls "createCalculator" method
# --------------------------------------------------------------------------------------------------------
def main():
    calculatorObj=""
    try:
        #This function creates the Calculator object

        calculatorObj = Calculator()
        num1,num2=Calculator.acceptNumbers()
        #set variables
        calculatorObj.setVariables(num1,num2)
        #Process numbers
        
        calculatorObj.calculatorMenu()
        #Display result
        print(calculatorObj)
        

    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 
                
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#------------------------------

