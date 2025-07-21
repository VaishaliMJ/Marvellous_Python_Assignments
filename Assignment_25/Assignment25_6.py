"""-----------------------------------------------------------------------------------------------------
                          Assignment25_6
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
---------------------------------------------------------------------------------------------------------
Problem statement: Replace mutiple values in a column using a dictionary
---------------------------------------------------------------------------------------------------------"""                  
from sklearn import preprocessing
import pandas as pd
BORDER="-"*60
#---------------------------------------------------------------------------------
#  Label Encoding using dictionary
#---------------------------------------------------------------------------------

def labelEncoding():
    data={'Grade':['A+','B','A','C','B+']}
    gradeMappingDict={'A+':'Excellent','A':'Very Good','B+':'Good',"B":"Average",'C':'Poor'}
    gradeDF=pd.DataFrame(data)
    print(BORDER)
    print("\nDataFrame Before replacement:")
    print(gradeDF)
    print(BORDER)
    
    gradeDF.replace({'Grade':gradeMappingDict}, inplace=True)
    print("\nDataFrame after replacement:")
    print(gradeDF)
    print(BORDER)

    
    
#---------------------------------------------------------------------------------
#  Main function calls labelEncoding() 
#---------------------------------------------------------------------------------------------------------
def main():
    labelEncoding()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    main()