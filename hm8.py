import sqlite3

# Создание подключения к базе данных (если базы данных не существует, она будет создана)
conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

# Создание таблицы countries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

# Создание таблицы cities
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

# Создание таблицы students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

# Добавление записей в таблицы countries и cities
cursor.executemany('INSERT INTO countries (title) VALUES (?)', [('Россия',), ('США',), ('Китай',), ('Великобритания',), ('Япония',), ('Франция',), ('Германия',)])

cursor.executemany('INSERT INTO cities (title, country_id) VALUES (?, ?)', [
    ('Москва', 1),
    ('Нью-Йорк', 2),
    ('Пекин', 3),
    ('Лондон', 4),
    ('Токио', 5),
    ('Париж', 6),
    ('Берлин', 7)
])

# Добавление учеников в разные города
cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', [
    ('Джастин', 'Бибер', 1),
    ('Кукушкин', 'Дмитрий', 2),
    ('Кирилл', 'Сарычев', 3),
    ('Саша', 'Козлова', 4),
    ('Якудза', 'Шер', 5),
    ('МАК', 'Трахер', 6),
    ('Пушки', 'Мустерманн', 7),
    ('Гэйб', 'Гобен', 1),
    ('Джон', 'Смит', 2),
    ('Людмила', 'Петрова', 3),
    ('Кёко', 'Сато', 5),
    ('Пьер', 'Лефевр', 6),
    ('Александр', 'Шульц', 7),
    ('Эмили', 'Джонсон', 2),
    ('Артем', 'Игнатьев', 1),
])

# Сохранение изменений и закрытие соединения
conn.committ()
conn.close()
