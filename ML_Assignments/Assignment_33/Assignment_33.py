"""-----------------------------------------------------------------------------------------------------
                          Assignment 33
                    (Student name - Vaishali Jorwekar)
                    Python by Marvellous Infosystems
--------------------------------------------------------------------------------------------------------
Problem statement:Cluster students into different academic performance group based on features like :
                        Final Grades,Study time,Failures,Absences
                  Based on this data identify
                        Top Performers,Average Students,Struggling students
--------------------------------------------------------------------------------------------------------"""
#####################################################################################################
# Required Python Packages
#####################################################################################################
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
#####################################################################################################
# Constants and file name
#####################################################################################################
BORDER="-"*65
FILENAME="student-mat.csv"
RANDOM_STATE=42
FEATURES=['studytime','failures','absences','G1','G2','G3']
NUM_CLUSTERS=3

#####################################################################################################
#   Function Name   :   loadStudentsData
#   Description     :   This method loads the data set from 'student-mat.csv' file
#   Input params    :   -
#   Output          :   Data frame
#####################################################################################################
def loadStudentsData():
    studentDF=pd.read_csv(FILENAME,sep=";")
    return studentDF
#####################################################################################################
#   Function Name   :   preprocessing
#   Description     :   Extracting required Features only
#   Input Params    :   Data Frame
#   Output          :   Extracted Data Frame
#####################################################################################################
def preprocessing(studentDF):
    studentDF.to_csv("StudentExtractedData.csv")
    """Dropping na values"""
    studentDF=studentDF.dropna(subset=FEATURES)

    extractedData=studentDF[FEATURES].copy()
    print("Extracted Data set")
    print(extractedData)

    # Heatmap for feature relationships
    sns.heatmap(extractedData.corr(), annot=True, cmap='coolwarm')
    plt.show()

    return extractedData
############################################################################################################
#   Function Name   :  plotKValueVsInertia
#   Description     :  Plots K values VS Inertia
#   Input Params    :   Data Frame
############################################################################################################
def plotKValueVsInertia(extractedDF):
    WCSS=[]
    for k in range(1,11):
        model=KMeans(n_clusters=k,init='k-means++',n_init=10,random_state=42)
        model.fit(extractedDF)
        print(f"K:{k} {model.inertia_}")   #WCSS
        WCSS.append(model.inertia_)
    plt.plot(range(1,11),WCSS,marker="o")
    plt.title("ElBow methods for K Means")
    plt.xlabel("Value of K")
    plt.ylabel("Within Cluster Sum of Squares")
    plt.grid(True)
    plt.show()


############################################################################################################
#   Function Name   :   buildModelForK
#   Description     :   Build Model for k=3
#   Input Params    :   data frame
#   Output          :   Data frame with 'cluster'
############################################################################################################
def buildModelForK(extractedDF):
    """Plot elbow value of k"""
    model=KMeans(n_clusters=3,init='k-means++',n_init=10,random_state=42)
    
    y_kMeans=model.fit_predict(extractedDF)
    extractedDF['cluster']=y_kMeans
    print("Clustered data....")
    print(extractedDF)
    return model,extractedDF
