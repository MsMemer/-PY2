import doctest


class Scooter:
    """
    Создание и подготовка к работе объекта "Самокат"
    :param brand_name: название бренда
    :param model: название модели
    :param construction: конструкция
    :param charging: возможность подзарядки.
    True - можно заряжать.
    False - не заряжается
    :paran depreciation: наличие амортизации.
    True - амортизация присутствует,
    False - амортизация отсутствует
    Атрибуты brand_name, model, construction, charging, depreciation
    являются неизменными. Открыты только для чтения
    Примеры:
    >>> scooter = Scooter(brand_name='Whoosh', model='Whoosh 01', \
        construction='Электрический', charging=True, depreciation=True)
    """

    def __init__(self, brand_name: str, model: str, construction: str,
                 charging: bool, depreciation: bool):
        if not isinstance(brand_name, str):
            raise TypeError("атрибут brand_name должен быть типа str")
        self._brand_name = brand_name
        if not isinstance(model, str):
            raise TypeError("атрибут model должен быть типа str")
        self._model = model
        if not isinstance(construction, str):
            raise TypeError("атрибут construction должен быть типа str")
        self._construction = construction
        if not isinstance(charging, bool):
            raise TypeError("атрибут charging должен быть типа bool")
        self._charging = charging
        if not isinstance(depreciation, bool):
            raise TypeError("атрибут depreciation должен быть типа bool")
        self._depreciation = depreciation

    @property
    def brand_name(self):
        return self._brand_name

    @property
    def model(self):
        return self._model

    @property
    def construction(self):
        return self._construction

    @property
    def charging(self):
        return self._charging

    @property
    def depreciation(self):
        return self._depreciation

    @property
    def presence_charging(self) -> bool:
        """
        Свойство, которое проверяет наличие возможности подзарядки в самокате
        :return: True - возможность подзарядки присутсвует, False - возможность подзарядки отсутствует
        """
        if self.charging is True:
            return True
        else:
            return False

    @property
    def presence_depreciation(self) -> bool:
        """
        Свойство, которое проверяет наличие амортизации в самокате
        :return: True - амортизация присутствует, False - амортизация отсутствует
        """
        if self.depreciation is True:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Самокат {self.brand_name} {self.model}'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(brand_name={self.brand_name!r}, '
                f'model={self.model!r}, construction={self.construction!r}, '
                f'charging={self.charging!r}, '
                f'depreciation={self.depreciation!r})')

    def connection_gadjet(self) -> None:
        """
        Функция, которая соединяет самокат с устройством.
        В классе "Scooter" методу "connection_gadjet" не нужно
        знать, каким имено образом происходит соединение.
        Примеры:
        >>> scooter = Scooter(brand_name='Whoosh', model='Whoosh 01', \
        construction='Электрический', charging=True, depreciation=True)
        >>> scooter.connection_gadjet()
        """
        ...

    def switch_depreciation(self, mode: int) -> None:
        """
        Функция, которая позволяет активировать функцию амортизации и выбрать один из уровней амортизации,
        при условии, что самокат поддерживает функцию амортизации
        :param mode: 0 - амортизация выключена. 1 - минимальная амортизация.
        2 - средняя амортизация. 3 - максимальная амортизация.
        Примеры:
        >>> scooter = Scooter(brand_name='Whoosh', model='Whoosh 01', \
        construction='Электрический', charging=True, depreciation=True)
        >>> scooter.switch_depreciation(mode=1)
        """


class Electroscooter(Scooter):
    """
    Создание и подготовка к работе объекта "Электросамокат"
    :param brand_name: название бренда
    :param model: название модели
    :param construction: конструкция
    :param charging: наличие возможности подзарядки.
    True - возможность подзарядки присутствует.
    False - возможность подзарядки отсутствует
    :paran depreciation: наличие амортизации.
    True - амортизация присутствует,
    False - амортизация отсутствует
    :param charging_place: место подзарядки
    :param charging_time: время подзарядки
    Атрибуты brand_name, model, construction, charging, depreciation,
   charging_place, charging_time являются неизменными.
    Открыты только для чтения
    Примеры:
    >>> electroscooter = Electroscooter(brand_name='Whoosh', model='Whoosh 01', \
        construction='Электрический', charging=True, depreciation=False, \
       charging_place='Розетка 220V', charging_time=100)
    """

    def __init__(self, brand_name: str, model: str, construction: str,
                charging: bool, depreciation: bool,
                 charging_place: str, charging_time: int):
        super().__init__(brand_name, model, construction, charging,
                         depreciation)
        if not isinstance(charging_place, str):
            raise TypeError("Атрибут charging_place должен быть типа str")
        self._charging_place = charging_place
        if not isinstance(charging_time, int):
            raise TypeError("Атрибут charging_time должен быть типа int")
        if charging_time <= 0:
            raise ValueError("Атрибут charging_time должен быть больше нуля")
        self._charging_time = charging_time

    @property
    def charging_place(self):
        return self._charging_place

    @property
    def charging_time(self):
        return self._charging_time


    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(brand_name={self.brand_name!r}, '
                f'model={self.model!r}, construction={self.construction!r}, '
                f'charging={self.charging!r}, '
                f'depreciation={self.depreciation!r}, '
                f'charging_place={self.charging_place!r}, '
                f'charging_time={self.charging_time!r}, )')

    def connection_gadjet(self) -> None:
        """
        Функция, которая соединяет самокат с другим устройством.
        Данный метод перегружается в дочернем классе "Electroscooter",
        так как необходимо учесть атрибут экземпляра класса "connection_type"
        Примеры:
        >>> electroscooter = Electroscooter(brand_name='Whoosh', model='Whoosh 01', \
        construction='Жлектрический', charging=True, depreciation=False, \
        charging_place='Розетка 220V', charging_time=100)
        >>> electroscooter.connection_gadjet()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()