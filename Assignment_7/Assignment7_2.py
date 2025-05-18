"""-----------------------------------------------------------------------------
                          Assignment7_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept list of intgers from user and use map() function t0
                    double each value
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# lambda function to double the number
#-------------------------------------------------------------------------------
double_number = lambda num : num * 2
#-------------------------------------------------------------------------------
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
    print("\nInput list elements are:",inputNumberList)  
    return inputNumberList 
#------------------------------------------------------------------------------------------
# Calls acceptNumbers() and calculates its double using map()
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputElementList=acceptElements()
    doubledList=list(map(double_number,inputElementList))
    print(f"\nDoubled list using map() function is :",doubledList)
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------