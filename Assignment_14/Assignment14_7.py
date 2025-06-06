"""-----------------------------------------------------------------------------------------------------
                          Assignment14_7
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Create class Person
                    2. Person Instance variables : name and age
                    3. Derived class Teacher 
                    4. Teacher instance variables : subject and salary
                    5. Use super() to call base class constructor and print both
---------------------------------------------------------------------------------------------------------"""
class Person:
    #Instance variables
    def __init__(self,personName,personAge):
        self.name=personName
        self.age=personAge

    #Display details 
    # def displayDetails(self):
    #     print("\n--------In Base class Person Display method-------------")
    #     print("\n------------------------------------------------------------")

    #     print("\nPerson Details Are:")
    #     print("\n--------------------------------------------------------")

    #     print("\nPerson Name:",self.name)
    #     print("\nPerson Age:",self.age)   

    def __str__(self):    
        return f"Person details are : \nName: {self.name} \nAge:{self.age}"
       
   
#--------------------------------------------------------------------------------------------------------    

class Teacher(Person):
    #Init method for teacher class
    def __init__(self, personName, personAge,teacherSubject,teacherSalary):
        super().__init__(personName, personAge)
        self.subject=teacherSubject
        self.salary=teacherSalary

    #Display details 
    
    """ 
    def displayDetails(self)    
        print("\n-----In dervived Teacher class Display method---------------")
        print("\n------------------------------------------------------------")
        print("\nTeacher Details Are:")
        print("\n------------------------------------------------------------")
        print("\nTeacher Name:",self.name)
        print("\nTeacher Age:",self.age)   
   
        print("\nTeacher Subject:",self.subject)
        print("\nTeacher Salary",self.salary)  """  

    def __str__(self):    
        return f"Tecaher details are : \nName: {self.name} \nAge:{self.age}\nSubject:{self.subject}\nSalary:{self.salary}"
       
#--------------------------------------------------------------------------------------------------------    

#Accept  details  
def acceptPersonDetails():
    try:
            print("\nEnter details....\n")
            personName=input("\nPerson Name :")
            personAge=float(input("\nPerson Age:"))
            teacherSubject=input("\nTeacher Subject:")
            teacherSalary=float(input("\nTeacher Salary:"))
    except Exception as excObj:
            print("\n\nExceptiom occured :",excObj)  
    return personName,personAge,teacherSubject,teacherSalary


#--------------------------------------------------------------------------------------------------------    
# This is main method creates teacher object and sets details
#------------------------------------------------------------------------------------------------------         
def main():
    teacherObj=""
    personObj=""
    try:
         personName,personAge,teacherSubject,teacherSalary=acceptPersonDetails()
         print("Creating Person object")
         personObj=Person(personName,personAge)
         print("Creating Teacher object")
         teacherObj=Teacher(personName,personAge,teacherSubject,teacherSalary)
         #personObj.displayDetails()
         #teacherObj.displayDetails() 
         print("\n-----------------------------------------------")
         print("Displaying Person object")
         print(personObj)
         print("\n-----------------------------------------------")
         print("Displaying Teacher object")
         print(teacherObj)  
        
    except ValueError as errObj:
        print("\n\nError while accepting element:",errObj)   
    except Exception as excObj:
        print("\n\nException occured in main :",excObj)       

#--------------------------------------------------------------------------------------------------------
# Entry point for program
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()        
                     
       
   

