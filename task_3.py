# TODO Написать 3 класса с документацией и аннотацией типов
class Toothpaste:
    def __init__(self, brand: str, taste: str, mass: int):
        """
        Создание и подготовка к работе объекта "Сумка"
        :param brand: Марка зубной пасты
        :param taste: Вкус зубной пасты
        :param mass: Вес зубной пасты

        Примеры:
        >>> toothpaste = Toothpaste("Biomed", "tutti-frutti", 75)
        """
        if not isinstance(brand, (str)):
            raise TypeError("Бренд зубной пасты должен быть типа str")
        self.brand = brand

        if not isinstance(taste, (str)):
            raise TypeError("Вкус зубной пасты должен быть типа str")
        self.taste = taste

        if not isinstance(mass, (int)):
            raise TypeError("Масса зубной пасты должна быть типа int")
        if mass < 0:
            raise ValueError("Масса зубной пасты должна быть положительным числом")
        self.mass = mass

    def is_empty_toothpaste(self) -> bool:
        """
        Функция которая проверяет является ли сумка пустой
        :return: Является ли сумка пустой
        Примеры:
        >>> toothpaste = Toothpaste("Biomed", "tutti-frutti", 75)
        >>> toothpaste.is_empty_toothpaste()
        """
        ...

    def put_toothpaste_on_brush(self, brush: str) -> None:
        """
        Добавление зубной пасты на зубную щетку.
        :param brush: Бренд зубной щетки
        :raise TypeError: Если марка зубной щетки не совпадает с маркой зубной пасты, то вызываем ошибку
        Примеры:
        >>> toothpaste = Toothpaste("Biomed", "tutti-frutti", 75)
        >>> toothpaste.put_toothpaste_on_brush("Biomed")
        """
        if not isinstance(brush, (str)):
            raise TypeError("Добавляемые вещи должны быть типа str")
        ...


if __name__ == "__main__":
   import doctest
   doctest.testmod()



