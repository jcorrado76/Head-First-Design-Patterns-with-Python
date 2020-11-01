from abc import ABC, abstractmethod
from weapon_behavior import *

def is_proper_weapon_behavior(weaponBehavior):
    return isinstance(weaponBehavior, WeaponBehavior)

class Character(ABC):
    def __init__(self):
        # this line doesn't do anything, since we could actually change
        # self.weapon at any point in our program. I leave it here because if
        # this were C++, type checking would be applied here, and then we'd be
        # restricted to derived classes of the WeaponBehavior() class. We will
        # need to implement type checking manually later on
        self.weapon = WeaponBehavior()

    def fight(self):
        assert is_proper_weapon_behavior(self.weapon),\
            "self.weaponBehavior must be set to an instance of a class that inherits from the WeaponBehavior interface"
        self.weapon.useWeapon()

    def setWeapon(self, newWeaponBehavior):
        assert is_proper_weapon_behavior(newWeaponBehavior),\
            "newWeaponBehavior must be set to an instance of a class that inherits from the WeaponBehavior interface"
        self.weapon = newWeaponBehavior

    @abstractmethod
    def display(self):
        pass

class Queen(Character):
    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def display(self):
        print("I am the Queen")

class King(Character):
    def __init__(self):
        self.weapon = KnifeBehavior()

    def display(self):
        print("I am the King")
    
class Knight(Character):
    def __init__(self):
        self.weapon = SwordBehavior()

    def display(self):
        print("I am the Queen's Knight")

class Troll(Character):
    def __init__(self):
        self.weapon = AxeBehavior()

    def display(self):
        print("I am a troll! For the horde!")
