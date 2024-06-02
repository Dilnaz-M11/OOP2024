class GameSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.volume = 50  # Начальное значение громкости
            cls._instance.difficulty = "Normal"  # Начальный уровень сложности
        return cls._instance

# Пример использования
settings1 = GameSettings()
settings2 = GameSettings()

# Проверяем, что это один и тот же объект
print(settings1 is settings2)  # Выведет True

# Меняем настройки в одном объекте
settings1.volume = 70
settings1.difficulty = "Hard"

# Проверяем, что настройки изменились в обоих объектах
print(settings2.volume)  # Выведет 70
print(settings2.difficulty)  # Выведет "Hard"
