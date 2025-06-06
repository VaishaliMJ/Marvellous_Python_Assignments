"""-----------------------------------------------------------------------------------------------------
                          Assignment14_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Rectangle
                    2. This class has instance variables length and width
                    3. Methods to calculate area and perimeter
---------------------------------------------------------------------------------------------------------"""
class Rectangle:
    #Constructor/ Init method to initialise all variables
    def __init__(self):
        self.length=0.0    #length
        self.width=0.0     #width 
        self.areaRectangle=0.0
        self.perimeterRect=0.0

    #This method accepts length and width from user
    @staticmethod
    def AcceptLenWidth():
        try:
            rectLength=float(input("Enter length:"))
            rectWidth=float(input("Enter Width:"))
        except ValueError as errObj:
            print("\n\nError while accepting length or width:",errObj)  

        except Exception as excObj:
                print("\n\nExceptiom occured in AcceptLenWidth():",excObj)  
        return rectLength,rectWidth    
    
    #This method sets Length and width of rectangle
    def setLengthWidth(self,rectLen,rectWidth):
        self.length=rectLen
        self.width=rectWidth

    #This method calculates Area of rectangle
    def calculateArea(self):
        self.areaRectangle=self.length * self.width
        
    
    #This method calculates Perimeter of rectangle
    def calculatePerimeter(self):
        self.perimeterRect=2*(self.length+self.width)
        
    
    #This method displays Area and Perimeter of created object
    def DisplayRect(self,rectObj):
        print("\nDisplaying Rectangle Details:")
        print(rectObj)

    #-----------------------------------------------
    #This method return Rectangle object created
    #--------------------------------------------
    def __str__(self):
        rectObj=""
        rectObj+="\nRectangle with length "+str(self.length)+" and  width "+str(self.width)+" has :"
        rectObj+="\nArea:"+str(self.areaRectangle)
        rectObj+="\nPerimeter:"+str(self.perimeterRect)
        rectObj+="\n-------------------------------------------------------------------------"
        return rectObj         
    
    #This function creates Rectangle object
    @staticmethod
    def createRectangle():
        rectObjCount=0
        rectObj=""
        createMoreRect="yes"
        rectangleobjList=[]    #Rectangle object list

        while(createMoreRect.lower()=="yes" or createMoreRect.lower()=="y"):
            rectObjCount=rectObjCount+1
            print("---------------------------------------------------------")
            print(f"Accepting Rectangle  length and width for Object : {rectObjCount}  ")
            print("---------------------------------------------------------")
            len,width=Rectangle.AcceptLenWidth()
            #create Rectangle object
            rectObj=Rectangle()
            #setting Length and Width
            rectObj.setLengthWidth(len,width)
            #Calculate Area 
            rectObj.calculateArea()
            #Calculate perimeter
            rectObj.calculatePerimeter()
            #Display Details
            rectObj.DisplayRect(rectObj)
            #Add to Object list
            rectangleobjList.append(rectObj)
            createMoreRect= input("\n\nContinue with creating more RECTANGLE Objects(Yes/No)??:")
        return rectangleobjList    
    
    #-----------------------------------------------------------------------------------------
    #This function displays all created Rectangle Details
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def displayAllRectangles(rectangleobjList):
        print("\n\n--------------------------------------------------------------")
        print(f"\nDisplaying Details of all newly created Rectangles ")
        print("-------------------------------------------------------------------")   
        rectCount=1
        for rectDetails in rectangleobjList:   
            print("Rectangle : ",rectCount)
            rectCount+=1
            print(rectDetails)



#--------------------------------------------------------------------------------------------------------    
# This is main method calls createRectangle() and displayAllRectangles() method
#--------------------------------------------------------------------------------------------------------
def main():
    try:
        #This function creates the Reactangle objects
        rectangleObjList = Rectangle.createRectangle()

        #This function displays all created Rectangle objects
        Rectangle.displayAllRectangles(rectangleObjList) 

    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       


#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()