"""-----------------------------------------------------------------------------------------------------
                          Assignment12_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                  1. Create class named Arithmetic 
                  2. Arithmetic class has Value1,Value2 as instance variable
                  3. init method initialises instance variables to "0"
                  4. Instance methods are : Accept(),Addition(),Subtraction(),Multiplication(),Division()
                  5. Accept()---> Accept Value1 and Value2 from user
                  6. Addition()--->Add Value1 and Value2
                  7. Subtraction--->Subtract Value1 and Value2
                  8. Multiplication()-->Multiply Value1 and Value2
                  9. Division()--->Value1/Value2
                  10. Create multiple objects of the class
--------------------------------------------------------------------------------------------------------"""

class Arithmetic:
    #This method initialise instance variables to "0"
    def __init__(self):
        self.Value1=0
        self.Value2=0
        self.result=""
        
    #----------------------------------------------------------------------------------------
    # This function accepts inputs from user
    #----------------------------------------------------------------------------------------
    def Accept(self):    
        try:
            self.Value1=int(input("Enter the first number:"))
            self.Value2=int(input("Enter the Second number:"))
            self.result+="Result of Arithmetic Operations on "+str(self.Value1)+ " and "+ str(self.Value2)+" as follows :"

        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
             print("\n\nExceptiom occured :",excObj)  
        
    #----------------------------------------------------------------------------------------
    # This function Adds two numbers
    #---------------------------------------------------------------------------------------
    def Addition(self):
        result=self.Value1+self.Value2
        self.result+="\nAddition : "+str(self.Value1)+" + "+str(self.Value2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function Subtract two numbers
    #---------------------------------------------------------------------------------------
    def Subtraction(self):
        result=self.Value1-self.Value2
        self.result+="\nSubtraction : "+str(self.Value1)+" - "+str(self.Value2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function multiply two numbers
    #---------------------------------------------------------------------------------------
    def Multiplication(self):
        result=self.Value1*self.Value2
        self.result+="\nMultiplication : "+str(self.Value1)+" * "+str(self.Value2)+" = "+str(result)
        return result
    #----------------------------------------------------------------------------------------
    # This function divide two numbers
    #---------------------------------------------------------------------------------------
    def Division(self):
        result=0
        try:
            
            result=self.Value1/self.Value2

        except ZeroDivisionError as zobj:
            print("Exception occured due to second input ...",zobj)
            result=zobj
        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
             print("\n\nExceptiom occured :",excObj) 
        self.result+="\nDivision : "+str(self.Value1)+" / "+str(self.Value2)+" = "+str(result)
      
        return result  
    #----------------------------------------------------------------------------------------       
    #This method displays String representation of object
    #----------------------------------------------------------------------------------------
    def __str__(self):
          return self.result

    #----------------------------------------------------------------------------------------       
    #This method performs selected Arithmetic operations on input numbers
    #-----------------------------------------------------------------------------------------
    def processArithmeticObject(self):
        print(f"\nPerforming following operations on {self.Value1} and {self.Value2}")
        choice=0
        while(not(choice==5 or choice>5)):    
            print("\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
            choice=int(input(f"Enter the choice of operation to perform on {self.Value1} and {self.Value2}:"))
            if(choice==1):
                 result=self.Addition()
                 print(f"\n\nAddition: {self.Value1} + {self.Value2} = {result}")
            elif choice==2:
                 result=self.Subtraction()
                 print(f"\n\nSubtraction: {self.Value1} - {self.Value2} = {result}")

            elif choice==3:
                 result=self.Multiplication()
                 print(f"\n\nMultiplication: {self.Value1} * {self.Value2} ={ result}")

            elif choice==4:
                 result=self.Division()
                 print(f"\n\nDivision: {self.Value1} / {self.Value2} = {result}")         

    #-----------------------------------------------------------------------------------------
    #This function creates the Arithmatic objects
    #--------------------------------------------------------------------------------
    @staticmethod
    def CreateArithmeticObjects():
        objCount = 0     
        createMoreObject="Yes"
        arithmeticObjList=[]      #creating list of Arithmetic objects
        arithmeticObj=""
        print("---------------------------------------------------------")
        print("Creating 'Arithmetic' objects")

        while (createMoreObject.lower()=="yes" or createMoreObject.lower()=="y"):
            objCount=objCount+1
            print("---------------------------------------------------------")
            print(f"Accepting input for Arithmetic Operation : {objCount}  ")
            print("---------------------------------------------------------")
            arithmeticObj=Arithmetic()
            arithmeticObj.Accept()
            arithmeticObj.processArithmeticObject()
            
            arithmeticObjList.append(arithmeticObj)
            createMoreObject= input("\n\n\nProceed with more Arithmatic operations on DIFFERENT NUMBERS(Yes/No)??:")
        return arithmeticObjList
    #-----------------------------------------------------------------------------------------
    #This function displays all created Arithmatic objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def PrintAllArithmeticObjects(arithmeticObjList):
        print("\n\n--------------------------------------------------------------")
        print(f"\tPrinting Details for All created Arithmatic Operations ")
        print("-------------------------------------------------------------------")   
        objCount=1
        for operation in arithmeticObjList:   
            print("Arithmetic Object ",objCount)
            objCount+=1
            print(operation)
            print("--------------------------------------------------------------")  
#----------------------------------------------------------------------------------------------------------
# This function calls "CreateArithmeticObjects" and "PrintAllArithmeticObjects methods
# --------------------------------------------------------------------------------------------------------
def main():
    try:
        #This function creates the Arithmetic objects
        arithmeticObjList = Arithmetic.CreateArithmeticObjects()

        #This function displays all created Arithmetic objects
        Arithmetic.PrintAllArithmeticObjects(arithmeticObjList)   
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 
                
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------           