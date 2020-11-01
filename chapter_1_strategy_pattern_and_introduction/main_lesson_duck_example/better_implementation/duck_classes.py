from abc import ABC, abstractmethod
from fly_behavior import *
from quack_behavior import *

def is_proper_quack_behavior(quackBehavior):
    return isinstance(quackBehavior, QuackBehavior)

def is_proper_fly_behavior(flyBehavior):
    return isinstance(flyBehavior, FlyBehavior)

class Duck(ABC):
    def __init__(self):
        # this is unecessary since we necessarily must do this in the derived
        # class constructor. Even if we set something here, it will be overriden
        # in the derived class __init__ method.
        self.flyBehavior = FlyBehavior()
        self.quackBehavior = QuackBehavior()

    # all ducks can swim
    def swim(self):
        print("Swim!")

    # we're hiding implementation details of quack from the user, while
    # delegating it to the QuackBehavior interface. The user only need worry
    # about remembering that every duck exposes a performQuack() method
    def performQuack(self):
        assert is_proper_quack_behavior(self.quackBehavior),\
            "self.quackBehavior must be set to an instance of a class that inherits from the QuackBehavior interface"
        self.quackBehavior.quack()

    def setQuackBehavior(self, newQuackBehavior):
        assert is_proper_quack_behavior(newQuackBehavior),\
            "self.quackBehavior must be set to an instance of a class that inherits from the QuackBehavior interface"
        self.quackBehavior = newQuackBehavior

    def performFly(self):
        assert is_proper_fly_behavior(self.flyBehavior),\
            "self.flyBehavior must be set to an instance of a class that inherits from the FlyBehavior interface"
        self.flyBehavior.fly()

    def setFlyBehavior(self, newFlyBehavior):
        assert is_proper_fly_behavior(newFlyBehavior),\
            "self.flyBehavior must be set to an instance of a class that inherits from the FlyBehavior interface"
        self.flyBehavior = newFlyBehavior

    # the user MUST override this
    @abstractmethod
    def display(self):
        pass

# NOTE: all of these duck classes possess self.performFly and
# self.performQuack methods, even though they're hidden and implemented
# elsewhere
class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I am a MallardDuck")

class RedHeadDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I am a RedHeadDuck")

class RubberDuck(Duck):
    def __init__(self):
        self.quackBehavior = Squeak()
        self.flyBehavior = FlyNoWay()

    def display(self):
        print("I am a RubberDuck")

class DecoyDuck(Duck):
    def __init__(self):
        self.quackBehavior = NoQuack()
        self.flyBehavior = FlyNoWay()

    def display(self):
        print("I am a DecoyDuck")

class ModelDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyNoWay()

    def display(self):
        print("I am a ModelDuck, but I can't fly :(")
