import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

file_path = 'lab2.xlsx'
df = pd.read_excel(file_path)

# Виведення перших 5 рядків даних (стовпців з 1 по 5)
print(df.iloc[:, 1:6].to_string(index=False))

data_to_normalize = df.iloc[:, 1:6]

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_to_normalize)

normalized_df = pd.DataFrame(normalized_data, columns=df.columns[1:6])

# Виведення нормалізованих даних
print(normalized_df.to_string(index=False))

plt.figure(figsize=(15, 10))

# Побудова діаграм для кожної комбінації змінних

# Діаграма 1: Змінна 1 проти Змінної 2
plt.subplot(4, 3, 1)
plt.scatter(normalized_df.iloc[:, 0], normalized_df.iloc[:, 1])
plt.xlabel('Змінна 1')
plt.ylabel('Змінна 2')
plt.title('Змінна 1 vs Змінна 2')

# Діаграма 2: Змінна 1 проти Змінної 3
plt.subplot(4, 3, 2)
plt.scatter(normalized_df.iloc[:, 0], normalized_df.iloc[:, 2])
plt.xlabel('Змінна 1')
plt.ylabel('Змінна 3')
plt.title('Змінна 1 vs Змінна 3')

# Діаграма 3: Змінна 1 проти Змінної 4
plt.subplot(4, 3, 3)
plt.scatter(normalized_df.iloc[:, 0], normalized_df.iloc[:, 3])
plt.xlabel('Змінна 1')
plt.ylabel('Змінна 4')
plt.title('Змінна 1 vs Змінна 4')

# Діаграма 4: Змінна 1 проти Змінної 5
plt.subplot(4, 3, 4)
plt.scatter(normalized_df.iloc[:, 0], normalized_df.iloc[:, 4])
plt.xlabel('Змінна 1')
plt.ylabel('Змінна 5')
plt.title('Змінна 1 vs Змінна 5')

# Діаграма 5: Змінна 2 проти Змінної 3
plt.subplot(4, 3, 5)
plt.scatter(normalized_df.iloc[:, 1], normalized_df.iloc[:, 2])
plt.xlabel('Змінна 2')
plt.ylabel('Змінна 3')
plt.title('Змінна 2 vs Змінна 3')

# Діаграма 6: Змінна 2 проти Змінної 4
plt.subplot(4, 3, 6)
plt.scatter(normalized_df.iloc[:, 1], normalized_df.iloc[:, 3])
plt.xlabel('Змінна 2')
plt.ylabel('Змінна 4')
plt.title('Змінна 2 vs Змінна 4')

# Діаграма 7: Змінна 2 проти Змінної 5
plt.subplot(4, 3, 7)
plt.scatter(normalized_df.iloc[:, 1], normalized_df.iloc[:, 4])
plt.xlabel('Змінна 2')
plt.ylabel('Змінна 5')
plt.title('Змінна 2 vs Змінна 5')

# Діаграма 8: Змінна 3 проти Змінної 4
plt.subplot(4, 3, 8)
plt.scatter(normalized_df.iloc[:, 2], normalized_df.iloc[:, 3])
plt.xlabel('Змінна 3')
plt.ylabel('Змінна 4')
plt.title('Змінна 3 vs Змінна 4')

# Діаграма 9: Змінна 3 проти Змінної 5
plt.subplot(4, 3, 9)
plt.scatter(normalized_df.iloc[:, 2], normalized_df.iloc[:, 4])
plt.xlabel('Змінна 3')
plt.ylabel('Змінна 5')
plt.title('Змінна 3 vs Змінна 5')

# Діаграма 9: Змінна 4 проти Змінної 5
plt.subplot(4, 3, 10)
plt.scatter(normalized_df.iloc[:, 3], normalized_df.iloc[:, 4])
plt.xlabel('Змінна 4')
plt.ylabel('Змінна 5')
plt.title('Змінна 4 vs Змінна 5')

plt.tight_layout()
plt.show()
