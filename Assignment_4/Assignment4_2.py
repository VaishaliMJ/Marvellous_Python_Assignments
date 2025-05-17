"""-------------------------------------------------------------------------------------------
                          Assignment4_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement: This program contains a lambda function and returns multiplication
------------------------------------------------------------------------------------------"""

Multi = lambda num1,num2 : num1 * num2
#------------------------------------------------------------------------------------------
# This function accepts a input number from user and calls lambda multiplication function
#------------------------------------------------------------------------------------------
def main():

    number1=int(input("Enter first number :"))
    number2=int(input("Enter second number :"))

    answer = Multi(number1,number2)
    print("--------------------------------------------------------------")
    print(f"Multiplication of {number1} * {number2} : {answer}")
    print("--------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
