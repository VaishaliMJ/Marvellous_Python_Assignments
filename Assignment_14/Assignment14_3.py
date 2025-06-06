"""-----------------------------------------------------------------------------------------------------
                          Assignment14_2
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Book
                    2. Book class has private attribute __price
                    3. Add methods to get and set price
                    4. Implement Encapsulation
---------------------------------------------------------------------------------------------------------"""
class Book:
    #Init or Constructor
    def __init__(self):
        self.__price=0.0
        #self.BookName=""

    #This method accepts Book name and price
    @staticmethod
    def AcceptBookDetails():
        try:
            #bookName=input("Enter Book Name:")
            bookPrice=float(input("Enter Book price:"))
        except ValueError as errObj:
            print("\n\nError while accepting book name or price:",errObj)  

        except Exception as excObj:
                print("\n\nExceptiom occured in AcceptNameAndPrice():",excObj)  
        #return bookName,bookPrice  
        return bookPrice
    
    #Setter method for __price
    def set__price(self,bookPrice):
        print("In setter 'set__price()' method......")
        self.__price= bookPrice


    #Getter method for __price  
    def get__price(self):
        print("In getter 'get__price()' method......")
        return self.__price  
    
        
#--------------------------------------------------------------------------------------------------------    
# This is main method creates Book object and calls setters and getters for price
#--------------------------------------------------------------------------------------------------------
def main():
    try:
        #This function creates the Book class object
        bookObj=Book()
        bookPrice=Book.AcceptBookDetails()

        
        #Calling setter method for price
        bookObj.set__price(bookPrice)

        #Calling Getter method
        print(bookObj.get__price())
        
        #print(bookObj.__price)       # can't access attribute directly ....Error message
        

    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       



#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
