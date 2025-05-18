"""-------------------------------------------------------------------------------------------
                          Assignment 5_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts length and width from the user and 
                    calculates area and perimeter of a rectangle
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------
#This function calculates area and perimeter of a rectangle
#-----------------------------------------------------------------------------------
def calculateAreaAndPerimeter(length,width):   
    print("------------------------------------------------------")
    area = length * width
    perimeter = 2*(length + width)
    print("Area of rectangle :",area)
    print("Perimeter of rectangle:",perimeter)
    print("------------------------------------------------------")
#-----------------------------------------------------------------------------------
# This function accepts length and width from user and 
# calls function calculateAreaAndPerimeter(length,width) 
#-----------------------------------------------------------------------------------
def main():
    length=int(input("Enter Length of rectangle:")) 
    width=int(input("Enter width of rectangle:")) 
    calculateAreaAndPerimeter(length,width)  
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
