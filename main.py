import pandas as pd

# Загрузка данных из файла с указанием кодировки
df = pd.read_csv('fifa_s2.csv', encoding='utf-8')
#Был проведен первоначальный анализ для выявления неполных данных. Было обнаружено, что в следующих столбцах отсутствуют значения:
#Nationality,Club,Value,International Reputation,Skill Moves,Position,Contract Valid Until,Release Clause

# Поиск и удаление неполных данных
df.dropna(inplace=True)
# Столбцы с пропущенными значениями были удалены из фрейма данных, за исключением столбца "Club".
# Пропущенные значения в столбце "Club" были заполнены "unknown".
# Поиск и удаление полных дубликатов
df.drop_duplicates(inplace=True)
# Функция для разбиения возраста по группам
def age_group(age):
    if age < 20:
        return 'до 20'
    elif age >= 20 and age < 30:
        return 'от 20 до 30'
    elif age >= 30 and age < 36:
        return 'от 30 до 36'
    else:
        return 'старше 36'
# Добавление колонки с разбиением возраста по группам
df['age_group'] = df['Age'].apply(age_group)
# Подсчет количества футболистов в каждой категории возраста
count_by_age_group = df['age_group'].value_counts()
# Вывод результатов
print(count_by_age_group)
