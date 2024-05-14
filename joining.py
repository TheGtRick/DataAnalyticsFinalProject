import pandas as pd
#We need to merge or join all tables to one
temperature = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table1.csv')
wind_speed = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table3.csv')
wind_direction = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table9.csv')
pressure = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table5.csv')
visibility = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table7.csv')
clouds = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table13.csv')
humidity = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table11.csv')
#We have some trash values or some mistakes in dataset
#We need to remove or replace them
temperature = temperature.drop(columns=['station'])
wind_speed = wind_speed.drop(columns=['station'])
wind_direction = wind_direction.drop(columns=['station'])
pressure = pressure.drop(columns=['station'])
visibility = visibility.drop(columns=['station'])
clouds = clouds.drop(columns=['station'])
humidity = humidity.drop(columns=['station'])
clouds.replace('*', '', inplace=True)
clouds.replace('*10', '10', inplace=True)
visibility.replace('>96', '', inplace=True)
# We have one column with date and 8 columns with values separated in time in one day
# We need to make 2 columns from them DateAndTime and Value(Temperature, 'WindSpeed' and etc.) for joining them into one df
melted_temperature = pd.melt(temperature, id_vars=['date'], var_name='Time', value_name='Temperature')
melted_wind_speed = pd.melt(wind_speed, id_vars=['date'], var_name='Time', value_name='WindSpeed')
melted_wind_direction = pd.melt(wind_direction, id_vars=['date'], var_name='Time', value_name='WindDirection')
melted_pressure = pd.melt(pressure, id_vars=['date'], var_name='Time', value_name='BarometricPressure')
melted_visibility = pd.melt(visibility, id_vars=['date'], var_name='Time', value_name='Visibility')
melted_clouds = pd.melt(clouds, id_vars=['date'], var_name='Time', value_name='Clouds')
melted_humidity = pd.melt(humidity, id_vars=['date'], var_name='Time', value_name='Humidity')
# Making column DateAndTime
melted_temperature['DateAndTime'] = melted_temperature['date'] + '-' + melted_temperature['Time']
melted_wind_speed['DateAndTime'] = melted_wind_speed['date'] + '-' + melted_wind_speed['Time']
melted_wind_direction['DateAndTime'] = melted_wind_direction['date'] + '-' + melted_wind_direction['Time']
melted_pressure['DateAndTime'] = melted_pressure['date'] + '-' + melted_pressure['Time']
melted_visibility['DateAndTime'] = melted_visibility['date'] + '-' + melted_visibility['Time']
melted_clouds['DateAndTime'] = melted_clouds['date'] + '-' + melted_clouds['Time'] 
melted_humidity['DateAndTime'] = melted_humidity['date'] + '-' + melted_humidity['Time']
# Droping unnecessary columns
melted_temperature = melted_temperature[['DateAndTime', 'Temperature']]
melted_wind_speed = melted_wind_speed[['DateAndTime', 'WindSpeed']]
melted_wind_direction = melted_wind_direction[['DateAndTime', 'WindDirection']]
melted_pressure = melted_pressure[['DateAndTime', 'BarometricPressure']]
melted_visibility = melted_visibility[['DateAndTime', 'Visibility']]
melted_clouds = melted_clouds[['DateAndTime', 'Clouds']]
melted_humidity = melted_humidity[['DateAndTime', 'Humidity']]
#Joining
data_almaty = pd.merge(melted_temperature, melted_wind_speed, on='DateAndTime')
data_almaty = pd.merge(data_almaty, melted_wind_direction, on='DateAndTime')
data_almaty = pd.merge(data_almaty, melted_pressure, on='DateAndTime')
data_almaty = pd.merge(data_almaty, melted_visibility, on='DateAndTime')
data_almaty = pd.merge(data_almaty, melted_clouds, on='DateAndTime')
data_almaty = pd.merge(data_almaty, melted_humidity, on='DateAndTime')
#Making some corrections
data_almaty['DateAndTime'] = pd.to_datetime(data_almaty['DateAndTime'], format='%Y-%m-%d-%H')
data_almaty = data_almaty.sort_values(by='DateAndTime')
numeric_columns = data_almaty.columns.difference(['DateAndTime'])
data_almaty[numeric_columns] = data_almaty[numeric_columns].apply(pd.to_numeric, errors='coerce')
data_almaty['Clouds'] = data_almaty['Clouds'].fillna(0)
data_almaty['Visibility'] = data_almaty['Visibility'].fillna(int(data_almaty['Visibility'].mean()))
data_almaty.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Almaty.csv', index=False)
#Same thing with Aktobe
temperature = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table2.csv')
wind_speed = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table4.csv')
wind_direction = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table10.csv')
pressure = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table6.csv')
visibility = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table8.csv')
clouds = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table14.csv')
humidity = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Table12.csv')

