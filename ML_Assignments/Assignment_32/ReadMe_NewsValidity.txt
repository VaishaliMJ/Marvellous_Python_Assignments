Priblem Statement:
Problem statement: Predict whether a news article is Fake or Real using text classification technique.
                  This assignment dmonstrates the power of ensemble learning using a voting classifier 
                  with models like Logistic Regression ,Decision tree

Data File :	Fake.csv, True.csv
interaction details.It Follows  industrial best practices  by
	•	Used Logistic Regression ,Decision tree individually and with Votiong Classifier(hard and Soft)
	•	Used TF-IDF Vectorization to convert text into numerical values
	•	Saving and loading trained model and Vectorizer using job lib
	•	Provided data visualiztion 

Dependencies:
Install the required Python packages before running the project
	pip install pandas numpy matplotlib scikit-learn joblib

DataSet information:
Features:
	1.	text
	2.	title

Target:
	Label
		0	Fake
		1	True
  

Workflow:
Data Preparation:
	•	Convert both .csv file into data frame
	•	combine both datasets into one with target as 'label' : 0 = Fake , 1 =True 
	•	Used 'text' feature for vector calculations
	•	Convert column values to numeric values using vectorizer

Train-Test-Split:
	•	Split data set into 80% Training and 20% Testing set
	•	Used Decision Tree Logistic Regression ,Decision tree individually and combined with
		Voting classification (hard and soft)

Model Training and Evaluation:
	•	Metrics: Accuracy,Confusion Matrix and Classification Report

Model Saving and Loading:
	•	Save the all models and vectorizer with joblib
	•	Load models for future predictions without retraining

Running the Project:
	•	Load both data set (only once)
	⁃	pandas.read_csv(file_path)
	•	Train and evaluate model:
		- Training module
	⁃		python3 NewsValidity.py
		- Testing module
			NewsValidityTestingModule.py

Expected Output:
		-Vectorizer saved to path :NEWS_VALIDITY/Tf-IDF_Vectorizer_Module.joblib
        -Model saved to path :NEWS_VALIDITY/Decision Tree.joblib	
		-Model saved to path :NEWS_VALIDITY/Logistic Regression.joblib
		-Model saved to path :NEWS_VALIDITY/Voting Classifier Hard.joblib
		-Model saved to path :NEWS_VALIDITY/Voting Classifier Soft.joblib
		-----------------------------------------------------------------
		Comparision matrix for algorithm....
		-----------------------------------------------------------------
				Algorithm Name  Training Accuracy  Accuracy Score          Confusion Matrix
		0           Decision Tree          99.997216       99.465479  [[4628, 22], [26, 4304]]
		1     Logistic Regression          99.120218       98.797327  [[4580, 70], [38, 4292]]
		2  Voting Classifier Hard          99.593519       99.298441   [[4645, 5], [58, 4272]]
		3  Voting Classifier Soft          99.997216       99.510022  [[4631, 19], [25, 4305]]
		-----------------------------------------------------------------
		Actual VS Predicted values
		-----------------------------------------------------------------
			Actual  Decision Tree  ...  Voting Classifier Hard  Voting Classifier Soft
		799         0              0  ...                       0                       0
		6500        0              0  ...                       0                       0
		3590        0              0  ...                       0                       0
		1377        1              1  ...                       1                       1
		11059       0              0  ...                       0                       0
		...       ...            ...  ...                     ...                     ...
		20702       0              0  ...                       0                       0
		4068        1              1  ...                       1                       1
		1081        0              0  ...                       0                       0
		14658       1              1  ...                       1                       1
		15236       1              1  ...                       1                       1



Visualiztions:
	•	Confusion matrix (Logistic Regression,Decision tree individually and with 
		      Votiong Classifier(hard and Soft))
	•	Accuracy comparision of Logistic Regression ,Decision tree individually and with Votiong Classifier(hard and Soft)

Model Storage:
		-Vectorizer saved to path :NEWS_VALIDITY/Tf-IDF_Vectorizer_Module.joblib
        -Model saved to path :NEWS_VALIDITY/Decision Tree.joblib	
		-Model saved to path :NEWS_VALIDITY/Logistic Regression.joblib
		-Model saved to path :NEWS_VALIDITY/Voting Classifier Hard.joblib
		-Model saved to path :NEWS_VALIDITY/Voting Classifier Soft.joblib


	•	Can be loaded anytime for prediction without retraining
	-   vectorizer=loadVectorizer(NEWS_VALIDITY/Tf-IDF_Vectorizer_Module.joblib)
	⁃	trainedModel=loadTrainedModel(‘NEWS_VALIDITY/Decision Tree.joblib’)
	⁃	trainedModel=loadTrainedModel(‘NEWS_VALIDITY/Logistic Regression.joblib’)
	⁃	trainedModel=loadTrainedModel(‘NEWS_VALIDITY/Voting Classifier Hard.joblib’)


Sample Prediction:
	sampleTestData =df.sample(n=1)

	textNews=sampleData[TRANSFORM_FEATURE]
    vectorizer=loadVectorizer()
    feature = vectorizer.transform(textNews)

	result=["Fake News","True News"]
    predictedResult=model.predict(sampleData.drop(columns=[TARGET_COLNAME]))
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
    print(BORDER)

Author:
Vaishali Jorwekar
Date: 14-08-2025




















 
