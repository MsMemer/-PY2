# TODO Написать 3 класса с документацией и аннотацией типов
class Bag:
    def __init__(self, type: str, color: str, capacity: int, occupied_capacity: int, weight: int):
        """
        Создание и подготовка к работе объекта "Сумка"
        :param type: Тип сумки
        :param color: Цвет сумки
        :param capacity: Вместимость сумки
        :param occupied_capacity: Сколько места занято в сумке
        :param weight: Вес сумки

        Примеры:
        >>> bag = Bag("shoulderbag", "multicolor", 100, 0, 200)
        """
        if not isinstance(type, (str)):
            raise TypeError("Тип сумки должен быть типа str")
        self.type = type

        if not isinstance(color, (str)):
            raise TypeError("Цвет сумки должен быть типа str")
        self.color = color

        if not isinstance(capacity, (int)):
            raise TypeError("Вместимость сумки должна быть типа int")
        if capacity < 0:
            raise ValueError("Вместимость сумки должна быть положительным числом")
        self.capacity = capacity

    def is_empty_bag(self) -> bool:
        """
        Функция которая проверяет является ли сумка пустой
        :return: Является ли сумка пустой
        Примеры:
        >>> bag = Bag("shoulderbag", "multicolor", 100, 0, 200)
        >>> bag.is_empty_bag()
        """
        ...

    def add_stuff_to_bag(self, stuff: float) -> None:
        """
        Добавление вещей в сумку.
        :param stuff: Объем добавляемых вещей
        :raise ValueError: Если количество добавляемых вещей превышает свободное место в сумке, то вызываем ошибку
        Примеры:
        >>> bag = Bag("shoulderbag", "multicolor", 100, 0, 200)
        >>> bag.add_stuff_to_bag(100)
        """
        if not isinstance(stuff, (int, float)):
            raise TypeError("Добавляемые вещи должны быть типа int или float")
        if stuff < 0:
            raise ValueError("Добавляемые вещи должны быть положительным числом")
        ...

    def remove_stuff_from_bag(self, estimate_stuff: float) -> None:
        """
        Извлечение вещей из сумки.
        :param estimate_stuff: Объем убранных вещей
        :raise ValueError: Если количество убранных вещей превышает количество вещей в сумке,
        то возвращается ошибка.
        :return: Объем реально убранных вещей
        Примеры:
        >>> bag = Bag("shoulderbag", "multicolor", 100, 100, 200)
        >>> bag.remove_stuff_from_bag(50)
        """
        ...

if __name__ == "__main__":
   import doctest
   doctest.testmod()



