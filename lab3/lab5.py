import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Зчитуємо дані з Excel файлу
df = pd.read_excel('lab3.xlsx')
df = df.drop("№", axis=1)
X = df.drop("X4", axis=1)
y = df['X4']

# Розподіл вибірки на навчальну та тестову (80%/20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Нормалізуємо дані
scaler = MinMaxScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Модель RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(X_train_normalized, y_train)
rf_predictions = rf_model.predict(X_test_normalized)

# Метрики RandomForestClassifier
rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_precision = precision_score(y_test, rf_predictions, average='macro', zero_division=1)
rf_recall = recall_score(y_test, rf_predictions, average='macro', zero_division=1)
rf_f1 = f1_score(y_test, rf_predictions, average='macro', zero_division=1)

print("Випадковий ліс (Random Forest Classifier):")
print("Точність (Accuracy):", rf_accuracy)
print("Точність (Precision):", rf_precision)
print("Повнота (Recall):", rf_recall)
print("F1-показник (F1 Score):", rf_f1)

# Модель LogisticRegression
lr_model = LogisticRegression()
lr_model.fit(X_train_normalized, y_train)
lr_predictions = lr_model.predict(X_test_normalized)

# Метрики LogisticRegression
lr_accuracy = accuracy_score(y_test, lr_predictions)
lr_precision = precision_score(y_test, lr_predictions, average='macro', zero_division=1)
lr_recall = recall_score(y_test, lr_predictions, average='macro', zero_division=1)
lr_f1 = f1_score(y_test, lr_predictions, average='macro', zero_division=1)

print("\nЛогістична регресія (Logistic Regression):")
print("Точність (Accuracy):", lr_accuracy)
print("Точність (Precision):", lr_precision)
print("Повнота (Recall):", lr_recall)
print("F1-показник (F1 Score):", lr_f1)

# Модель Support Vector Machine
svm_model = SVC()
svm_model.fit(X_train_normalized, y_train)
svm_predictions = svm_model.predict(X_test_normalized)

# Метрики Support Vector Machine
svm_accuracy = accuracy_score(y_test, svm_predictions)
svm_precision = precision_score(y_test, svm_predictions, average='macro', zero_division=1)
svm_recall = recall_score(y_test, svm_predictions, average='macro', zero_division=1)
svm_f1 = f1_score(y_test, svm_predictions, average='macro', zero_division=1)

print("\nМетод опорних векторів (Support Vector Machine):")
print("Точність (Accuracy):", svm_accuracy)
print("Точність (Precision):", svm_precision)
print("Повнота (Recall):", svm_recall)
print("F1-показник (F1 Score):", svm_f1)
