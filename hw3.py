import matplotlib.pyplot as plt
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width",
                "petal_length", "petal_width", "class"]

iris_df = pd.read_csv(url, header=None, names=column_names)
print(iris_df.head())  # перші 5 рядків
print(iris_df.describe())  # описова статистика
print(iris_df.info())  # виводимо типи даних та к-сть  не нульових значень

# знаходимо середнє значення стовпця sepal_length
average_sepal_length = iris_df.groupby('class')['sepal_length'].mean()
print("Середня довжина чашолистика для кожного виду ірису:\n", average_sepal_length)

# знаходимо максимальну ширину для виду "setosa"
max_width_setosa = iris_df[iris_df['class'] == 'Iris-setosa']['petal_width'].max()
print("Максимальна ширина листка для виду “setosa”:", max_width_setosa)

# Новий df для виду versicolor
versicolor_df = iris_df[iris_df['class'] == 'Iris-versicolor']
print(versicolor_df.head())

# Відбір даних з довжиною більше 5
filtered_df = iris_df[iris_df['petal_length'] > 5.0]
print(filtered_df.head())

# середня довжина для кожного виду
average_petal_width = iris_df.groupby('class')['petal_width'].mean()
print("Середня ширина листка для кожного виду ірису:\n", average_petal_width)
# мінімальна довжина листка
min_sepal_length = iris_df.groupby('class')['sepal_length'].min()
print("Мінімальна довжина чашолистика для кожного виду ірису:\n", min_sepal_length)
# к-сть ірисів більше за середню довжину
average_petal_length_all = iris_df['petal_length'].mean()
count_above_average = iris_df[iris_df['petal_length'] > average_petal_length_all].groupby('class').size()
print("Кількість ірисів кожного виду з довжиною листка більше за середню довжину всіх ірисів:\n", count_above_average)

# Розподіл довжини листка (petal length) для всіх ірисів
plt.hist(iris_df['petal_length'], bins=20, edgecolor='black')
plt.title('Розподіл довжини листка (petal length)')
plt.xlabel('Довжина листка')
plt.ylabel('Частота')
plt.show()
