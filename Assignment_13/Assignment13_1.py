"""-----------------------------------------------------------------------------------------------------
                          Assignment13_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                  1. Create class named BookStore
                  2. BookStore class has two instance variables Name,Author
                  3. One class variable NoOfBooks=0
                  4. Display() instance method displays Name,Author and NoOfBooks
                  5. Initialise instance variables in init method by accepting user input
                  6. Inside init method increment value of NoOfBooks by 1
--------------------------------------------------------------------------------------------------------"""
class BookStore:
    NoOfBooks=0
    #This method initialise instance variables
    def __init__(self,bookName,bookAuthor):
        self.Name=bookName
        self.Author=bookAuthor
        BookStore.NoOfBooks+=1

    #This method Displays a Book details
    def Display(self):
        print("---------------------------------------------------------")
        print(f"Displaying Book Details for Book '{self.Name}' \n")
        print(f"\n'{self.Name}' by '{self.Author}'. No Of Books:{BookStore.NoOfBooks}") 
        print("---------------------------------------------------------")

    def __str__(self):
        bookDetails=""
        #bookDetails+="\n---------------------------------------------------------"    
        bookDetails+="\nBook Name:"+str(self.Name)
        bookDetails+="\nBook Author:"+str(self.Author)
        bookDetails+="\nTotal Book Count in Book Store:"+str(BookStore.NoOfBooks)
        return bookDetails 

    #--------------------------------------------------------------------------------------
    # This function accepts book details from the user
    #--------------------------------------------------------------------------------------
    @staticmethod
    def acceptBookDetails():
        try:
            print("\nEnter the Book Details ,Book Name And Author....\n\n")
            bookName=input("Book Name:")
            bookAuthor=input(f"Author of book '{bookName}':")  
        except Exception as excObj:
                print("\n\nExceptiom occured :",excObj)  
        return bookName,bookAuthor     
    #-----------------------------------------------------------------------------------------
    #This function creates the BookStore objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def CreateBookStoreObjects():
        bookStoreObjCount = 0     
        createMoreObject="Yes"
        bookStoreObjList=[]      #creating list of Book Store objects
        bookStoreObj=""
        print("---------------------------------------------------------")
        print("Creating 'Book Store' objects")

        while (createMoreObject.lower()=="yes" or createMoreObject.lower()=="y"):
            bookStoreObjCount=bookStoreObjCount+1
            print("---------------------------------------------------------")
            print(f"Accepting Book Details for Book Number : {bookStoreObjCount}  ")
            print("---------------------------------------------------------")
            #Accepting Book name and Author from user
            bookName,bookAuthor=BookStore.acceptBookDetails()
            #Creating BookStore Object
            bookStoreObj=BookStore(bookName,bookAuthor)
            #Calling Display() instance method
            bookStoreObj.Display()
            bookStoreObjList.append(bookStoreObj)
            createMoreObject= input("\n\nContinue with creating more BOOK STORE Objects(Yes/No)??:")
        return bookStoreObjList    
    
    #-----------------------------------------------------------------------------------------
    #This function displays all created BookStore objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def PrintAllBooksInformation(bookStoreObjList):
        print("\n\n--------------------------------------------------------------")
        print(f"\tPrinting Details for All created Book Store Objects")
        print("-------------------------------------------------------------------")   
        bookCount=1
        for bookDetails in bookStoreObjList:   
            print("Book Number : ",bookCount)
            bookCount+=1
            print(bookDetails)
            print("--------------------------------------------------------------")  

  
#----------------------------------------------------------------------------------------------------------
# This function calls "CreateBookObjects" and "PrintAllBooksInformation methods
# --------------------------------------------------------------------------------------------------------
def main():
    try:   
        #This function creates the BookStore objects
        bookStoreObjList = BookStore.CreateBookStoreObjects()

        #This function displays all created BookStore objects
        BookStore.PrintAllBooksInformation(bookStoreObjList)   
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured :",excObj) 

#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------