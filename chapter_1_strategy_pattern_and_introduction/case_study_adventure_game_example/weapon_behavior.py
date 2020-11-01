from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    @abstractmethod
    def useWeapon(self):
        pass

class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("cutting with a knife")

class BowAndArrowBehavior(WeaponBehavior):
    def useWeapon(self):
        print("shooting an arrow with a bow")

class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("chopping with an axe")

class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("swinging a sword")
