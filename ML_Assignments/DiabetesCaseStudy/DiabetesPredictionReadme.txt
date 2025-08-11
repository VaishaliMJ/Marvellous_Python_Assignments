Diabetes Prediction using Logistic Regression and Pipeline

This project predicts whether a given patient is diabetic  or non-diabetic using “diabetes.csv”
It Follows  industrial best practices  by
	•	Automating preprocessing with Pipeline
	•	Scaling the dataset values using StandardScalar
	•	Used Logistic Regression as classification algorithm
	•	Saving and losing trained model using job lib
	•	Provided data visualiztion 

Dependencies:
Install the required Python packages before running the project
	pip install pandas numpy matplotlib scikit-learn joblib

DataSet information:
Features:
	1.	Pregnancies
	2.	Glucose
	3.	BloodPressure
	4.	SkinThickness
	5.	Insulin
	6.	BMI 
	7.	DiabetesPedigreeFunction
	8.	Age

Target:
	Outcome 
			0 : Non Diabetic
			1:  Diabetic


  

Workflow:
Data Preparation:
	•	Convert .csv file into data frame
	•	Replace ‘0’ values in the columns by column mean() value
	•	Convert all column values to numeric values

Train-Test-Split:
	•	Split data set into 80% Training and 20% Testing set

	•	Pipeline Construction:
	•	Step 1 : Standard scalar to scale all the features
	•	Step 2 : Used ‘Logistic Regression’ for result prediction

Model Training and Evaluation:
	•	Metrics: Accuracy,Confusion Matrix and Classification Report
	•	Feature Importance Plot: Shows most influential features

Model Saving and Loading:
	•	Save the model with joblib
	•	Load model for future predictions without retraining

Running the Project:
	•	Load data set (only once)
	⁃	pandas.read_csv(file_path)
	•	Train and evaluate model:
	⁃		python3 DiabetesPredictionUsingLR.py
	⁃	Expected Output:
		-----------------------------------------------------------------
						Zero values in column report
		-----------------------------------------------------------------
                   		 	ColName  Missing Value Count
		0               Pregnancies                  111
		1                   Glucose                    5
		2             BloodPressure                   35
		3             SkinThickness                  227
		4                   Insulin                  374
		5                       BMI                   11
		6  DiabetesPedigreeFunction                    0
		7                       Age                    0


			-----------------------------------------------------------------
					Comparision matrix for algorithm....
			-----------------------------------------------------------------
       		 Algorithm Name  Training Accuracy  Accuracy Score  ... Precision    Recall  F1 Score
			0  Logistic Regression           77.52443       76.623377  ...  0.686275  0.636364  0.660377

			[1 rows x 8 columns]

		⁃	Algorithm Name  Training Accuracy  Accuracy Score  ... Precision    Recall  F1 Score
		⁃	Model saved to path :diabetes_sample/diabetes_pipeline.joblib
		⁃	Model saved to path :diabetes_sample/diabetes_pipeline.joblib
		⁃	Model loaded from the path :diabetes_sample/diabetes_pipeline.joblib
		⁃	Selected sample data for testing is 
		⁃	:      Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
		542         10.0            90.0           85.0  ...                     0.825   56        1
		⁃	[1 rows x 9 columns]
		⁃	Loaded model prediction for randomly selected test sample:Non Diabetic
Visualiztions:
	•	Feature importance
	•	Confusion matrix 
Model Storage:
	•	Model is saved as ‘diabetes_pipeline.joblib’
	•	Can be loaded anytime for prediction without retraining
	⁃	trainedModel=loadTrainedModel(‘diabetes_sample/diabetes_pipeline.joblib’)
Sample Prediction:
    result=['Non Diabetic','Diabetic']
    sample =dfDiabetes.sample(n=1)
    predictedResult=model.predict(sample.drop(columns=['Outcome']))
    print(f"Selected sample data for testing is \n: {sample}")
    print(f"Loaded model prediction for randomly selected test sample:{result[predictedResult[0]]}")
Author:
Vaishali Jorwekar
Date: 11-08-2025




















 
