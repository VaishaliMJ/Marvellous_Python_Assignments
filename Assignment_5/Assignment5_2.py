"""-------------------------------------------------------------------------------------------
                          Assignment 5_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts a character from user and checks 
                    if it's a vowel or consonant
-----------------------------------------------------------------------------------------"""
Vowel_List=("a","e","i","o","u","A","E","I","O","U")
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
def checkIfVowel(inputLetter):
    isVowel = False
    for letter in Vowel_List:
        if inputLetter==letter:  
            isVowel = True
            break
    return isVowel             
#-----------------------------------------------------------------------------------
# This is main function calls checkIfVowel() function
#-----------------------------------------------------------------------------------
def main():
    letter=input("Enter a letter to be checked:")
    isVowel=checkIfVowel(letter)
    ans = lambda isVowel : "a Vowel" if isVowel else "a Consonant"
    print(f"\'{letter}\' is ",ans(isVowel))
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
