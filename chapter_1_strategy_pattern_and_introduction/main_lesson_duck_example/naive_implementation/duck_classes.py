class Duck(object):
    def __init__(self):
        pass

    def swim(self):
        print("Swim!")

    def display(self):
        print("I am a Duck")

    # problematic methods, may not apply to all potential subclasses
    def fly(self):
        print("Fly!")

    def quack(self):
        print("Quack!")

class MallardDuck(Duck):
    def __init__(self):
        pass

    def display(self):
        print("I am a MallardDuck")

class RedHeadDuck(Duck):
    def __init__(self):
        pass

    def display(self):
        print("I am a RedHeadDuck")

class RubberDuck(Duck):
    def __init__(self):
        pass

    def display(self):
        print("I am a RubberDuck")

    # overriden to do nothing
    def fly(self):
        pass

    # overriden to Squeak
    def quack(self):
        print("Squeak!")

class DecoyDuck(Duck):
    def __init__(self):
        pass

    def display(self):
        print("I am a DecoyDuck")

    # overridden to do nothing
    def fly(self):
        pass

    # overridden to do nothing
    def quack(self):
        pass
