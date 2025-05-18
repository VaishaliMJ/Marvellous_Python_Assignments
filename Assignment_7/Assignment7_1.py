"""-----------------------------------------------------------------------------
                          Assignment7_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program using lambda function
                    -Lambda function to calculate square
                    -Lambda function to calculate cube of a number
----------------------------------------------------------------------------------------"""
#-------------------------------------------------------------------------------
# lambda functions to find square and cube of a number
#-------------------------------------------------------------------------------
square_number = lambda num : num * num
cube_number = lambda num : num**3
#-------------------------------------------------------------------------------
# main() function calls lambda functions for square and cube
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    number=int(input("Enter a number to calculate sqaure and cube:"))
    print(f"\nSquare of {number} using lambda function is :",square_number(number))
    print(f"\nCube of {number} using lambda function is :",cube_number(number))
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------