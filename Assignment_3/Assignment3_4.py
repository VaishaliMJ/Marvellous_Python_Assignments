"""-------------------------------------------------------------------------------------------
                          Assignment3_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets N elements from the user and 
                    store it into a list
                    2. It also accepts another number to 
                    be searched in the list and find its frequency in the list
------------------------------------------------------------------------------------------"""
from MarvellousFun import acceptElements
#-------------------------------------------------------------------------------------
# This Function finds the frequency of number in the list
#-------------------------------------------------------------------------------------
def findNumberFrequency(numberList,searchNumber):
    count = 0
    for num in numberList:
         if searchNumber == num :
             count+=1
    print("-----------------------------------------------------------------------")
    print(f"Frquency of number {searchNumber} in the list {numberList} is : {count}")     
    print("-----------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
# This function accepts a number of elements number from user and calls function 
# acceptElements(number), findNumberFrequency(inputNumberList,searchNumber)
#------------------------------------------------------------------------------------------
def main():
    noOfElements=int(input("Enter number of elements in the list:"))
    inputNumberList=acceptElements(noOfElements)
    searchNumber=int(input("Enter the number to be searched for frequency:"))
    findNumberFrequency(inputNumberList,searchNumber)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
