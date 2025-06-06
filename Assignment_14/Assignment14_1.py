"""-----------------------------------------------------------------------------------------------------
                          Assignment14_1
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Employee
                    2. Create attributes with name,emp_id,salary
                    3. Create objects of this class
                    4. Print their details using a method
---------------------------------------------------------------------------------------------------------"""
class Employee:
    EmployeeID=100
    #Init or constructor method
    def __init__(self):
        self.name=""
        self.emp_id=0
        Employee.EmployeeID+=1
        self.salary=0.0
        
    #----------------------------------------------------------------------------------------------------------    
    #This method creates objects of Employee class 
    #----------------------------------------------------------------------------------------------------------
    @staticmethod
    def acceptEmployeeDetails():
        try:
            print("\nEnter the Employee Details ,Employee Name,Employee Id and Salary...\n\n")
            empName=input("Employee Name:")

            #Generate Employee Id 
            
            #print(f"\nEmployee Id of '{empName}' :{self.emp_id}")

            #Employee Salary
            empSalary=float(input(f"\nEmployee salary:"))

        except ValueError as errObj:
            print("\n\nError while accepting element:",errObj)  

        except Exception as excObj:
                print("\n\nExceptiom occured in acceptEmployeeDetails():",excObj)  

        return empName,empSalary
    #----------------------------------------------------------------------------------------------------------    
    #This method Sets Values of Employee class 
    #----------------------------------------------------------------------------------------
    
    def setEmployeeDetails(self,empName,empSalary):
        self.name=empName
        self.salary=empSalary
        self.emp_id=Employee.EmployeeID

    #----------------------------------------------------------------------------------------------------------           
    #This method Displays a Employee details
    #----------------------------------------------------------------------------------------------------------
    def displayEmployeeDetails(self):
        print("---------------------------------------------------------")
        print(f"Displaying Employee Details '{self.name}' \n")
        print("-----------------------------------------------------------")            
        print(f"\nName        :  {self.name} ")
        print(f"\nEmployee Id :  {self.emp_id}") 
        print(f"\nSalary      :  {self.salary}")      
        print("-----------------------------------------------------------")            

    #-----------------------------------------------
    #This method return Employee object created
    #--------------------------------------------
    def __str__(self):
        empDetails=""
        empDetails+="\nName:"+str(self.name)
        empDetails+="\nEmployee Id:"+str(self.emp_id)
        empDetails+="\nSalary:"+str(self.salary)
        return empDetails     
#-----------------------------------------------------------------------------------------
    #This function creates the Employee objects
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def createEmployees():
        empObjCount = 0     
        addMoreEmp="Yes"
        EmployeeObjList=[]      #creating list of Employee objects
        empObj=""
        try:    
            print("---------------------------------------------------------")
            print("Creating 'Employee' ")

            while (addMoreEmp.lower()=="yes" or addMoreEmp.lower()=="y"):
                empObjCount=empObjCount+1
                print("---------------------------------------------------------")
                print(f"Accepting Employee Details for Employee : {empObjCount}  ")
                print("---------------------------------------------------------")
                
                #Accepting Employee name and Salary from user
                empName,empSalary=Employee.acceptEmployeeDetails()
                #Creating Employee Object
                empObj=Employee()
                #setting values of name and Salary ....generating emp id
                empObj.setEmployeeDetails(empName,empSalary)
                #Calling Display() instance method
                empObj.displayEmployeeDetails()
                EmployeeObjList.append(empObj)
                addMoreEmp= input("\n\nContinue with creating more EMPLOYEES(Yes/No)??:")
        except ValueError as errObj:
         print("\n\nError while accepting element in createEmployees():",errObj)   
        except Exception as excObj:
         print("\n\nException occured in createEmployees() :",excObj)   
        return EmployeeObjList    
    #-----------------------------------------------------------------------------------------
    #This function displays all created Employees Details
    #-----------------------------------------------------------------------------------------
    @staticmethod
    def displayAllEmployeesInfo(employeeList):
        print("\n\n--------------------------------------------------------------")
        print(f"\nDisplaying Details of all newly created Employees ")
        print("-------------------------------------------------------------------")   
        empCount=1
        for empDetails in employeeList:   
            print("New Employee : ",empCount)
            empCount+=1
            print(empDetails)
            print("--------------------------------------------------------------")  

#----------------------------------------------------------------------------------------------------------
# This function calls "createEmployees" and "displayAllEmployeesInfo" methods
# --------------------------------------------------------------------------------------------------------
def main():  
    try:
        #This function creates the Employee objects
        employeeList = Employee.createEmployees()

        #This function displays all created Employee objects
        Employee.displayAllEmployeesInfo(employeeList) 

    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)     
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------