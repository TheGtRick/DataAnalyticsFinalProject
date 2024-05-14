import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\MeteoData.csv')
X = data[['Humidity', 'WindSpeed', 'WindDirection', 'BarometricPressure', 'Visibility', 'Clouds', 'City', 'DateAndTime']]
y = data[['Temperature']]
# We need to extact year month and etc. to make them numeric
X['DateAndTime'] = pd.to_datetime(X['DateAndTime'])
X['Hour'] = X['DateAndTime'].dt.hour
X['DayOfWeek'] = X['DateAndTime'].dt.dayofweek
X['Month'] = X['DateAndTime'].dt.month
X['Year'] = X['DateAndTime'].dt.year
X = X.drop('DateAndTime', axis=1)
#Spliting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Creaeting model amd adding parameters for it
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error')
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)
y_pred = model.predict(X_test_scaled)
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'R-squared: {r2_score(y_test, y_pred)}')
y_test = pd.DataFrame(y_test, columns=['Temperature'])
y_test.reset_index(inplace=True)
y_pred = pd.DataFrame(y_pred, columns=['Temperature'])
y_test.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-testN.csv', index=False)
y_pred.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-predN.csv', index=False)