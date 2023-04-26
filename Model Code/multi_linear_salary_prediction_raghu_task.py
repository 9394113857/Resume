# -*- coding: utf-8 -*-
"""Multi_Linear_Salary_Prediction_raghu_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dqeZnbjsZ4FjGuTtI2A8Hllxo1rLcFOH
"""

# Importing the libraries
import pandas as pd

dataset = pd.read_csv('https://raw.githubusercontent.com/9394113857/Predict-Salary-Analysis/raghu/hiring.csv')

dataset.head()

# Replacing null values with zero:-
dataset['experience'].fillna(0, inplace=True)
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

# 0 to 3rd columns:-
X = dataset.iloc[:, :3]

X

#Converting words to integer values
def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))

X

y = dataset.iloc[:, -1]

y

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Model Accuracy Score:-
regressor.score(X, y)

X # These are the inputs we have to give to model when the model is loaded ok.

# These are y single outcome y is test results, we have given first x as train data, 
# then y is test data we are looking the samples okay, 
# but check actual predicted model results would near to the test results means we achieved our use-case ok.
y

import pickle

# Saving model to disk
pickle.dump(regressor, open('multi_linear_regression_salary_prediction.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('multi_linear_regression_salary_prediction.pkl','rb'))

model

type(model)

result = model.predict([[2, 9, 6]])
print(result)

"""# User Input:"""

Value_1 = float(input("Enter Experience | Eg: 2 "))
Value_2 = float(input("Enter Test Score | Eg: 9 "))
Value_3 = float(input("Enter Interview Score | Eg: 6 "))
print()

# Like this we have to load the saved model from path and test results with comparing test set results Ok.
predicted = model.predict([[Value_1, Value_2, Value_3]]) 

print("=================================================")
print("The predicted value from model : " + str(predicted))
print("=================================================")



"""#Regards
Raghu
"""

