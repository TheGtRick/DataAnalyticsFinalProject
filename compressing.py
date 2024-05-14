import pandas as pd
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\MeteoData.csv')
df['DateAndTime'] = pd.to_datetime(df['DateAndTime'])
df['Month'] = df['DateAndTime'].dt.to_period('M')
com_df = df.groupby(['Month', 'City']).agg({
    'Temperature': 'mean',
    'WindSpeed': 'mean',
    'WindDirection': 'mean',
    'BarometricPressure': 'mean',
    'Visibility': 'mean',
    'Clouds': 'mean',
    'Humidity': 'mean'
}).reset_index()
com_df.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv', index=False)