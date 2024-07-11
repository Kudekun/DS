# 1
import numpy as np
import pandas as pd

# Завантажую свою xlsx в проект
file_path1 = 'дз1.xlsx'
# Зчитую її
df1 = pd.read_excel(file_path1, sheet_name=0, header=None)
df2 = pd.read_excel(file_path1, sheet_name=1, header=None)

array1 = df1.to_numpy()
array2 = df2.to_numpy()

sum_array1 = np.sum(array1)
sum_array2 = np.sum(array2)
difference_arrays = array1 - array2
product_arrays = array1 * array2
power_arrays = np.power(array1, array2)

print("\nЗавдання 1")
print("Масив1:\n", array1)
print("Масив2:\n", array2)
print("Сума елементів масиву 1:", sum_array1)
print("Сума елементів масиву 2:", sum_array2)
print("Різниця між елементами масиву:\n", difference_arrays)
print("Перемноження 2-х масивів:\n", product_arrays)
print("Підняття в степінь масивів\n", power_arrays)

# 2
# Завантажую свою xlsx в проект
file_path2 = 'дз2.xlsx'
# Зчитую її
chess_board = pd.read_excel(file_path2, sheet_name=0, header=None)

third_row = chess_board.iloc[2].to_numpy()
fifth_column = chess_board.iloc[:, 4].to_numpy()
left_side = chess_board.iloc[:3, :3].to_numpy()

print("\nЗавдання 2")
print("Третій рядок:", third_row)
print("П'ятий стовпець:", fifth_column)
print("3×3 в лівому верхньому куті:", left_side)
# Зробив вивід колоно і стовпців методом індексів, якщо так не підходить то напишіть, спробую переробити

# 3
from PIL import Image
import numpy as np

# Завантажую зображення
image_path = "example.jpg"
image = Image.open(image_path)

# Перетворюємо зображення в NumPy-масив
image_array = np.array(image)

# Виводимо інформацію про розмір та тип даних
print("\nЗавдання 3")
print("Розмір зображення:", image_array.shape)
print("Тип даних:", image_array.dtype)

# Розбиваємо зображення на окремі канали (R, G, B)
red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

# Статистичний аналіз
print("\nСереднє значення каналу R:", np.mean(red_channel))
print("Мінімальне значення каналу R:", np.min(red_channel))
print("Максимальне значення каналу R:", np.max(red_channel))

print("Середнє значення каналу G:", np.mean(green_channel))
print("Мінімальне значення каналу G:", np.min(green_channel))
print("Максимальне значення каналу G:", np.max(green_channel))

print("Середнє значення каналу B:", np.mean(blue_channel))
print("Мінімальне значення каналу B:", np.min(blue_channel))
print("Максимальне значення каналу B:", np.max(blue_channel))

# Загальна сума інтенсивності пікселів
total_intensity = np.sum(image_array)
print("\nЗагальна сума інтенсивності пікселів:", total_intensity)

# Нормалізація зображення
max_value = np.max(image_array)
normalized_image = image_array / max_value

# Виводимо перші 5 пікселів після нормалізації
print("Перші 5 пікселів після нормалізації:\n", normalized_image[:5])

# можливо в 3 завданні були помилки, бо не розбирали PIL на уроці
