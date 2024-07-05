import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

# Зчитуємо дані з Excel файлу
df = pd.read_excel('lab3.xlsx')

# Відокремлюємо ознаки та цільову змінну
df = df.drop("№", axis=1)
X = df.drop("X4", axis=1)
y = df['X4']

# Розподіл вибірки на навчальну та тестову (80%/20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Нормалізуємо дані
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Навчаємо модель Random Forest Classifier з максимальною глибиною дерева 1
model = RandomForestClassifier(max_depth=1)
model.fit(X_train_normalized, y_train)

# Передбачення для тестової вибірки
predictions = model.predict(X_test_normalized)

# Оцінка якості моделі
accuracy = accuracy_score(y_test, predictions)

# Виведення результатів
print("Передбачення:", predictions)
print("Вірність моделі:", accuracy)

# Підготовка нових даних для передбачення
new_data = {
    'X1': [1000],
    'X2': [32],
    'X3': [1],
    'X5': [1],
    'X6': [1]
}

# Створюємо DataFrame з новими даними
new_data_df = pd.DataFrame(new_data)
new_data_normalized = scaler.transform(new_data_df)
new_predictions = model.predict(new_data_normalized)

print("Передбачення для нових даних:", new_predictions)
