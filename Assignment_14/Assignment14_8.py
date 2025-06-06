"""-----------------------------------------------------------------------------------------------------
                          Assignment14_8
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Vehicle,method name start()
                    2. Derived class Car ,override method start()
                    3. Show method overriding
---------------------------------------------------------------------------------------------------------"""
class Vehicle:
    # Init method
    def __init__(self,startType):
        self.vehicleStartType=startType

    #start method    
    def start(self):
        print("\nIn start method of Vehicle")
        print("\nVehicle start type is :",self.vehicleStartType)
#-------------------------------------------------------------------------------------------------------
class Car(Vehicle):
    #init method
    def __init__(self, startType):
        super().__init__(startType)
        self.vehicleStartType=startType
        

    #Overriding Start method
    def start(self):
        print("\nIn start method of Car")
        print("\nCar start type is :",self.vehicleStartType)

#--------------------------------------------------------------------------------------------------------    
# This is main method creates vehicle and car object and sets details
#------------------------------------------------------------------------------------------------------         
def main():
    vehicleObj=""
    carObj=""
    try:
        #Creating Vehicle object
        vehicleObj=Vehicle("Manual")
        #Creating Car object
        carObj=Car("Automatic")

        #vehicle start() method
        vehicleObj.start()    # output:  In start method of Vehicle
                              #          Vehicle start type is: Manual  

        # Car start() method
        carObj.start()    # Output : In start method of Car
                          #          Car start type is : Automatic
        
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

 


        
        