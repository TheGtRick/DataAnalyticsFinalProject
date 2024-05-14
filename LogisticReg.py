import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
data = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\MeteoData.csv')
#Our target is City
X = data[['Temperature', 'WindSpeed', 'WindDirection', 'BarometricPressure', 'Visibility', 'Humidity', 'Clouds', 'DateAndTime']]
y = data['City']
# We need to extact year month and etc. to make them numeric
X['DateAndTime'] = pd.to_datetime(X['DateAndTime'])
X['Hour'] = X['DateAndTime'].dt.hour
X['DayOfWeek'] = X['DateAndTime'].dt.dayofweek
X['Month'] = X['DateAndTime'].dt.month
X['Year'] = X['DateAndTime'].dt.year
X = X.drop('DateAndTime', axis=1)
# Spliting data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Creating a Logistic Regression model
logreg_model = LogisticRegression()
# Training
logreg_model.fit(X_train, y_train)
# Prediction
y_pred = logreg_model.predict(X_test)
#Accuracy and etc.
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
print(f'Classification Report:\n{classification_report(y_test, y_pred)}')
