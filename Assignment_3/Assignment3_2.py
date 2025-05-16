"""-------------------------------------------------------------------------------------------
                          Assignment3_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts N elements from the user and 
                    store it into a list and returns the maximum number 
                    from the list
------------------------------------------------------------------------------------------"""
from MarvellousFun import acceptElements
#-------------------------------------------------------------------------------------
# This Function finds the maximum number from the list
#-------------------------------------------------------------------------------------
def findMaximumElement(numberList):
    max = 0
    for num in numberList:
         if num > max :
             max = num
    print("-------------------------------------------------------------------")
    print(f"Maximum element from the list {numberList} is : {max}")     
    print("-------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
# This function accepts a number of elements number from user and calls function 
# acceptElements(number),findMaximumElement(inputNumberList)
#------------------------------------------------------------------------------------------

def main():
    noOfElements=int(input("Enter number of elements in the list:"))
    inputNumberList=acceptElements(noOfElements)
    findMaximumElement(inputNumberList)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
