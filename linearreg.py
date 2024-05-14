import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\MeteoData.csv')
# Our data
# We want to predict temperature and humidity
X = data[['WindSpeed', 'WindDirection', 'BarometricPressure', 'Visibility', 'Clouds', 'City', 'DateAndTime']]
y = data[['Temperature', 'Humidity']]
# We need to extact year month and etc. to make them numeric
X['DateAndTime'] = pd.to_datetime(X['DateAndTime'])
X['Hour'] = X['DateAndTime'].dt.hour
X['DayOfWeek'] = X['DateAndTime'].dt.dayofweek
X['Month'] = X['DateAndTime'].dt.month
X['Year'] = X['DateAndTime'].dt.year
X = X.drop('DateAndTime', axis=1)
# Spliting into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Creating model here is Linear Regression
model = LinearRegression()
# Training model
model.fit(X_train, y_train)
# Making prediction
y_pred = model.predict(X_test)
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'R-squared: {r2_score(y_test, y_pred)}')
y_test = pd.DataFrame(y_test, columns=['Temperature', 'Humidity'])
y_test.reset_index(inplace=True)
y_pred = pd.DataFrame(y_pred, columns=['Temperature', 'Humidity'])
y_test.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-testL.csv', index=False)
y_pred.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-predL.csv', index=False)