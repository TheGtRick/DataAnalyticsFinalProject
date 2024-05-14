import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\CompressedData.csv')
plt.figure(figsize=(12, 8))
sns.boxplot(x='City', y='Clouds', data=df, palette='Set2')
plt.title('Cloud Cover Comparison across Cities')
plt.xlabel('City')
plt.ylabel('Cloud Cover (%)')
plt.show()