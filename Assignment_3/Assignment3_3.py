"""-------------------------------------------------------------------------------------------
                          Assignment3_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the minimum number
                    from the list
------------------------------------------------------------------------------------------"""
from MarvellousFun import acceptElements
#-------------------------------------------------------------------------------------
# This Function finds the minimum number from the list
#-------------------------------------------------------------------------------------
def findMinimumElement(numberList):
    min=numberList[0]
    for num in numberList:
         if num < min :
             min = num
    print("-------------------------------------------------------------------")
    print(f"Minimum element from the list {numberList} is : {min}")     
    print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------------------
# This function accepts a number of elements number from user and calls function 
# acceptElements(number), findMinimumElement(inputNumberList)
#------------------------------------------------------------------------------------------
def main():
    noOfElements=int(input("Enter number of elements in the list:"))
    inputNumberList=acceptElements(noOfElements)
    findMinimumElement(inputNumberList)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