############################################################################################################
#   Function Name   :   ModelBuildingKMeansClustering
#   Description     :   Builds Model using K-Means 
#   Input Params    :   Extracted Data Frame
############################################################################################################
def ModelBuildingKMeansClustering(extractedDF):
    xFeatures=extractedDF
    print("Xfeatures:\n",xFeatures)
    """Plot K Values VS Inertia """
    plotKValueVsInertia(extractedDF)
    """Build model for k=3"""
    model,extractedDF=buildModelForK(extractedDF)


    df0=extractedDF[extractedDF.cluster==0]
    df1=extractedDF[extractedDF.cluster==1]
    df2=extractedDF[extractedDF.cluster==2]
    """Pair Plot"""
    plotPairPlot(extractedDF)
    

    plt.figure(figsize=(10,8))
    plt.scatter(df0["G3"],df0["studytime"],color="green",label="Top Performer")
    plt.scatter(df0["studytime"],df0["absences"],color="green")
    plt.scatter(df0["G3"],df0["failures"],color="green")


    plt.scatter(df1["G3"],df1["studytime"],color="blue",label="Average Students")
    plt.scatter(df1["studytime"],df1["absences"],color="blue")
    plt.scatter(df1["failures"],df1["absences"],color="blue")
    plt.scatter(df1["G3"],df1["failures"],color="blue")


    plt.scatter(df2["G3"],df2["studytime"],color="red",label="Struggling Students")
    plt.scatter(df2["G3"],df2["absences"],color="red")
    plt.scatter(df2["studytime"],df2["absences"],color="red")
    plt.scatter(df2["G3"],df2["failures"],color="blue")

    plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=100,c='yellow',label='centroid')
    plt.title("Cluster wise plotting")
    plt.legend()
    plt.show()    

    """Plot different features"""
    PlotSubPlotFeatures(df0, df1, df2)

############################################################################################################
#   Function Name   :   PlotSubPlotFeatures
#   Description     :   Plots different features
############################################################################################################

def PlotSubPlotFeatures(df0, df1, df2):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,8)) 
    axes[0][0].scatter(df0["G3"],df0["failures"],color="green",label="Top Performer")
    axes[0][0].scatter(df1["G3"],df1["failures"],color="blue",label="Average Students")
    axes[0][0].scatter(df2["G3"],df2["failures"],color="red",label="Struggling Student")
    axes[0][0].set_ylabel("Number of failures")
    axes[0][0].set_xlabel("Grades")
    axes[0][0].set_title("Grades Vs Failures plot")
    axes[0][0].legend()

    axes[0][1].scatter(df0["G3"],df0["studytime"],color="green",label="Top Performer")
    axes[0][1].scatter(df1["G3"],df1["studytime"],color="blue",label="Average Students")
    axes[0][1].scatter(df2["G3"],df2["studytime"],color="red",label="Struggling Student")
    axes[0][1].set_ylabel("studytime")
    axes[0][1].set_xlabel("Grades")
    axes[0][1].set_title("Grades Vs studytime plot")
    axes[0][1].legend()
    
    axes[1][1].scatter(df0["G3"],df0["absences"],color="green",label="Top Performer")
    axes[1][1].scatter(df1["G3"],df1["absences"],color="blue",label="Average Students")
    axes[1][1].scatter(df2["G3"],df2["absences"],color="red",label="Struggling Student")
    axes[1][1].set_ylabel("absences")
    axes[1][1].set_xlabel("Grades")
    axes[1][1].set_title("Grades Vs absences plot")
    axes[1][1].legend()
   

    axes[1][0].scatter(df0["studytime"],df0["absences"],color="green",label="Top Performer")
    axes[1][0].scatter(df1["studytime"],df1["absences"],color="blue",label="Average Students")
    axes[1][0].scatter(df2["studytime"],df2["absences"],color="red",label="Struggling Student")
    axes[1][0].set_ylabel("absences")
    axes[1][0].set_xlabel("studytime")
    axes[1][0].set_title("studytime Vs absences plot")
    axes[1][0].legend()
    plt.tight_layout()
    plt.show()
############################################################################################################
#   Function Name   :   plotPairPlot
#   Description     :   pair plot of features
############################################################################################################
def plotPairPlot(extractedDF):
    sns.pairplot(extractedDF,hue="cluster")
    plt.show()
############################################################################################################
#   Function Name   :   StudentsClustering
#   Description     :   Load Data file
#                       Select required columns from the data set
############################################################################################################
def StudentsClustering():
    studentDF=loadStudentsData()
    print(studentDF.head())
    extractedDF=preprocessing(studentDF)
    print(extractedDF.head())
    """Build Model using K-Means Clustering"""
    ModelBuildingKMeansClustering(extractedDF)
############################################################################################################
#   Function Name   :  Main function 
############################################################################################################
def main():
    StudentsClustering()
############################################################################################################
#Main entry point of the program
############################################################################################################
if __name__=="__main__":
    main()
