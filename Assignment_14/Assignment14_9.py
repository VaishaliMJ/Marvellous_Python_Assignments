"""-----------------------------------------------------------------------------------------------------
                          Assignment14_9
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Product
                    2. Attributes of Product class are : name and price
                    3. Implement __eq__ method to compare both products to check products as per price
---------------------------------------------------------------------------------------------------------"""
class Product:
    #init method
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __eq__(self, secondObj):
        if isinstance(secondObj,Product):
            return(self.price==secondObj.price)
        
        return False
#--------------------------------------------------------------------------------------------------------
# Accept product details
#--------------------------------------------------------------------------------------------------------  
def acceptProductDetails():
    try:
            productName=input("\nName :")
            productPrice=float(input("\nPrice:"))
    except Exception as excObj:
            print("\n\nException occured :",excObj)  
    return productName,productPrice

#--------------------------------------------------------------------------------------------------------    
# This is main method creates 2 products object and compares them
#------------------------------------------------------------------------------------------------------         
def main():
    productObj1=""
    productObj2=""
    try:
        #Accepting Product 1 details
        print("\nEnter Product 1 details....\n")

        product_1_Name,product_1_price=acceptProductDetails()
        #Accepting Product 2 Details
        print("\nEnter Product 2 details....\n")

        product_2_Name,product_2_price=acceptProductDetails()

        productObj1=Product(product_1_Name,product_1_price)

        productObj2=Product(product_2_Name,product_2_price)

        print("Both Products are equal:",end="")
        print(productObj1==productObj2)

        
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       

#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
                     
 
#-------------------------------------------------------------------------------------------------------        


                    