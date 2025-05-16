"""-------------------------------------------------------------------------------------------
                          Assignment3_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the addition of 
                    elements of the list
------------------------------------------------------------------------------------------"""
from MarvellousFun import acceptElements
#-------------------------------------------------------------------------------------
# This Function adds all the elements from input list
#-------------------------------------------------------------------------------------
def additionOfAllElements(inputNumberList):
    sum=0
    for num in inputNumberList:
         sum= sum + num
    print("-------------------------------------------------------------------")
    print(f"Addition of all list elements {inputNumberList} is : {sum}")     
    print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------------------
# This function accepts a number of elements number from user and calls function 
# acceptElements(number) to accept elements in the list 
#------------------------------------------------------------------------------------------

def main():
    noOfElements=int(input("Enter number of elements in the list:"))
    inputNumberList = acceptElements(noOfElements)
    additionOfAllElements(inputNumberList)
   
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
