"""-------------------------------------------------------------------------------------------
                          Assignment11_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepets a number from user and displays
                     number of * in following matrix format
                     e.g. Input :accepted number 5
                     Output * 
                            * * 
                            * * * 
                            * * * *   
                            * * * * *
-------------------------------------------------------------------------------------------"""

STAR ="*"
ROW=0
#-----------------------------------------------------------------------------------------
#   This function prints the * in given format
#-----------------------------------------------------------------------------------------
def printStarstInFormat1(num):
    for row in range(num):
        for column in range(num):
            if (row>=column):
                print(STAR,end=" ")
        print()
#-----------------------------------------------------------------------------------------
#   This function prints the * in given format
#-----------------------------------------------------------------------------------------
def printStarstInFormat(num):
    row=0
    while (row<=num):
        coulmn=0
        while(coulmn<row):
            print(STAR,end=" ")   
            coulmn=coulmn+1  
        print()     
        row=row+1            
#-----------------------------------------------------------------------------------------
#   This recursive function prints the * in given format
#-----------------------------------------------------------------------------------------
def recursivePrintStarstInFormat(num,column) :
    global ROW
    if (ROW<=num):
            
        if(column<ROW):
            print(STAR,end=" ")    
            column=column+1 
            recursivePrintStarstInFormat(num,column) 
        else:
            print()     
        ROW=ROW+1  
        recursivePrintStarstInFormat(num,column=0 ) 

#-----------------------------------------------------------------------------------------
# main() function calls printStarstInFormat(number)----Non recursive
#                       recursivePrintStarstInFormat(number)----->Recursive
#------------------------------------------------------------------------------------
def main():
    try:
        print("Print * in triangle pattern")
        print("---------------------------------------------------------")
        number=int(input("Enter the number:"))
        printStarstInFormat(number)
        print("---------------------------------------------------------")
        print("\nPrinting pattern using recursive function")
        print("---------------------------------------------------------")

        recursivePrintStarstInFormat(number,column=0 )
        print("---------------------------------------------------------")
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 
    

#-----------------------------------------------------------------------------------------
#  Entry point of prog
#-----------------------------------------------------------------------------------------
if __name__=="__main__":
    main()