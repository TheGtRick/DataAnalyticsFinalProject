import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv')
plt.figure(figsize=(12, 8))
sns.violinplot(x='City', y='Humidity', data=df, inner='quartile', linewidth=2)
sns.swarmplot(x='City', y='Humidity', data=df, color='black', size=5, alpha=0.7)
plt.title('Humidity Distribution by City')
plt.xlabel('City')
plt.ylabel('Humidity (%)')
plt.show()