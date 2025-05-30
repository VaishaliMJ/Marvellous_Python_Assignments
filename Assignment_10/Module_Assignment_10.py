
"""-----------------------------------------------------------------------------
                          Module_Assignment_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------"""
# This function accepts numbers from user and creates a input number list
#--------------------------------------------------------------------------------
def acceptNumberFromUser():
    inputNumberList=[]
    try:
        numOfElements=int(input("Enter the total number of elements in the list:"))
        while (numOfElements<=0) :
            print("\n\nPlease enter number greater than 0.....")
            numOfElements=int(input("Enter again number of elements in the list:"))
          
        print(f"Accepting {numOfElements} numbers from user")
        print("------------------------------------------------------")
        for count in range(numOfElements):
            number=int(input(f"Number({count+1}):"))
            inputNumberList.append(number)
    except ValueError as errObj:
        print("Error while accepting element:",errObj)   
    except Exception as excObj:
        print("Exceptiom occured :",excObj)
    finally:
        print("Input list elements are:",inputNumberList)                
    return inputNumberList    
#--------------------------------------------------------------------------------