temperature = temperature.drop(columns=['station'])
wind_speed = wind_speed.drop(columns=['station'])
wind_direction = wind_direction.drop(columns=['station'])
pressure = pressure.drop(columns=['station'])
visibility = visibility.drop(columns=['station'])
clouds = clouds.drop(columns=['station'])
humidity = humidity.drop(columns=['station'])
clouds.replace('*', '', inplace=True)
clouds.replace('*10', '10', inplace=True)
visibility.replace('>96', '', inplace=True)

melted_temperature = pd.melt(temperature, id_vars=['date'], var_name='Time', value_name='Temperature')
melted_wind_speed = pd.melt(wind_speed, id_vars=['date'], var_name='Time', value_name='WindSpeed')
melted_wind_direction = pd.melt(wind_direction, id_vars=['date'], var_name='Time', value_name='WindDirection')
melted_pressure = pd.melt(pressure, id_vars=['date'], var_name='Time', value_name='BarometricPressure')
melted_visibility = pd.melt(visibility, id_vars=['date'], var_name='Time', value_name='Visibility')
melted_clouds = pd.melt(clouds, id_vars=['date'], var_name='Time', value_name='Clouds')
melted_humidity = pd.melt(humidity, id_vars=['date'], var_name='Time', value_name='Humidity')

melted_temperature['DateAndTime'] = melted_temperature['date'] + '-' + melted_temperature['Time']
melted_wind_speed['DateAndTime'] = melted_wind_speed['date'] + '-' + melted_wind_speed['Time']
melted_wind_direction['DateAndTime'] = melted_wind_direction['date'] + '-' + melted_wind_direction['Time']
melted_pressure['DateAndTime'] = melted_pressure['date'] + '-' + melted_pressure['Time']
melted_visibility['DateAndTime'] = melted_visibility['date'] + '-' + melted_visibility['Time']
melted_clouds['DateAndTime'] = melted_clouds['date'] + '-' + melted_clouds['Time'] 
melted_humidity['DateAndTime'] = melted_humidity['date'] + '-' + melted_humidity['Time']

melted_temperature = melted_temperature[['DateAndTime', 'Temperature']]
melted_wind_speed = melted_wind_speed[['DateAndTime', 'WindSpeed']]
melted_wind_direction = melted_wind_direction[['DateAndTime', 'WindDirection']]
melted_pressure = melted_pressure[['DateAndTime', 'BarometricPressure']]
melted_visibility = melted_visibility[['DateAndTime', 'Visibility']]
melted_clouds = melted_clouds[['DateAndTime', 'Clouds']]
melted_humidity = melted_humidity[['DateAndTime', 'Humidity']]

data_aktobe = pd.merge(melted_temperature, melted_wind_speed, on='DateAndTime')
data_aktobe = pd.merge(data_aktobe, melted_wind_direction, on='DateAndTime')
data_aktobe = pd.merge(data_aktobe, melted_pressure, on='DateAndTime')
data_aktobe = pd.merge(data_aktobe, melted_visibility, on='DateAndTime')
data_aktobe = pd.merge(data_aktobe, melted_clouds, on='DateAndTime')
data_aktobe = pd.merge(data_aktobe, melted_humidity, on='DateAndTime')

data_aktobe['DateAndTime'] = pd.to_datetime(data_aktobe['DateAndTime'], format='%Y-%m-%d-%H')
data_aktobe = data_aktobe.sort_values(by='DateAndTime')
numeric_columns = data_aktobe.columns.difference(['DateAndTime'])
data_aktobe[numeric_columns] = data_aktobe[numeric_columns].apply(pd.to_numeric, errors='coerce')
data_aktobe['Clouds'] = data_aktobe['Clouds'].fillna(0)
data_aktobe['Visibility'] = data_aktobe['Visibility'].fillna(int(data_aktobe['Visibility'].mean()))
data_aktobe.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Aktobe.csv', index=False)