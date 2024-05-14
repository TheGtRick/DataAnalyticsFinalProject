import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_test = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-testR.csv')
df_predicted = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Final Project\\Y-predR.csv')
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_test['Temperature'], y=df_predicted['Temperature'], data=pd.concat([df_test, df_predicted], keys=['Test', 'Predicted']))
plt.xlabel('Test Temperature')
plt.ylabel('Predicted Temperature')
plt.title('Test vs Predicted Temperature Scatter Plot')
plt.show()