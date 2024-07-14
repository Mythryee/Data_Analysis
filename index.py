import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/student.csv')
print("Number of rows and columns:", df.shape)
print(df.dtypes)
print(df.head())
print(df.describe())
print(df.isnull().sum())


plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(3, 2, 2)
plt.hist(df['StudyTimeWeekly'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Study Time Weekly')
plt.xlabel('Study Time (hours)')
plt.ylabel('Frequency')

plt.subplot(3, 2, 3)
plt.hist(df['Absences'], bins=20, color='salmon', edgecolor='black')
plt.title('Distribution of Absences')
plt.xlabel('Number of Absences')
plt.ylabel('Frequency')

plt.subplot(3, 2, 4)
plt.hist(df['GPA'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of GPA')
plt.xlabel('GPA')
plt.ylabel('Frequency')

plt.subplot(3, 2, 5)
plt.hist(df['GradeClass'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Grade Class')
plt.xlabel('Grade Class')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


