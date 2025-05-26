"""----------------------------------------------------------------------------------------
                          Assignment8_4
                    (Student name - Vaishali Jorwekar)
                   Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionality
                    1.Accept a string from user
                    2.Create three threads 'small','capital' and 'digits'
                    3.'small' thread display number of small characters in input String
                    4.'capital' thread display number of capital characters in input String
                    5.'digits' thread display number of digits in input string
                    6.Display Id and name of each thread

-------------------------------------------------------------------------------------------------"""
import threading,os
#-----------------------------------------------------------------------------------------------
COUNT_SMALL_LETTERS=0
COUNT_CAPITAL_LETTERS=0
COUNT_DIGITS=0
#-------------------------------------------------------------------------------
# This function finds and counts 'small',capital letters and digits from input string
#-------------------------------------------------------------------------------
def countCaseLettersAndNumbers(inputString):
    global COUNT_SMALL_LETTERS,COUNT_CAPITAL_LETTERS,COUNT_DIGITS
    currThreadName=threading.current_thread().name
    print(f"\n\nStarting {currThreadName} thread--PID-->{os.getpid()}....(ThreadId-->{threading.get_ident()})")
    for letter in inputString:
        #ord() is inbuilt function in python to find ascii
        ascii_val=ord(letter)

        if currThreadName=="small" and (ascii_val>=97 and ascii_val<=122):   #a-z letters
            COUNT_SMALL_LETTERS=COUNT_SMALL_LETTERS+1

        elif currThreadName=="capital" and (ascii_val>=65 and ascii_val<=90):  #A-Z letters 
            COUNT_CAPITAL_LETTERS=COUNT_CAPITAL_LETTERS+1

        elif currThreadName=="digits" and (ascii_val>=48 and ascii_val<=57): #0-9 digits
            COUNT_DIGITS=COUNT_DIGITS+1    
    print(f"\nExiting {currThreadName} thread.....")
        
#-------------------------------------------------------------------------------
# main() function create and start three threads small,capital and digits
#-------------------------------------------------------------------------------
def main():
    print("----------------------------------------------------------------------------")
    inputNumberString=input("Enter the string with combination of letters and numbers:")
    print("----------------------------------------------------------------------------")
    small=threading.Thread(target=countCaseLettersAndNumbers,
                           args=(inputNumberString,),
                           name="small")
    
    capital=threading.Thread(target=countCaseLettersAndNumbers,
                             args=(inputNumberString,),
                             name="capital")
    
    digits=threading.Thread(target=countCaseLettersAndNumbers,
                            args=(inputNumberString,),
                            name="digits") 

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    #Print result details
    printResultData(inputNumberString, small, capital, digits)

    print("\n\nExiting main...")
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
#  THis function prints the all result data
#-------------------------------------------------------------------
def printResultData(inputNumberString, small, capital, digits):
    print("----------------------------------------------------------------------------")
    print("\nInput String is : ",inputNumberString)
    print("----------------------------------------------------------------------------")

    print(f"\nCount of 'small case letters' in '{inputNumberString}' is :{COUNT_SMALL_LETTERS}")
    print("\nSmall thread name :",small.name)
    print("\nSmall thread id:",small.ident)
    print("----------------------------------------------------------------------------")

    print(f"\nCount of 'Capital case letters' in '{inputNumberString}' is :{COUNT_CAPITAL_LETTERS}")
    print("\nCapital thread id:",capital.ident)
    print("\nCapital thread name :",capital.name)
    print("----------------------------------------------------------------------------")
    
    print(f"\nCount of 'Digits' in '{inputNumberString}' is :{COUNT_DIGITS}")
    print("\nDigits thread name :",digits.name)
    print("\nDigits thread id:",digits.ident)
    print("----------------------------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------
