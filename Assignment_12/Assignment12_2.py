"""-----------------------------------------------------------------------------
                          Assignment12_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                  1. Create a class named Circle
                  2. Circle class has 3 instance variables.Radius,Area and Circumference
                  3. Class variable PI=3.14
                  4. init method initialise all instance variables to 0.0
                  5. Three instance methods Acccept(),CalculateArea(),CalculateCircumference() and Dislay()
                  6. Accept()---> Accept Radius from user
                  7. CalculateArea()-->Calculate Area of circle and store in Area
                  8. CalculateCircuference()-->Calculate circumference and store in Circumfernece
                  9. Display() ---> Displays values of all three instance variables
                  10. Create multiple objects of the class
-----------------------------------------------------------------------------------------"""

class Circle:
    #Class variable 
    PI=3.14

    #Instance Variable initialization to 0.0
    def __init__(self,):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
        


    #Accept Radius from user
    def Accept(self):    
        try:
            radiusInput=int(input("Enter the radius of circle:"))
            self.Radius=radiusInput
        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nExceptiom occured :",excObj)  


    # Calculate Area of the circle
    def CaculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
        #print("Area is :",self.Area)

    # Calculate Circumfernece of circle
    def CalculateCircumference(self):
        self.Circumference=2 * Circle.PI *self.Radius
        #print("Circumference is :",self.Circumference)

    # Displays Values of Radius,Area and Circumference of a circle  
    def Display(self):
        print("---------------------------------------------------------")
        print("    Displaying Circle details     ") 
        print("---------------------------------------------------------")
        print("Radius of the Circle:",self.Radius)
        print(f"Area of circle with Radius {self.Radius} is :{self.Area}")
        print(f"Circumference of circle with Radius {self.Radius} is :{self.Circumference}")
        print("---------------------------------------------------------")

    #This method displays String representation of object
    def __str__(self):
        circleObj=""
        circleObj+="Radius of the Circle:"+str(self.Radius)
        circleObj+="\nArea of circle with Radius ("+ str(self.Radius)+")is :"+str(self.Area)  
        circleObj+="\nCircumference of circle with Radius ("+str(self.Radius)+")is :"+str(self.Circumference)
        return circleObj
 
    #-----------------------------------------------------------------------------------------
    #This function displays all created circle objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def PrintAllCircleObjects(circleObjList):
        print("\n\n---------------------------------------------------------")
        print(f"      Printing Details for All created Circle objects ")
        print("--------------------------------------------------------------")   
        countCircle=1
        for circleObject in circleObjList:   
            print("Circle Object ",countCircle)
            countCircle+=1
            print(circleObject)
            print("--------------------------------------------------------------")     

#----------------------------------------------------------------------------------------------------------
# This function creates Circle class object and stores it in a list
#---------------------------------------------------------------------------------------------------------
def main():
    try:
        objCount = 0     
        createMoreObject="Yes"
        circleObjList=[]      #creating list of circle objects
        circleObj=""
        print("      Creating 'Circle' class objects   ")
        while (createMoreObject.lower()=="yes" or createMoreObject.lower()=="y"):
            objCount=objCount+1
            print("---------------------------------------------------------")
            print(f"      Accepting input for Circle object : {objCount}  ")
            print("---------------------------------------------------------")
            circleObj=Circle()
            
            print("Calculating Area and Circumference.......")
            circleObj.Accept()
            circleObj.CaculateArea()
            circleObj.CalculateCircumference()
            circleObj.Display()

            circleObjList.append(circleObj)
            createMoreObject= input("Create more circle objects(Yes/No)??:")

        #This function displays all circle objects
        Circle.PrintAllCircleObjects(circleObjList)   
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