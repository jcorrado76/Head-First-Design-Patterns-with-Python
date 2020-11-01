if __name__ == "__main__":
    from duck_classes import MallardDuck, RedHeadDuck, RubberDuck, DecoyDuck,\
        ModelDuck, FlyRocketPowered

    for duck in [MallardDuck(), RedHeadDuck(), RubberDuck(), DecoyDuck()]:
        duck.display()
        duck.performQuack()
        duck.performFly()
        print("\n")

    model_duck = ModelDuck()
    model_duck.display()
    model_duck.performFly()
    print("But now add a rocket...")
    model_duck.setFlyBehavior(FlyRocketPowered())
    model_duck.performFly()
