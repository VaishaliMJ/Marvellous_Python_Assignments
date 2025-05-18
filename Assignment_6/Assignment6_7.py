"""-----------------------------------------------------------------------------
                          Assignment6_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Accept 5 numbers from user and print largest number
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# This function finds largest of 5 numbers
#-------------------------------------------------------------------------------
def printLargest(num1,num2,num3,num4,num5):
    max = num1
    if num2 > max:
        max= num2
    if num3>max:
        max=num3
    if num4>max:
        max=num4
    if num5>max:
        max=num5
    print("Maximum number is :",max)                               
#-------------------------------------------------------------------------------
# Calls printLargest(number)
#-------------------------------------------------------------------------------
def main():
    print("Enter the five numbers :")
    num1=int(input("Number 1:"))
    num2=int(input("Number 2:"))
    num3=int(input("Number 3:"))
    num4=int(input("Number 4:"))
    num5=int(input("Number 5:"))

    print("------------------------------------------------------")
    printLargest(num1,num2,num3,num4,num5)
    
    print("------------------------------------------------------")
    
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------