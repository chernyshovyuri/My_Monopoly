from abc import ABC, abstractmethod
from businesman import Businessman

class Cell(ABC):

    _x: int

    def __init__(self, x: int):

        if not isinstance(x, int): raise TypeError()

        self._x = x

    @abstractmethod
    def land(self, businessman: Businessman): raise NotImplemented()

class ChanceResultTypes:

    POSITIVE = 1
    NEGATIVE = -1


class Chance(Cell):

    CASH = 30

    def __init__(self, x: int):

        super().__init__(x)

    def land(self, businessman: Businessman):
        self.__try_luck(businessman)

    def __try_luck(self, businessman: Businessman):  # испытать удачу

        result = self.__solve_chance()

        if result == ChanceResultTypes.POSITIVE:
            self.__execute_positive_chance(businessman)
        else:
            self.__execute_negative_chance(businessman)

    def __execute_positive_chance(self, businessman):  # выполнить позитивный исход
        businessman.increase_balance(Chance.CASH)

    def __execute_negative_chance(self, businessman):  # выполнить негативный исход
        businessman.decrease_balance(Chance.CASH)

    def __solve_chance(self) -> int:  # вычислить шанс
        import random

        if random.randint(0, 10) > 5:
            return ChanceResultTypes.POSITIVE
        else:
            return ChanceResultTypes.NEGATIVE


class Ownership(Cell, ABC):
    # Модель Собственности

    _owner: Businessman
    _price: float

    def __init__(self, x: int, price: int, rent: int):
        super().__init__(x)

        if not isinstance(price, int):  raise  TypeError()
        if not isinstance(rent, int):  raise TypeError()

        self._owner = None
        self._price = price
        self._rent = rent

    @abstractmethod
    def calculate_price(self) -> int:  raise NotImplemented()

    @abstractmethod
    def calculate_rent(self) -> int:  raise NotImplemented()

    def get_price(self) -> int:
        return self._price


    def set_owner(self, owner: Businessman) -> bool:
        if not isinstance(owner, Businessman): raise TypeError()

        if not owner:  return False

        self._owner = owner

        return True


    def has_owner(self) -> Businessman | None:
        return  self._owner


    def identify_owner(self, owner: Businessman) -> bool:
        if not isinstance(owner, Businessman): raise TypeError()

        return self._owner == owner


    def unset_owner(self) -> None:
        self._owner = None


class NeighborhoodTypes:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PINK = 4
    BROWN = 5
    LIGHT_BLUE = 6


class Street(Ownership):

    def __init__(self, x: int, price: int, rent: int, neighborhood: NeighborhoodTypes, ):
        super().__init__(x, price, rent)

        self.__neighborhood =  neighborhood


    def land(self, businessman: Businessman) -> None:
        if not isinstance(businessman, Businessman): raise TypeError()

        self._x = businessman

    def calculate_price(self) -> int:
        pass

    def calculate_rent(self) -> int:
        pass

    def build_home(self) -> None:  # построить дом


        



    def build_hotel(self) -> None:  # построить отель
        pass

    def can_build_hotel(self) -> bool: # можно ли построить отель
        pass

class BuildingRatioTypes:
    HOME = 2
    HOTEL = 9

class Building:  # строение

    def __init__(self, price: int, ratio: int):
        if not isinstance(price, int):  raise TypeError()
        if not isinstance(ratio, int):  raise TypeError()

        self.__price = price
        self.__ratio = ratio

    def get_price(self):
        return self.__price

    def get_ratio(self):
        return self.__ratio

    def get_full_price(self):
        return self.__price * self.__ratio



