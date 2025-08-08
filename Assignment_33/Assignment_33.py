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
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

BORDER="-"*60
"""---------------------------------------------------------------------------------
#  Step - 1.1
#  This method loads the data set from 'student-mat.csv' file
#  Input params : Data file path
#  Output       : Data frame
#---------------------------------------------------------------------------------"""
def DataLoading():
    studentDF=pd.read_csv("student-mat.csv",sep=";")
    #print(studentDF.columns)    
    # studentDF=studentDF[['studytime','failures','absences','G1','G2','G3']]
    # studentDF.to_csv("StudentExtractedData.csv")
    return studentDF
"""---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------"""
def preprocessing(studentDF):
    
    xFeatures=['studytime','failures','absences','G1','G2','G3']
    #xFeatures=studentDF.iloc[:,[13,14,29,30,31,32]].values
    studentDF.to_csv("StudentExtractedData.csv")
    """Dropping na values"""
    studentDF=studentDF.dropna(subset=xFeatures)

    extractedData=studentDF[xFeatures].copy()
    print("Extracted Data set")
    print(extractedData)

    # Heatmap for feature relationships
    sns.heatmap(extractedData.corr(), annot=True, cmap='coolwarm')
    plt.show()
    """Scaling the dataset using standard scalar"""
    #scaler = StandardScaler()
    #extractedData = scaler.fit_transform(extractedData)
    #extractedData=((extractedData-extractedData.min())/(extractedData.max()-extractedData.min()))*9+1
    #scalar=MinMaxScaler(feature_range=(0, 10))
    # scalar=StandardScaler()
    # df_scaled_array = scalar.fit_transform(extractedData)
    # df_scaled = pd.DataFrame(df_scaled_array, columns=extractedData.columns)
    # print("Scaled data")
    # print(df_scaled)
    # print(df_scaled.describe())
    # df_scaled.to_csv("StudentExtractedData.csv")

    # return df_scaled

    return extractedData
"""---------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------"""
def ModelBuildingKMeansClustering(extractedDF):
    xFeatures=extractedDF
    print("Xfeatures:\n",xFeatures)
    
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

    #xFeatures=['studytime','failures','absences','G1','G2','G3']

    model=KMeans(n_clusters=3,init='k-means++',n_init=10,random_state=42)
    
    y_kMeans=model.fit_predict(extractedDF)
    extractedDF['cluster']=y_kMeans
    print("Clustered data....")
    print(extractedDF)
    


    df0=extractedDF[extractedDF.cluster==0]
    df1=extractedDF[extractedDF.cluster==1]
    df2=extractedDF[extractedDF.cluster==2]

    sns.pairplot(extractedDF,hue="cluster")
    plt.show()

    
   
    plt.figure(figsize=(10,8))
    plt.scatter(df0[["G1","G2","G3"]],df0[["studytime","failures","absences"]],color="green",label="Top Performer")
    plt.scatter(df1[["G1","G2","G3"]],df1[["studytime","failures","absences"]],color="blue",label="Average Students")
    plt.scatter(df2[["G1","G2","G3"]],df2[["studytime","failures","absences"]],color="red",label="Struggling Student")
    plt.title("All Grades VS Study Time,failure,absenses")
    plt.xlabel("G1,G2,G3 Grades")
    plt.ylabel("Study Time,Failure and absenses")
    plt.legend()
    plt.show()   
    

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
"""---------------------------------------------------------------------------------------------------------
    Step 1: Load Data file
    Step 2: Select required columns from the data set

""---------------------------------------------------------------------------------------------------------"""
def StudentsClustering():
    studentDF=DataLoading()
    print(studentDF.head())
    extractedDF=preprocessing(studentDF)
    print(extractedDF.head())
    ModelBuildingKMeansClustering(extractedDF)
"""---------------------------------------------------------------------------------------------------------
  Main function 
---------------------------------------------------------------------------------------------------------"""
def main():
    StudentsClustering()
#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
