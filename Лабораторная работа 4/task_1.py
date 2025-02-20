class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int, species: str):
        """
        Инициализация базового класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый животным.

        :return: Строка с описанием звука.
        """
        return "Some generic animal sound"

    def eat(self) -> str:
        """
        Возвращает описание действия поедания пищи.
        
        Этот метод оставлен без перегрузки в дочерних классах,
        чтобы продемонстрировать наследование функционала из базового класса.
        
        :return: Строка с описанием еды.
        """
        return f"{self.name} is eating."

    def __str__(self) -> str:
        return f"{self.species} named {self.name}, age {self.age}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self.age!r}, species={self.species!r})"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age, species="Dog")
        self.breed = breed

    def make_sound(self) -> str:
        """
        Перегруженный метод, возвращающий лай собаки.
        
        Перегрузка необходима, чтобы возвращать специфичный звук для собаки,
        а не общий звук из базового класса.
        
        :return: Строка с описанием лая.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод, описывающий, как собака приносит предмет.

        :param item: Предмет, который приносит собака.
        :return: Строка с описанием действия.
        """
        return f"{self.name} is fetching the {item}."

    def __str__(self) -> str:
        return f"{self.breed} dog named {self.name}, age {self.age}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, age={self.age!r}, breed={self.breed!r})"


class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация класса Cat.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age, species="Cat")
        self.color = color

    def make_sound(self) -> str:
        """
        Перегруженный метод, возвращающий мяуканье кошки.
        
        Перегрузка позволяет задать специфичный звук для кошки,
        отличающийся от общего звука базового класса.
        
        :return: Строка с описанием мяуканья.
        """
        return "Meow!"

    def scratch(self) -> str:
        """
        Метод, описывающий, как кошка царапается.

        :return: Строка с описанием действия.
        """
        return f"{self.name} is scratching the furniture."

    def __str__(self) -> str:
        return f"{self.color} cat named {self.name}, age {self.age}"

    def __repr__(self) -> str:
        return f"Cat(name={self.name!r}, age={self.age!r}, color={self.color!r})"


if __name__ == "__main__":
    # Пример использования классов
    dog = Dog("Buddy", 3, "Golden Retriever")
    cat = Cat("Whiskers", 5, "Black")

    print(dog)  # Вывод: Golden Retriever dog named Buddy, age 3
    print(cat)  # Вывод: Black cat named Whiskers, age 5

    print(dog.make_sound())  # Вывод: Woof!
    print(cat.make_sound())  # Вывод: Meow!

    print(dog.fetch("ball"))  # Вывод: Buddy is fetching the ball.
    print(cat.scratch())  # Вывод: Whiskers is scratching the furniture.
    
    # Демонстрация наследования метода eat из базового класса Animal
    print(dog.eat())  # Вывод: Buddy is eating.
    print(cat.eat())  # Вывод: Whiskers is eating.
