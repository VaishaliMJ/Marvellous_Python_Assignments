"""-----------------------------------------------------------------------------------------------------
                          Assignment18_4
                    (Student name - Vaishali Jorwekar)
                     Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement : This program implements following functionalities
                    1. Accepts two file names from the user
                    2. If both file content are same then display success
                    3. Otherwise display failure
                    4. Accept input from command line
---------------------------------------------------------------------------------------------------------"""
import os,sys,filecmp
import Assignment18_Module as Module
Border="-"*55
#------------------------------------------------------------------------
# This function compares two file content
#---------------------------------------------------------------------
def compareInputFiles(fileName1,fileName2):
    print(f"\nSerching File '{fileName1}'.....")
    isExists_file1,currDirectory=Module.checkIfFileExists(fileName1)
    print(f"\nSearching file '{fileName2}'.....")

    isExists_file2,currDirectory=Module.checkIfFileExists(fileName2)
    absFileName1=os.path.join(currDirectory,fileName1)
    absFileName2=os.path.join(currDirectory,fileName2)
    #print(fileName1)
    #print(fileName2)
    if(isExists_file1 and isExists_file2):
        print(f"Found both files '{fileName1}' and '{fileName2}'")  
        isEqual=filecmp.cmp(absFileName1,absFileName2)
        if(isEqual):
           print(f"Content of '{fileName1}' and '{fileName2}' are same")  
        else:
           print(f"Content of '{fileName1}' and '{fileName2}' are not same")  
    
    else:
        if(not(isExists_file1)):
            print(f"'{fileName1}' file not found...") 
        elif(not(isExists_file2)):
            print(f"'{fileName2}' file not found...") 
        return   
    
# This function accepts inputs from command line
#----------------------------------------------------------------------   
def initScript():
    try:
        print(Border)
        print("--------Compares File 1 and File 2 content---------")
        print(Border)    #Logic
        if(len(sys.argv)==1):
            Module.invalidArgsMsg()
        elif(len(sys.argv)==2):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to comapre two files")
                print("This Script compares two files ")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")  
                print("ScriptName.py  FileName1 FileName2")  
                print("Please provide valid absolute path....")
            else:
                Module.invalidArgsMsg()   
        elif(len(sys.argv)==3):
            compareInputFiles(sys.argv[1],sys.argv[2])
        else:
            Module.invalidArgsMsg()        
        print(Border)
    except Exception as excObj:
        print("\nError while accepting the command line arguments...",excObj)
#--------------------------------------------------------------------------------------
# This is main function calls initScript()
#-------------------------------------------------------------------------------------    
def main():
    try:
       initScript()
    except Exception as exeObj:
        print("\nException in method main()",exeObj)   
#------------------------------ENTRY POINT OF PROGRAM-------------------------------------------
if __name__=="__main__":
    main()
#-----------------------------------------------------------------------------------------------