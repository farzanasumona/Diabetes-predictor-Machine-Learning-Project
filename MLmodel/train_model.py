import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


df = pd.read_csv('diabetes_prediction_dataset.csv')
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull())

gender_map = {'Female': 0.0, 'Male': 1.0, 'Other': 2.0}
df['gender'] = df['gender'].map(gender_map)

smoking_map = {'never': 0.0, 'current': 1.0, 'former': 2.0, 'No Info': 3.0, 'not current': 4.0, 'ever': 5.0}
df['smoking_history'] = df['smoking_history'].map(smoking_map)
df = df.astype(float)

# missing_values = df.isnull().sum()
# print(missing_values)

feature_names = df.columns.tolist()
column_to_drop = 'diabetes'
if column_to_drop in feature_names:
    feature_names.remove(column_to_drop)
# print(feature_names)

#split dataset
x = df.drop('diabetes', axis='columns')
y = df['diabetes']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10000)
y_train = np.ravel(y_train)

x_train_df = pd.DataFrame(x_train, columns=feature_names)
x_test_df = pd.DataFrame(x_test, columns=feature_names)

model = RandomForestClassifier(n_estimators=100, criterion='gini')
model.fit(x_train_df, y_train)

y_pred = model.predict(x_test_df)
# print(y_pred)
accuracy = model.score(x_test_df, y_test)
print("Accuracy:", accuracy)
patient = [1.0, 57.0, 0.0, 0.0, 3.0, 57.1, 6.5, 126.0]
patient_df = pd.DataFrame([patient], columns=feature_names)
prediction = model.predict(patient_df)
if prediction == 0:
    print("Diabetes test result is negative")
else:
    print("Diabetes test result is positive")
