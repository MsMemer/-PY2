# TODO Написать 3 класса с документацией и аннотацией типов
class Smuzy:
    def __init__(self, flavor: str, taste: str, color: str, mass: int):
        """
        Создание и подготовка к работе объекта "Смузи"
        :param flavor: Состав смузи
        :param taste: Вкус смузи
        :param color: Цвет смузи
        :param mass: Масса нетто

        Примеры:
        >>> smuzy = Smuzy("berries", "sweet", "purple", 150)
        """
        if not isinstance(flavor, (str)):
            raise TypeError("Состав смузи должен быть типа str")
        self.flavor = flavor

        if not isinstance(taste, (str)):
            raise TypeError("Вкус смузи должен быть типа str")
        self.taste = taste

        if not isinstance(color, (str)):
            raise TypeError("Цвет смузи должен быть типа str")
        self.color = color

        if not isinstance(mass, (int)):
            raise TypeError("Масса нетто должна быть типа int или float")
        if mass < 0:
            raise ValueError("Масса нетто должна быть неотрицательным числом")
        self.mass = mass

    def is_empty_smuzy(self) -> bool:
        """
        Функция которая проверяет закончилось ли смузи
        :return: Есть ли еще смузи
        Примеры:
        >>> smuzy = Smuzy("berries", "sweet", "purple", 0)
        >>> smuzy.is_empty_smuzy()
        """
        ...

    def add_straw_to_smuzy(self, straw: float) -> None:
        """
        Добавление трубочки в смузи.
        :param straw: Объем трубочки
        :raise ValueError: Если объем трубочки превышает свободное место в смузи, то вызываем ошибку
        Примеры:
        >>> smuzy = Smuzy("berries", "sweet", "purple", 0)
        >>> smuzy.add_straw_to_smuzy(10)
        """
        if not isinstance(straw, (int, float)):
            raise TypeError("Объем трубочки должен быть типа int или float")
        if straw < 0:
            raise ValueError("Объем добавляемой трубочки должен быть положительным числом")
        ...


if __name__ == "__main__":
   import doctest
   doctest.testmod()



