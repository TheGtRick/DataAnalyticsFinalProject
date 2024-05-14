import pandas as pd
# Final concat
almaty = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Almaty.csv')
aktobe = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Aktobe.csv')
almaty['City'] = 0
aktobe['City'] = 1
meteodata = pd.concat([almaty, aktobe], ignore_index=True)
meteodata = meteodata.sort_values(by='DateAndTime')
meteodata.to_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\MeteoData.csv', index=False)