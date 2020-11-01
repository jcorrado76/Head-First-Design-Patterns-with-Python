In this case study, we'll solve an additional problem using the *strategy pattern*.

We have a list of classes and interfaces someone wrote to create an action adventure game.
However, they need to be organized in a way that allows for flexibility and extensibility of certain parts, or behaviors.
We will organize them into the strategy pattern.

Here are the list of pieces:
* `Character` class containing a `WeaponBehavior weapon;`, exposing a `fight()` method
* `Queen` class exposing a `fight()` method
* `King` class exposing a `fight()` method
* `Knight` class exposing a `fight()` method
* `Troll` class exposing a `fight()` method
* `WeaponBehavior` class - this is what we'll use as our abstract interface base class; it exposes a `useWeapon()` method and will be used in composition with our `Character` class (our `Character` *HAS-A* `WeaponBehavior` called `weapon`)
* `KnifeBehavior` class with `useWeapon()` method that implements "cutting with a knife"
* `BowAndArrowBehavior` class with `useWeapon()` method that implements "shooting an arrow with a bow"
* `AxeBehavior` class with `useWeapon()` method that implements "chopping with an axe"
* `SwordBehavior`class with `useWeapon()` method that implements "swinging a sword"
* `setWeapon(WeaponBehavior w)` method that our `Character` possesses, and will allow our character to change weapons dynamically during runtime


We only have one behavior to implement, and further, because of the strategy pattern, we don't even have to think about it.
All we do is set which behavior in our character's constructor.
Then, it will come with the correct method with a consistent API.

Note that the flexibility with the composition relationship in this example allows us to make a weapon out of any object that comes to mind! We just define a class for it, and then we equip it on an instantiated `Character`.
