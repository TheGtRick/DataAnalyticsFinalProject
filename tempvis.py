import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv')
df['Month'] = pd.to_datetime(df['Month'])
plt.figure(figsize=(12, 8))
sns.lineplot(x='Month', y='Temperature', hue='City', style='City', markers=True, dashes=False, data=df)
plt.title('Temperature Comparison by City')
plt.xlabel('Dates')
plt.ylabel('Temperature (°C)')
plt.show()
