"""-------------------------------------------------------------------------------------------
                          Assignment3_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------
This file is a module and contains common Functions
-----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------------------
# This Function accepts the number to be added in the list
#------------------------------------------------------------------------------------------
def acceptElements():
    noOfElements=int(input("Enter the number of elements in the list:"))
    inputNumberList =[]
    print(f"Enter the {noOfElements} number to be added in the list:")
    for count in range(noOfElements):
        number = int(input(f"Element({count+1}) : "))
        inputNumberList.append(number)
    print("Input list elements are:",inputNumberList)  
    return inputNumberList 
#------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# This is the user defined filter function for Assignment 4
# -------------------------------------------------------------------------------------------
def CustomFilterFunction(Task,Values):
    FilterData = []
    for num in Values:
        Ret = Task(num)
        if (Ret == True) :
            FilterData.append(num)
    return FilterData
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# This is the user defined Map function for Assignment 4
#-------------------------------------------------------------------------------------------
def CustomMapFunction(Task,Values):
    MapData = []
    for num in Values:
        retValue = Task(num)
        MapData.append(retValue)
    return MapData    
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
# This is the user defined Reduce function for Assignment 4
#-------------------------------------------------------------------------------------------
def CustomReduceFunction(Task,Values,Result):
    for num in Values:
        Result = Task(Result,num)
    return Result    
#--------------------------------------------
