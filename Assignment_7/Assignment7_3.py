"""-----------------------------------------------------------------------------
                          Assignment7_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept list of intgers from user and use filter() function to 
                   keep only even numbers
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# lambda function for even number
#-------------------------------------------------------------------------------
even_number = lambda num : (num%2==0)
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
# Calls acceptNumbers() and calculates its double using filter()
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputElementList=acceptElements()
    evenNumberList=list(filter(even_number,inputElementList))
    print(f"\nEven numbers list using filter() function is :",evenNumberList)
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------