"""----------------------------------------------------------------------------------------
                          Assignment7_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program checks if given string is palindrome or not
------------------------------------------------------------------------------------------"""
def checkPalindrome(inputString):
    reverseString=""
    for char in inputString:
        reverseString=char+reverseString
    print(f"\nReversed string of '{inputString}' is : '{reverseString}'")    
    if (inputString==reverseString):
        return "a Palindrome"
    else:
        return "Not a Palindrome"

#------------------------------------------------------------------------------------------
# Calls checkPalindrome(inputString) and checks if its palindrome or not
#-------------------------------------------------------------------------------
def main():
    print("------------------------------------------------------")
    inputString = input("Enter the string checked for palindrome:")
    isPalindrome=checkPalindrome(inputString)
    print(f"\n'{inputString}' is {isPalindrome}")
          #lambda isPalindrome : "Palindrome" if isPalindrome else "Not Palindrome")
    print("------------------------------------------------------")

#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#------------------------------------------------------------------------------