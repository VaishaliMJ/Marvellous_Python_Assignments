"""-----------------------------------------------------------------------------------------------------
                          Assignment13_3
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                   1. Create a class named Numbers
                   2. "Numbers" class has a instance variable as "Value"
                   3. Init method will initialise "Value" accepted from user
                   4. Instance methods are ChkPrime(),ChkPerfect(),SumFactors() and Factors()
                   5. ChkPrime() returns true if number is Prime else false
                   6. ChkPerfect() returns true if number is Perfect else false
                   7. Factors() Displays all factors of instance variable
                   8. SumFactors() returns addition of all the factors of number 
                   9. Creates multiple objects of "Number" class
---------------------------------------------------------------------------------------------------------"""
class Numbers:
    #constructor
    def __init__(self,inputNumber):
        self.Value=inputNumber
        self.result=f"\nGiven number "+str(self.Value)+" is :"

    
    # This function accepts inputs from user
    #----------------------------------------------------------------------------------------
    @staticmethod
    def AcceptNumber():
        try:
            number=int(input("Enter the number:"))
        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nException occured :",excObj)  
        return number   
    
    #This method checks if number is prime
    #----------------------------------------------------------------------------------------
    def ChkPrime(self):
        if self.Value<=1:
            return False
        for num in range(2,self.Value):
            if (self.Value%num==0):
                return False
        return True
    
    #This method finds the factors of a number
    #----------------------------------------------------------------------------------------
    def Factors(self):
        factorsList=[]
        for cnt in range(1,self.Value):
            if self.Value%cnt==0:
                factorsList.append(cnt)
        return factorsList
    #This method adds the factors of a number
    #----------------------------------------------------------------------------------------
    def SumFactors(self,factorsList):
        
        sumFactors=0
        for num in factorsList:
            sumFactors=sumFactors+num
        return sumFactors    

   #This method checks if given number is perfect
    #----------------------------------------------------------------------------------------
    def checkPerfect(self,sumFactors):
        if (self.Value==sumFactors):
            return True
        else:
            return False

    #This method return NUMBERS object created
    #----------------------------------------------------------------------------------------
    def __str__(self):
        return self.result
    

    #This Function checks number for "Prime",perfect number ,finds factors and Sum factors
    #----------------------------------------------------------------------------------------
    def CheckNumber(self):
        try:
            print(f"Checking number '{self.Value} for Prime,Perfect Number,Factors and Sum of Factors:")
            print("---------------------------------------------------------")
            #Checking for PRIME
            isPrime="\nPRIME:"
            if(self.ChkPrime()):
                isPrime+=str(self.Value)+" is Prime number"
            else:
               isPrime+=str(self.Value)+" is not Prime number"
            self.result+=isPrime   

            #Finding factors
            factors=self.Factors()
            self.result+="\nFACTORS:"+str(factors)

            #Finding Sum of all factors
            sumFactors=self.SumFactors(factors)
            self.result+="\nSUM OF FACTORS "+str(self.Value)+" is :" +str(sumFactors)

            #Checking for PERFECT 
            isPerfect="\nPERFECT:"
            if(self.checkPerfect(sumFactors)):
                isPerfect+=str(self.Value)+" is a perfect number"
            else:
                isPerfect+=str(self.Value)+" is not a perfect number"   

            self.result+=isPerfect

            print(self.result)
        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)   
        except Exception as excObj:
            print("\n\nException occured :",excObj)       
    #----------------------------------------------------------------------------------------
    #This method Creates objects for "Numbers" class
    @staticmethod
    def CreateNumbersObjects():
        numbersObj=""
        addMoreNumbersObj="Yes"
        NumbersObjList=[]
        NumbersObjCount=0
        print("---------------------------------------------------------")
        print("Creating 'Numbers' Object")

        while (addMoreNumbersObj.lower()=="yes" or addMoreNumbersObj.lower()=="y"):
            NumbersObjCount+=1
            print("---------------------------------------------------------")
            print(f"Accepting 'Number' for creating NUMBERS objects")
            print("---------------------------------------------------------")
            #Accepting a number from user
            userInput=Numbers.AcceptNumber()
            #creating "Numbers" object
            numbersObj=Numbers(userInput)
            #Process accepted Input
            Numbers.CheckNumber(numbersObj)
            #Adds number object in Numbers object list
            NumbersObjList.append(numbersObj)
            print("---------------------------------------------------------")
            addMoreNumbersObj = input("\n\nADD MORE NUMBERS(Yes/No)??:")
        return NumbersObjList       

    #-----------------------------------------------------------------------------------------
    #This function displays all created NUMBERS objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def DisplayNumbersObjects(numberObjectsList):
        print("\n\n--------------------------------------------------------------")
        print(f"\nPrinting Details for All created NUMBERS Objects ")
        print("---------------------------------------------------------")

        objCount=1
        for numObj in numberObjectsList:   
            print("Number Object ",objCount)
            objCount+=1
            print(numObj)
            print("--------------------------------------------------------------")  

#----------------------------------------------------------------------------------------------------------
# This function calls "CreateNumbersObjects" and 
# --------------------------------------------------------------------------------------------------------
def main():
    try:   
        #This function creates the Number objects
        numberObjectsList = Numbers.CreateNumbersObjects()

        #This function displays all created Numbers objects
        Numbers.DisplayNumbersObjects(numberObjectsList)   
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 
        print("---------------------------------------------------------")
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------
        