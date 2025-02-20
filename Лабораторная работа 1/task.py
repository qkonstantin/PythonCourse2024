import doctest


class Backpack:
    """
    Класс для описания рюкзака.
    """

    def __init__(self, volume: float, weight_limit: float):
        """
        Создание и подготовка к работе объекта "Рюкзак".

        :param volume: Объем рюкзака в литрах.
        :param weight_limit: Максимально допустимый вес содержимого в килограммах.

        Примеры:
        >>> backpack = Backpack(40, 15)
        >>> backpack.volume
        40.0
        >>> backpack.weight_limit
        15.0
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем рюкзака должен быть числом.")
        if not isinstance(weight_limit, (int, float)):
            raise TypeError("Максимально допустимый вес должен быть числом.")
        if volume <= 0:
            raise ValueError("Объем рюкзака должен быть положительным.")
        if weight_limit <= 0:
            raise ValueError("Максимальный вес должен быть положительным.")

        self.volume = float(volume)
        self.weight_limit = float(weight_limit)
        self.current_volume = 0.0
        self.current_weight = 0.0
        self.items = {}  # Словарь для хранения предметов: {название: (объем, вес)}

    def add_item(self, name: str, item_volume: float, item_weight: float) -> None:
        """
        Добавление предмета в рюкзак.

        :param name: Название предмета.
        :param item_volume: Объем предмета.
        :param item_weight: Вес предмета.

        Примеры:
        >>> backpack = Backpack(40, 15)
        >>> backpack.add_item("Книга", 2, 1)
        >>> backpack.list_items()
        {'Книга': (2, 1)}
        >>> backpack.current_load()
        (2.0, 1.0)
        """
        if not isinstance(name, str):
            raise TypeError("Название предмета должно быть строкой.")
        if not isinstance(item_volume, (int, float)):
            raise TypeError("Объем предмета должен быть числом.")
        if not isinstance(item_weight, (int, float)):
            raise TypeError("Вес предмета должен быть числом.")
        if item_volume <= 0 or item_weight <= 0:
            raise ValueError("Объем и вес предмета должны быть положительными.")
        if self.current_volume + item_volume > self.volume:
            raise ValueError("Добавление предмета превышает объем рюкзака.")
        if self.current_weight + item_weight > self.weight_limit:
            raise ValueError("Добавление предмета превышает допустимый вес.")
        if name in self.items:
            raise ValueError(f"Предмет '{name}' уже находится в рюкзаке.")

        self.items[name] = (item_volume, item_weight)
        self.current_volume += item_volume
        self.current_weight += item_weight

    def remove_item(self, name: str) -> None:
        """
        Удаление предмета из рюкзака.

        :param name: Название предмета.

        Примеры:
        >>> backpack = Backpack(40, 15)
        >>> backpack.add_item("Книга", 2, 1)
        >>> backpack.remove_item("Книга")
        >>> backpack.list_items()
        {}
        >>> backpack.current_load()
        (0.0, 0.0)
        """
        if not isinstance(name, str):
            raise TypeError("Название предмета должно быть строкой.")
        if name not in self.items:
            raise ValueError(f"Предмет '{name}' отсутствует в рюкзаке.")

        item_volume, item_weight = self.items.pop(name)
        self.current_volume -= item_volume
        self.current_weight -= item_weight

    def current_load(self) -> tuple[float, float]:
        """
        Получение текущего загруженного объема и веса.

        :return: Кортеж из текущего объема и веса.

        Примеры:
        >>> backpack = Backpack(40, 15)
        >>> backpack.add_item("Бутылка воды", 1, 0.5)
        >>> backpack.current_load()
        (1.0, 0.5)
        """
        if not isinstance(self.current_volume, (int, float)):
            raise TypeError("Текущий объем должен быть числом.")
        if not isinstance(self.current_weight, (int, float)):
            raise TypeError("Текущий вес должен быть числом.")

        return self.current_volume, self.current_weight

    def list_items(self) -> dict:
        """
        Возвращает список всех предметов в рюкзаке с их объемом и весом.

        :return: Словарь предметов {название: (объем, вес)}.

        Примеры:
        >>> backpack = Backpack(40, 15)
        >>> backpack.add_item("Книга", 2, 1)
        >>> backpack.add_item("Бутылка воды", 1, 0.5)
        >>> backpack.list_items()
        {'Книга': (2, 1), 'Бутылка воды': (1, 0.5)}
        """
        if not isinstance(self.items, dict):
            raise TypeError("Список предметов должен быть словарем.")

        return self.items.copy()


class Intercom:
    """
    Класс для описания работы домофона.
    """

    def __init__(self, apartment_number: int, is_locked: bool = True):
        """
        Создание и подготовка к работе объекта "Домофон".

        :param apartment_number: Номер квартиры.
        :param is_locked: Состояние блокировки домофона (True - закрыт, False - открыт).

        Примеры:
        >>> intercom = Intercom(101)
        >>> intercom.apartment_number
        101
        >>> intercom.is_locked
        True
        """
        if not isinstance(apartment_number, int):
            raise TypeError("Номер квартиры должен быть целым числом.")
        if not isinstance(is_locked, bool):
            raise TypeError("Состояние двери (is_locked) должно быть логическим значением.")
        if apartment_number <= 0:
            raise ValueError("Номер квартиры должен быть положительным числом.")
        self.apartment_number = apartment_number
        self.is_locked = is_locked

    def unlock(self, code: str) -> bool:
        """
        Открытие домофона с использованием кода.

        :param code: Код для разблокировки.
        :return: True, если код верен и домофон разблокирован, иначе False.

        Примеры:
        >>> intercom = Intercom(101)
        >>> intercom.unlock('1234')
        True
        >>> intercom.is_intercom_locked()
        False
        """
        if not isinstance(code, str):
            raise TypeError("Код должен быть строкой.")
        valid_code = "1234"  # Предположим, код разблокировки установлен как "1234"
        if code == valid_code:
            self.is_locked = False
            return True
        return False

    def lock(self) -> None:
        """
        Закрытие домофона.

        Примеры:
        >>> intercom = Intercom(101)
        >>> intercom.unlock('1234')
        True
        >>> intercom.lock()
        >>> intercom.is_intercom_locked()
        True
        """
        self.is_locked = True

    def is_intercom_locked(self) -> bool:
        """
        Проверяет, закрыт ли домофон.

        :return: True, если домофон закрыт, иначе False.

        Примеры:
        >>> intercom = Intercom(101)
        >>> intercom.is_intercom_locked()
        True
        """
        if not isinstance(self.is_locked, bool):
            raise TypeError("Состояние блокировки (is_locked) должно быть логическим значением.")
        return self.is_locked


class Airplane:
    """
    Класс для описания самолета.
    """

    def __init__(self, max_speed: float, max_altitude: float, max_range: float):
        """
        Создание и подготовка к работе объекта "Самолет".

        :param max_speed: Максимальная скорость самолета в км/ч.
        :param max_altitude: Максимальная высота полета самолета в метрах.
        :param max_range: Максимальная дальность полета самолета в километрах.

        Примеры:
        >>> airplane = Airplane(900, 12000, 5000)
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть числом.")
        if not isinstance(max_altitude, (int, float)):
            raise TypeError("Максимальная высота должна быть числом.")
        if not isinstance(max_range, (int, float)):
            raise TypeError("Максимальная дальность должна быть числом.")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        if max_altitude <= 0:
            raise ValueError("Максимальная высота должна быть положительным числом.")
        if max_range <= 0:
            raise ValueError("Максимальная дальность полета должна быть положительным числом.")
        self.max_speed = float(max_speed)
        self.max_altitude = float(max_altitude)
        self.max_range = float(max_range)
        self.current_speed = 0.0
        self.current_altitude = 0.0
        self.current_distance = 0.0

    def set_speed(self, speed: float) -> None:
        """
        Устанавливает текущую скорость самолета.

        :param speed: Скорость самолета в км/ч.

        Примеры:
        >>> airplane = Airplane(900, 12000, 5000)
        >>> airplane.set_speed(800)
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом.")
        if speed < 0 or speed > self.max_speed:
            raise ValueError("Скорость должна быть в диапазоне от 0 до максимальной скорости.")
        self.current_speed = float(speed)

    def climb(self, altitude: float) -> None:
        """
        Устанавливает текущую высоту полета самолета.

        :param altitude: Высота в метрах.

        Примеры:
        >>> airplane = Airplane(900, 12000, 5000)
        >>> airplane.climb(10000)
        """
        if not isinstance(altitude, (int, float)):
            raise TypeError("Высота должна быть числом.")
        if altitude < 0 or altitude > self.max_altitude:
            raise ValueError("Высота должна быть в диапазоне от 0 до максимальной высоты.")
        self.current_altitude = float(altitude)

    def fly(self, distance: float) -> None:
        """
        Увеличивает текущую пройденную дистанцию самолета.

        :param distance: Дистанция полета в километрах.

        Примеры:
        >>> airplane = Airplane(900, 12000, 5000)
        >>> airplane.fly(1000)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Дистанция должна быть числом.")
        if distance < 0:
            raise ValueError("Дистанция должна быть положительным числом.")
        if self.current_distance + distance > self.max_range:
            raise ValueError("Превышение максимальной дальности полета.")
        self.current_distance += float(distance)

    def status(self) -> dict:
        """
        Возвращает текущий статус самолета: скорость, высоту и пройденную дистанцию.

        :return: Словарь с текущими параметрами самолета.

        Примеры:
        >>> airplane = Airplane(900, 12000, 5000)
        >>> airplane.set_speed(800)
        >>> airplane.climb(10000)
        >>> airplane.fly(1000)
        >>> airplane.status()
        {'speed': 800.0, 'altitude': 10000.0, 'distance': 1000.0}
        """
        if not isinstance(self.current_speed, (int, float)):
            raise TypeError("Текущая скорость должна быть числом.")
        if not isinstance(self.current_altitude, (int, float)):
            raise TypeError("Текущая высота должна быть числом.")
        if not isinstance(self.current_distance, (int, float)):
            raise TypeError("Текущая дистанция должна быть числом.")
        return {
            "speed": self.current_speed,
            "altitude": self.current_altitude,
            "distance": self.current_distance
        }


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров из документации.
