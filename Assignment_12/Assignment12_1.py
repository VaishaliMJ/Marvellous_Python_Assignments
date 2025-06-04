"""-----------------------------------------------------------------------------
                          Assignment12_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                  1. Create a class named Demo
                  2. Demo class contains two instance variables no1 and no2
                  3. Demo class also has one class variable "Value"
                  4. Class contains two instance methods "Fun" and "Gun" and displays 
                     values of instance variables
                  5. Initialise instance variables in "init" method
                  6. Accept values of instance variables from user
-----------------------------------------------------------------------------------------"""

class Demo:
    Value="value"
    #This method initialise instance variables to user accepted values
    def __init__(self,num1,num2):
        self.no1=num1
        self.no2=num2

    #Instance method displays "instance variables" values
    def Fun(self):
        print("\n\nInside Fun() function")
        print("Values of instance variables are ...")  
        print(f"No1:{self.no1}")  
        print(f"No2:{self.no2}")  

    #Instance method displays "instance variables" values
    def Gun(self):
        print("\n\nInside Gun() function")
        print("Values of instance variables are ...")  
        print(f"No1:{self.no1}")  
        print(f"No2:{self.no2}")  
#----------------------------------------------------------------------------------------
# This function accepts inputs from user
#----------------------------------------------------------------------------------------
def acceptNumbers():
    try:
        number1=int(input("Enter the first number:"))
        number2=int(input("Enter the Second number:"))
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj)  
    return number1,number2   
#----------------------------------------------------------------------------------------------------------
# This function accepts 2 inputs from user and creates two objects of "Demo" class with these parameters
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        
        print("      Creating DEMO class objects   ")
        print("---------------------------------------------------------")
        print("      Accepting input for first object   ")
        print("---------------------------------------------------------")
        number1,number2=acceptNumbers()
        #Create class object
        obj1=Demo(number1,number2)

        print("---------------------------------------------------------")
        print("      Accepting input for Second object")
        print("---------------------------------------------------------")
        number1,number2=acceptNumbers()
        #Create class object
        obj2=Demo(number1,number2)

        print("---------------------------------------------------------")
        print("     Calling Fun() method     ")
        print("---------------------------------------------------------")
        obj1.Fun()
        obj2.Fun()

        print("---------------------------------------------------------")
        print("      Calling Gun() method      ")
        print("---------------------------------------------------------")
        obj1.Gun()
        obj2.Gun()

        
        print("---------------------------------------------------------")
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