"""-------------------------------------------------------------------------------------------
                          Assignment2_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a number from user and 
                    displays the addition of it's factors
------------------------------------------------------------------------------------------"""
from Arithmatic import Add
#----------------------------------------------------------------------------------------
# This function calculates addition of factors of given number and returns 
# all factors of given number and addition of factors
#---------------------------------------------------------------------------------------
def calculate_addition_factors(number):
    result = 0
    factors=[]
    for num in range(1,number):
        if (number % num == 0) :
            result = Add(result,num)
            factors.append(num)
    return factors,result
#------------------------------------------------------------------------------------------
# This function accepts a input number from user and calls factorial function
#------------------------------------------------------------------------------------------
def main():
    number=int(input("Enter number :"))
    factors,result=calculate_addition_factors(number)
    print("--------------------------------------------------------------")
    print(f"Addition of all factors {factors} of {number} is :",result)
    print("--------------------------------------------------------------")

#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
