"""-----------------------------------------------------------------------------------------------------
                          Assignment14_10
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Employee
                    2. Demonstrate public,private and Protected access modifiers
                    3. Class variable are : __salary,_department,name
---------------------------------------------------------------------------------------------------------"""  
class Employee:
    #init method
    def __init__(self,name,dept,sal):
        #Public variable,Accessible everywhere
        self.name=name
        #Protected Variable,Accessible within class and derived class as well
        self._department=dept
        #private variable,Accessible within class only
        self.__salary=sal

    #Display employee details
    def displayEmployeeDetails(self):
        print("\n-------------------------------------------")
        print("\nEmployee Details : Employee class") 
        print("\n-------------------------------------------")
        print("\nEmployee Name       : ",self.name)             #Prints name
        print("\nEmployee Department : ",self._department)      #Prints department
        print("\nEmployee Salary     : ",self.__salary)         #Prints salary

   
#-------------------------------------------------------------------------------------------------------
class GovtEmployee(Employee):
    def __init__(self, name, dept, sal):
        super().__init__(name, dept, sal)

    def displayGovtEmployeeDetails(self):
        print("\n-------------------------------------------")
        print("\nGoverment Employee Details : Employee class") 
        print("\n-------------------------------------------")
        print("\nEmployee Name       : ",self.name)             #Prints name
        print("\nEmployee Department : ",self._department)      #Prints department

        #print("\nEmployee Salary     : ",self.__salary)         #Error 
        #Description of Error: 'GovtEmployee' object has no attribute '_GovtEmployee__salary'



#-------------------------------------------------------------------------------------------------------
#Accept Employee details
#-------------------------------------------------------------------------------------------------------
def acceptEmployeeDetails():
    try:
            print("\nEnter Employee details....\n")
            empName=input("\nEmployee Name       :")
            empDept=input("\nEmployee Deparatment:")
            empSalary=float(input("\nEmployee Salary:"))
    except Exception as excObj:
            print("\n\nExceptiom occured :",excObj)  
    return empName,empDept,empSalary
#--------------------------------------------------------------------------------------------------------
#Display employee details
def displayEmployee(empObj):
    print("\n-------------------------------------------")
    print("\nEmployee Details Outside class: Employee class") 
    print("\n-------------------------------------------")
    print("\nEmployee Name       : ",empObj.name)             #Prints name
    print("\nEmployee Department : ",empObj._department)      #Prints department
    #print("\nEmployee Salary     : ",empObj.__salary)         # Not accessible : salary
    #Description of Error: 'Employee' object has no attribute '__salary'
  
#--------------------------------------------------------------------------------------------------------    
# This is main method creates Employee object 
#------------------------------------------------------------------------------------------------------         
def main():
    empObj=""
    govtEmpObj=""
    try:
        #Creating Employee object
        empName,empDept,empSalary=acceptEmployeeDetails()
        empObj=Employee(empName,empDept,empSalary)
        #Display Employee Details
        empObj.displayEmployeeDetails()
        #Accessing Instance variables outside class
        displayEmployee(empObj)

        #Creating Derived class 
        print("\nEnter details for Goverment Employee...")
        print("\n------------------------------------------------")
        govtEmpName,govtEmpDept,govtEmpSalary=acceptEmployeeDetails()
        #Creating Govt Employee Object
        govtEmpObj=GovtEmployee(govtEmpName,govtEmpDept,govtEmpSalary)
        #Display Employee Details
        govtEmpObj.displayGovtEmployeeDetails()
        #Accessing Instance variables outside class
        displayEmployee(govtEmpObj)
        
        
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       

#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
                     




         


