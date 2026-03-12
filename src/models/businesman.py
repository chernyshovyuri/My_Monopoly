from src.models.gameboard import Ownership


class Businessman:

    def __init__(self, balance):

        self.__balance = balance
        self.__ownerships = []

    def get_balance(self) -> int:
        return self.__balance

    def add_ownership(self, ownership: Ownership) -> bool:
        if not isinstance(ownership, Ownership):  raise TypeError()

        if ownership.has_owner():  return False

        if ownership in self.__ownerships:  return False

        self.__ownerships.append(ownership)
        ownership.set_owner(self)
        return True


    def delete_ownership(self, ownership:Ownership) -> bool:
        if not isinstance(ownership, Ownership): raise TypeError()

        if ownership not in self.__ownerships: return False

        dell_ownership = None
        for elem in self.__ownerships:
            if elem == ownership:
                dell_ownership = elem
                break

        self.__ownerships.remove(dell_ownership)
        ownership.unset_owner()
        return True


    def increase_balance(self, money): # увеличить баланс
        pass

    def decrease_balance(self, money):  # уменьшить баланс
        pass

    def make_move(self) -> int:  # сделать ход
        pass

    def check_balance(self, price) -> bool:
        pass