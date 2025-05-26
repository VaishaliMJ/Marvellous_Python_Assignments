"""-----------------------------------------------------------------------------
                          Assignment8_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
-------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionality
                   1.Creates two threads 'evenfactor' and 'oddfactor'
                   2.Accepts one integer number from user and pass as a argument to these threads
                   3.'evenfactor' thread will add even factors of the number
                   4.'oddfactor' thread will add odd factors of the number   
                   5.After completion of main thread should display message "exit from main"
----------------------------------------------------------------------------------------------"""
import threading,os
#---------------------------------------------------------------------------------
SUM_EVEN_FACTORS=0
SUM_ODD_FACTORS=0
EVEN_FACTORS=[]
ODD_FACTORS=[]
#---------------------------------------------------------------------------------
# This function calculates sum of even and odd factors of input number
#---------------------------------------------------------------------------
def evenAndOddFactorsAddition(number):
    nameCurrentThread=threading.current_thread().name
    print(f"Starting '{nameCurrentThread}' thread--PID->{os.getpid()}--(ThreadId-->{threading.get_ident()})")
    global SUM_EVEN_FACTORS,EVEN_FACTORS
    global SUM_ODD_FACTORS,ODD_FACTORS
    for num in range(1,number):
        if (number % num == 0):
            if (num%2==0) and nameCurrentThread=="evenfactor":
            # print(f"{nameCurrentThread}:",num)
                EVEN_FACTORS.append(num)
                SUM_EVEN_FACTORS=SUM_EVEN_FACTORS+num
            if (not(num%2==0)) and nameCurrentThread=="oddfactor":
                #print(f"{nameCurrentThread}:",num)
                ODD_FACTORS.append(num)
                SUM_ODD_FACTORS=SUM_ODD_FACTORS+num    
    print(f"\nExiting '{nameCurrentThread}' thread.....")

#---------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# main() function,create and start two thread evenfactor and oddfactor
#-------------------------------------------------------------------------------
def main():
    number=0
    try:
        print("------Program to find EVEN and ODD factors of number(Threading)---------------")
        number = int(input("Enter the number to find factors:"))
        if (number>1):
            evenfactor=threading.Thread(target=evenAndOddFactorsAddition,
                                        args=(number,),
                                        name="evenfactor")
            oddfactor=threading.Thread(target=evenAndOddFactorsAddition,
                                    args=(number,),
                                    name="oddfactor")
            
            evenfactor.start()
            oddfactor.start()

            evenfactor.join()
            oddfactor.join()

        
            print(f"\nEven factors of {number} are:{EVEN_FACTORS}")        
            print(f"\nAddition of all even factors of {number} is :",SUM_EVEN_FACTORS)

            print(f"\nOdd factors of {number} are:{ODD_FACTORS}")            
            print(f"\nAddition of all Odd factors of {number} is :",SUM_ODD_FACTORS)
        else:
            print(f"\n'{number}' does not have any EVEN or ODD factors")

    except ValueError as valObj:
        print("Exception ocuured while accepting input number:",valObj)
    except Exception as excObj:
        print("Exception occured...",excObj)  
    finally: 
        print("\n\nExit from main...")
        print("------------------------------------------------------")      
#-------------------------------------------------------------------------------
# Entry point of program
#-------------------------------------------------------------------------------
if __name__=="__main__":   
    main()
#-------------------------------------------------------------------------------