"""-------------------------------------------------------------------------------------------
                          Assignment3_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets N elements from the user and 
                    store it into a list
                    2. It finds prime number from the list
                    3. Returns addition of all prime numbers
------------------------------------------------------------------------------------------"""
from MarvellousFun import ChkPrime,acceptElements
#-------------------------------------------------------------------------------------
# This Function finds the prime number in the list
#-------------------------------------------------------------------------------------
def listPrime(numberList):
    sumPrime = 0
    listPrime=[]
    for num in numberList: 
         if (num>1) and ChkPrime(num) :
             listPrime.append(num)
             sumPrime+=num
    print("-------------------------------------------------------------------")
    print("Original list :",numberList)
    print("Prime Number list:",listPrime)
    print(f"Addition of Prime numbers in the list is : {sumPrime}")     
    print("-------------------------------------------------------------------")

#------------------------------------------------------------------------------------------
# This function accepts a number of elements number from user and calls function 
# acceptElements(number), listPrime(inputNumberList)
#------------------------------------------------------------------------------------------
def main():
    noOfElements=int(input("Enter number of elements in the list:"))
    inputNumberList=acceptElements(noOfElements)
    listPrime(inputNumberList)
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
