import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создание исходного DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Функция для перевода в one-hot-формат
def one_hot_encoding(row, categories):
    return [1 if row == category else 0 for category in categories]

# Уникальные категории в столбце
unique_categories = data['whoAmI'].unique()

# Применение one-hot encoding
one_hot_data = data['whoAmI'].apply(lambda row: one_hot_encoding(row, unique_categories))

# Преобразование в DataFrame и добавление правильных столбцов
one_hot_df = pd.DataFrame(list(one_hot_data), columns=unique_categories)

print(one_hot_df.head(11))
