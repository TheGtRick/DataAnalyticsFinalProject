import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv')
plt.figure(figsize=(10, 6))
sns.boxplot(x='City', y='WindSpeed', data=df, palette='Set2')
plt.title('Wind Speed Comparison')
plt.xlabel('City')
plt.ylabel('Wind Speed (m/s)')
plt.show()