"""-------------------------------------------------------------------------------------------
                          Assignment 5_6
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------
Problem statement : This program accepts temperature in 
                    Celsius and converts it into Farenheit
-----------------------------------------------------------------------------------------"""
#-----------------------------------------------------------------------------------
#This function converts temperature to farenheit
#-----------------------------------------------------------------------------------
def convertToFarenheit(tempInCelsius):    
    print("------------------------------------------------------")
    tempInFarenheit = ((tempInCelsius*9)/5)+32
    print(f"Temperature {tempInCelsius}°C in Farenheit = {tempInFarenheit}°F")
    print("------------------------------------------------------")
#-----------------------------------------------------------------------------------
# This function accepts temperature in Celsius from users and calls function 
# convertToFarenheit(tempInCelsius) for conversion
#-----------------------------------------------------------------------------------
def main():
    tempInCelsius=int(input("Enter temperature in celsius:")) 
    convertToFarenheit(tempInCelsius)  
#-----------------------------------------------------------------------------------
# This is main entry point of the program
#-----------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------
