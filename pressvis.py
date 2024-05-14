import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv')
df['Month'] = pd.to_datetime(df['Month'])
plt.figure(figsize=(12, 8))
sns.lineplot(x='Month', y='BarometricPressure', hue='City', data=df, palette='Set2', marker='o')
plt.title('Barometric Pressure Comparison')
plt.xlabel('Dates', fontsize=14)
plt.ylabel('Barometric Pressure')
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.legend(title='City', title_fontsize='14', fontsize='12', loc='upper left')
plt.show()