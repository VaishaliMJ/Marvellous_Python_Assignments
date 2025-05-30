"""-----------------------------------------------------------------------------
                          Assignment11_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
------------------------------------------------------------------------------------------
Problem statement : Write a program counts number of "0" in the input number
-----------------------------------------------------------------------------------------"""
COUNT_NO_ZEROS=0
#-----------------------------------------------------------------------------------------
#This function counts number of "0" from function
#-----------------------------------------------------------------------------------------
def countNumberOfZeros(num):
    zeroCount=0
    while(num!=0):
        digit=num%10
          
        if (digit==0):
            zeroCount+=1

        num=int(num/10)     
    return zeroCount     
#-----------------------------------------------------------------------------------------
#Finds number of "0" in the number (recursive)
#-----------------------------------------------------------------------------------------
def recursiveCountNoOfZeros(num):
    global COUNT_NO_ZEROS
    if(num!=0):
        digit=num%10
        
        if(digit==0):
             COUNT_NO_ZEROS+=1

        num=int(num/10)    
        recursiveCountNoOfZeros(num)

#-----------------------------------------------------------------------------------------
# main() function calls countNumberOfZeros(number)----Non recursive
#                        recursiveCountNoOfZeros----->Recursive
#-----------------------------------------------------------------------------------------
def main():
    global COUNT_NO_ZEROS
    try:
        print("\nCounts number of '0' in the input number")
        print("---------------------------------------------------------")
        number=int(input("Enter the number with '0''s in it:"))
        if number == 0:
            zeroCount =1
            COUNT_NO_ZEROS = 1
        else:    
            zeroCount=countNumberOfZeros(number)
            recursiveCountNoOfZeros(number)
            

        print(f"Number of '0''s in '{number}' using normal function:{zeroCount}")
        print(f"Number of '0''s in '{number}' using Recursive function:{COUNT_NO_ZEROS}")
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