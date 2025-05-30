"""-----------------------------------------------------------------------------
                          Assignment11_1 
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program to print numbers from 1 to n using recursion
-----------------------------------------------------------------------------------------"""
NUM_COUNT=1
#-----------------------------------------------------------------------------------------
#Display numbers function(Non recursive)
#-----------------------------------------------------------------------------------------
def DisplayNumbersInOrder(num):
    cnt=1
    print("Normal loop to Display Numbers In Order function")
    while  (cnt <=num):
        print(cnt,end=" ")
        cnt=cnt+1
    print()    
#-----------------------------------------------------------------------------------------
#Display numbers function(recursive)
#-----------------------------------------------------------------------------------------
def RecursiveDisplayNumbersInOrder(num):
    global NUM_COUNT
    if (NUM_COUNT<=num):
        print(NUM_COUNT,end=" ")
        NUM_COUNT = NUM_COUNT + 1
        RecursiveDisplayNumbersInOrder(num)

    else:
        print()        
#-----------------------------------------------------------------------------------------
# main() function calls DisplayNumbersInOrder(number)----Non recursive
#                       RecursiveDisplayNumbersInOrder(number)--->recursive
#-----------------------------------------------------------------------------------------
def main():
    try:
        print("\nProgram to display numbers from 1 to N")
        number=int(input("Enter the number:"))
        print("---------------------------------------------------------")
        if(number<=0):
            print(f"Can not process with input '{number}'")
        else:    
            DisplayNumbersInOrder(number)
            print("\nUsing Recursive Display Numbers In Order")
            RecursiveDisplayNumbersInOrder(number)
            print("\n")
            print("---------------------------------------------------------")
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nExceptiom occured :",excObj)   
#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------    