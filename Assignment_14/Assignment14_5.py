"""-----------------------------------------------------------------------------------------------------
                          Assignment14_5
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class BankAccount
                    2. Instance Variables: account_number,name and balance
                    3. __init__ method to initialise variables
                    4. Create methods to deposit,withdraw and displaying balance
---------------------------------------------------------------------------------------------------------"""    
class BankAccount:
    #initialise variables
    def __init__(self):
        self.account_number=0
        self.name=0
        self.balance=0.0
        self.operationDetails="\n---------------------------------------------------------"
        
  

    #Accept user details
    def acceptBankAccDetails():
        try:
            print("\nEnter the customer Bank Details....\n")
            accNumber=int(input("\nAccount number:"))
            customerName=input("\nCustomer Name:")
            accBalance=float(input(f"Account Balance':Rs.")) 
        except Exception as excObj:
                print("\n\nExceptiom occured :",excObj)  
        return accNumber,customerName,accBalance  
    
    #Set accountDetails()  
    def setAccountDetails(self,accNumber,customerName,accBalance):
        self.account_number=accNumber
        self.name=customerName
        self.balance=accBalance
        self.operationDetails+="\nTransaction Details of Account Number :  "+str(self.account_number)
        self.operationDetails+="\n---------------------------------------------------------"
        
        self.operationDetails+="\nInitial Account balance :Rs."+str(self.balance)

   #This method deposits user accepted amount to "balance"
    def Deposit(self,depositAmount):
        try:
            #Amount to be deposited
            self.balance=self.balance+depositAmount
            print(f"\nDeposit Successful : Rs. {depositAmount} for Account Number '{self.account_number}'\
                  \n\t\t\tUpdated balance:Rs.{self.balance}")
            self.operationDetails+="\nDeposited:Rs."+str(depositAmount)

        except Exception as excObj:
            print(f"Exception occured while depositing the {depositAmount} for '{self.account_number}':",excObj)

    #This method  acceppts amount from user and withdraws that from "balance""
    def Withdraw(self,withdrawAmount):
        if (withdrawAmount >= self.balance):
            print(f"Insufficient Balance in Account {self.account_number}.\
                  \nCan not proceed with withdraw.Current balance is Rs. {self.balance}")
        else:    
            self.balance=self.balance-withdrawAmount
            print(f"\nWithdraw successful: Rs.{withdrawAmount} for Account Number '{self.account_number}'\
                  \n\t\t\tUpdated balance:Rs.{self.balance}")
            self.operationDetails+="\nWithdraw:Rs."+str(withdrawAmount)

    #This method displays Account details
    def displayAccount(self):
        print("---------------------------------------------------------")
        print(f"Displaying Bank Details for '{self.name}' \n")
        print("---------------------------------------------------------")
        print(f"\nAccount Holder Name:{self.name}")
        print(f"\nAccount Number:{self.account_number}")
        print(f"\nAccount Balance:{self.balance}")
        
    
    #This method return Customer Bank Account details
    def __str__(self):
        accDetails=""
        accDetails+="\nAccount Holder Name:"+str(self.name)
        accDetails+="\nAccount Number:"+str(self.account_number)
        accDetails+="\nAccount Balance:"+str(self.balance) 
        print("---------------------------------------------------------")

        return accDetails    

    #-----------------------------------------------------------------------------------------
    #This function Performs deposit,withdraw operations on BankAccount object
    #---------------------------------------------------------------------------------------
    def processBankAccount(self):
        try:
            print(f"Which transaction would you like to perform for'{self.name}'\
                     with Account number '{self.account_number}'")
            choice=0
            while(not(choice==5 or choice>5)):
                print("\n\n1.Deposit\n2.Withdraw\n3.Display Account details\n4.All transaction details\n5.Exit")
                choice=int(input(f"\n\nEnter the choice of transaction for '{self.name}':"))
                #Deposit process
                if(choice==1):
                    depositAmount=float(input("\nEnter the Amount to be deposited:"))
                    self.Deposit(depositAmount)

                #Withdraw process    
                elif choice==2:
                    withdrawAmount=float(input("\nEnter the Amount to withdraw:"))
                    self.Withdraw(withdrawAmount)

                #Display current account status
                elif choice==3:
                        self.displayAccount()
                #Diplay all transactions for current account        
                elif choice==4:
                     print(self.operationDetails)
                     print("\n------------------------------------------------")
                     print(f"\nFinal Balance is :Rs.{self.balance}")
                     print("\n------------------------------------------------")

        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nExceptiom occured :",excObj)             
#--------------------------------------------------------------------------------------------------------    
# This is main method creates Student object and sets student details
#------------------------------------------------------------------------------------------------------         
def main():
    bankAccObj=""
    try:
        accNumber,customerName,accBalance=BankAccount.acceptBankAccDetails()
        bankAccObj=BankAccount()
        bankAccObj.setAccountDetails(accNumber,customerName,accBalance)
        bankAccObj.displayAccount()
        bankAccObj.processBankAccount()


    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       

#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
                     