"""-----------------------------------------------------------------------------------------------------
                          Assignment13_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                  1. Create class BankAccount,with 2 instance variables Name and Amount.Class Variable ROI=10.5
                  2. Init method initialises all instance variable with user accepted values
                  3. Instance mathods are Display(),Deposit(),Withdraw() and CalculateIntrest()
                  4. Deposit() --> Adds user accepted amount to instance variable Amount
                  5. Withdraw()--> Accept amount to be withdrawn from user and subtract that from instance variable Amount
                  6. CalculateIntrest()-->Calculate interest based on Amount by considering ROI
                  7. Display()-->Displays value of all instance variables
                  8. Create multiple objects of BankAccount
---------------------------------------------------------------------------------------------------------"""
class BankAccount:
    #class variable
    ROI=10.5
    
    #This method initialise all instance variables with user accepted values
    def __init__(self,customerName,balanceAmount):
        #Instance variables
        self.Name=customerName
        self.Amount=balanceAmount
        self.operationDetails="\n---------------------------------------------------------"
        self.operationDetails+="\nTransaction Details of Account Holder : "+str(self.Name)
        self.operationDetails+="\n---------------------------------------------------------"
        self.operationDetails+="\nInitial Account balance :Rs."+str(self.Amount)

    #This method deposits user accepted amount to instance variable "Amount"
    def Deposit(self,depositAmount):
        try:
            #Amount to be deposited
            self.Amount=self.Amount+depositAmount
            print(f"\nDeposit Successful : Rs. {depositAmount} for Account '{self.Name}'\
                  .\n\t\t\tUpdated balance:Rs.{self.Amount}")
            self.operationDetails+="\nDeposited:Rs."+str(depositAmount)

        except Exception as excObj:
            print(f"Exception occured while depositing the {depositAmount} for {self.Name}:",excObj)


    #This method accept amount to be withdrawn from user and subtract that from instance variable Amount
    def Withdraw(self,withdrawAmount):
        if (withdrawAmount >= self.Amount):
            print(f"Insufficient Balance in Account.Can not proceed with withdraw.\
                  \n\t\t\tCurrent balance is Rs. {self.Amount}")
        else:    
            self.Amount=self.Amount-withdrawAmount
            print(f"\nWithdraw successful: Rs.{withdrawAmount} for Account '{self.Name}'.\
                  \n\t\t\tUpdated balance:Rs.{self.Amount}")
            self.operationDetails+="\nWithdraw:Rs."+str(withdrawAmount)

    #This method calculates Simple Intrest based on given Amount and Tenure
    def CalculateIntrest(self,principalAmount,loanTenure):
        try:
            #Simple Intrest= Principal Amount * ROI * Tenure /100  
            
            Simple_Intrest= (principalAmount * BankAccount.ROI * loanTenure )/100
            print(f"\nFor Principal amount Rs.{principalAmount} and Tenure of {loanTenure}(years).\
                   \n\t\t\tSimple intrest is :Rs.{Simple_Intrest}")
        except Exception as excObj:
            print(f"Exception occured while calculating the Intrest:",excObj)


    #This method displays Account details
    def Display(self):
        print("---------------------------------------------------------")
        print(f"Displaying Bank Details for '{self.Name}' \n")
        print("---------------------------------------------------------")
        print(f"\nAccount Holder Name:'{self.Name}'")
        print(f"\nCurrent Available Account balance: Rs.{self.Amount}") 
        print("---------------------------------------------------------")

    
    #This method return Customer Bank Account details
    def __str__(self):
        accDetails=""
        accDetails+="\nAccount Holder Name:"+str(self.Name)
        accDetails+="\nCurrent Available Account balance:Rs."+str(self.Amount) 
        print("---------------------------------------------------------")

        return accDetails
    #--------------------------------------------------------------------------------------
    # This function accepts Bank Account details from the user
    #--------------------------------------------------------------------------------------
    @staticmethod
    def AcceptCustomerDetails():
        try:
            print("\nEnter the customer Bank Details....\n")
            customerName=input("Customer Name:")
            initialDeposit=float(input(f"Initial Deposit Amount for '{customerName}':Rs.")) 
        except Exception as excObj:
                print("\n\nExceptiom occured :",excObj)  
        return customerName,initialDeposit

    #-----------------------------------------------------------------------------------------
    #This function Performs deposit,withdraw operations on BankAccount object
    #---------------------------------------------------------------------------------------
    
    def processBankAccount(self):
        try:
            print(f"Which transaction would you like to perform for '{self.Name}'")
            choice=0
            while(not(choice==6 or choice>6)):
                print("\n\n1.Deposit\n2.Withdraw\n3.Calculate Intrest\n4.Display Account details\
                      \n5.All transaction details\n6.Exit")
                choice=int(input(f"\n\nEnter the choice of transaction for '{self.Name}':"))
                #Deposit process
                if(choice==1):
                    depositAmount=float(input("\nEnter the Amount to be deposited:Rs."))
                    self.Deposit(depositAmount)

                #Withdraw process    
                elif choice==2:
                    withdrawAmount=float(input("\nEnter the Amount to withdraw:Rs."))
                    self.Withdraw(withdrawAmount)

                #Calculate Interest    
                elif choice==3:
                    principalAmount=float(input("\nEnter the principal amount:Rs."))
                    tenure=int(input("Loan Tenure in years:"))
                    self.CalculateIntrest(principalAmount,tenure)
                    
                #Display current account status
                elif choice==4:
                        self.Display()
                #Diplay all transactions for current account        
                elif choice==5:
                     print(self.operationDetails)
                     print("\n------------------------------------------------")
                     print(f"\nFinal Balance is :Rs.{self.Amount}")
                     print("\n------------------------------------------------")

        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nExceptiom occured :",excObj)         

    #-----------------------------------------------------------------------------------------
    #This function creates the BankAccount objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def CreateBankAccountObject():
        bankAccountObjCount = 0     
        addMoreBankAccount="Yes"
        bankAccountsList=[]      #creating list of Bank Accounts objects
        bankAccountObj=""
        print("---------------------------------------------------------")
        print("Creating a new 'Bank Account'")

        while (addMoreBankAccount.lower()=="yes" or addMoreBankAccount.lower()=="y"):
            bankAccountObjCount=bankAccountObjCount+1
            print("---------------------------------------------------------")
            print(f"Accepting Bank Details for new Account")
            print("---------------------------------------------------------")
            #Accepting Customer name and Amount from user
            customerName,initialDepositAmount=BankAccount.AcceptCustomerDetails()
            #Creating new account for customer
            bankAccountObj=BankAccount(customerName,initialDepositAmount)
            #Process on newly created Bank Account
            bankAccountObj.processBankAccount()
            #Additing newly created object to the objects list
            bankAccountsList.append(bankAccountObj)
            
            print("---------------------------------------------------------")
            addMoreBankAccount= input("\n\nADD MORE BANK ACCOUNTS(Yes/No)??:")

        return bankAccountsList    
    #-----------------------------------------------------------------------------------------
    #This function displays all created BANK ACCOUNT objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def PrintAllBankAccounts(BankAccountObjList):
        print("\n\n--------------------------------------------------------------")
        print(f"\tPrinting Details for All created Bank Accounts ")
        objCount=1
        for bankAcc in BankAccountObjList:   
            #print("Bank Account ",objCount)
            #objCount+=1
            print(bankAcc)
            print("--------------------------------------------------------------")  

#-----------------------------------------------------------------------------------------------
def main():
    try:
        BankAccountObjList=BankAccount.CreateBankAccountObject()
        BankAccount.PrintAllBankAccounts(BankAccountObjList)
    except ValueError as valObj:
        print("Error occured while calculating:",valObj) 
    except Exception as excObj:
        print("\n\nException occured :",excObj)      

#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------
