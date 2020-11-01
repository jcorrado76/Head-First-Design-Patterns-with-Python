Suppose we need to add a new feature to our implementation of Ducks.
Naively, we could add a `fly()` method in the `Duck` class, and have all subsequently created ducks inherit the new method.
What happens when we create a `RubberDuck` class. Does this class share the same _kind_ of `fly` as `MallardDuck`?
No, it doesn't. 
Not all ducks should be able to fly. You will mostly feel the cost of this issue when it comes to code reuse and maintenance on the product.
*Every time* you create a new duck class that shouldn't fly or quack, you'll need to override those methods in the derived classes.
Furthermore, suppose you need to do maintenance on these classes. If something affects how the ducks fly, you'll need to implement that change in every single class that you overrode.

Apply the design principle:
*Take what varies in your application, and encapsulate it and separate it out from the rest of your code.*

In our case, there are two features that vary across ducks:
* how the `fly()` method is implemented
* how the `quack()` method is implemented

Pull these methods out of the `Duck` class, and create a new set of classes to represent each behavior.
So we'll create a new class for each variation of the `fly` behavior, and a new class for each variation of the `quack` behavior.

What about creating a single class for the `fly` behavior, and a single class for the `quack` behavior, and just putting all variations as different methods inside those classes?
Pros:
* all your methods are centralized, and encapsulated in the same class - easier to track down and change functionality
* you don't need to manage multiple classes
Cons:
* you want to be able to call the same method in each new derived duck class. You don't want to call different identifiers `FlyWithWings()`, `FlyNoWay` in your derived classes (remember, these are supposed to implement the _same_ feature/functionality). You want to just call something like `fly()` in all your derived classes (consistent API - easier to use, and your duck classes don't need to know anything about the implementation details for their own behaviors).
* each new derived duck class now has a whole bunch of methods exposed to it that provide redundant functionality and won't ever be used (this isn't important for our trivial example of ducks, but what if the feature we're trying to refactor is something sensitive, like loading proprietary data from different sources? You don't want that data to just be exposed to every derived instance)

To solve this, let's apply another design principle:
*Program to an interface, not an implementation*
Use an interface to represent each behavior:
* `FlyBehavior`
* `QuackBehavior`

We'll make a set of classes whose entire reason for existing is to represent a behavior.
It's these behavior classes, rather than the `Duck` class, that will implement the behavior interface.
This is distinct from what we were doing before, which was relying on an implementation in the superclass `Duck`, or a specialized implementation in the duck subclasses.
The actual implementation of these behaviors won't be locked in the duck subclass.

Using this design, new ducks can be implemented and reuse our fly and quack behaviors because these behaviors are no longer hidden away in the duck classes.
In addition, we can add new behaviors without modifying any of our existing behavior classes or touching any of the duck classes already using the behaviors we previously implemented.

The key is that a duck will now delegate its flying and quacking behavior, instead of using quacking and flying methods defined in the duck class, or the derived class.
We need to add two instance variables to the `Duck` class called `flyBehavior` and `quackBehavior`.
Each duck object will set these variables polymorphically in order to specify which behavior type is appropriate for this duck at runtime.

We will remove the `fly()` and `quack()` methods from the `Duck` class and any subclasses because it's been moved out into the `FlyBehavior` and `QuackBehavior` classes.

We will replace `fly()` and `quack()` in the `Duck` class with two similar methods, called `performFly()` and `performQuack()` (remember - we still want a consistent API from the perspective of someone trying to use one of these derived classes; we want our user to be able to just call `performFly` from any derived duck class).

Note that since this is python, nothing is going to stop you from going:
`self.flyBehavior = Quack() # Quack IS a QuackBehavior, NOT a FlyBehavior`
Such as the type checking in C++ or Java (since a `Quack` IS A `QuackBehavior`).
However, you will get a *runtime error* if your `Quack` doesn't implement `performFly()`.
It would be best to implement some manual checking in here to replicate that behavior.
We'd like to restrict the user to select an appropriate quack behavior, and an appropriate fly behavior, i.e. instantiate those member variables with proper fly behaviors.

I did this by adding an `assert isinstance` inside the `performFly` methods in the abstract base class.
This way, it's all handled between the `Duck` abstract base class, and the abstract interface base classes.
Any new developers or users of the duck subclasses now no longer need to worry about implementation details or anything.
All they do is respect the API exposed by the abstract base behavior interface classes.


Now, since we have this powerful abstraction for how to set and encapsulate certain sets of behaviors under interface classes, we can extract additional value from this framework by adding the capability of setting the behavior dynamically.
If you want, you can define a getter for these behaviors to update what the behavior of the duck is.
We'll do this by adding a `setFlyBehavior` method, and another for the quack behavior.
Be careful to do the type checking manually as we did above when instantiating the member variable, as python does not do this for you automatically the way C++ does when you declare you variable of a certain type.

In a sense, setting the `flyBehavior` and `quackBehavior` members inside the `__init__` in the `Duck` abstract base class doesn't actually do anything since we're in python.
You can just change it to be whatever you want at any point in time, since it's dynamically typed.

Let's test this new functionality by adding a new duck variation, called `ModelDuck`, and a new flight behavior type `FlyRocketPowered`.
Our `ModelDuck` is going to start off unable to fly. But then, we'll add a rocket to it during runtime so that it can fly!


This allowed us to dynamically change the flying behavior of our new duck type.
If you had implemented the fly behavior right inside the duck class, it would have taken a ton of extra code, and exposing a new parameter perhaps to implement some workaround to get the same functionality.

In summary: to change a duck's behavior at runtime, just call the setter method for that behavior.

We have a `Duck` abstract base class, and several derived duck classes, such as `MallardDuck`, etc.
These derived duck classes have an *IS-A* relationship to teh `Duck` abstract base class.

In addition, `Duck` abstract base class has a *HAS-A* relationship to the `FlyBehavior` and `QuackBehavior`.

Finally, the `FlyWithWings` and `FlyNoWay` classes have an *IMPLEMENTS* relationship to the `FlyBehavior` class, and similarly for the quack behaviors.

In this way, we think of the `FlyWithWings`, and `FlyNoWay` classes as "algorithms" rather than behaviors, as they are interchangeable from the perspective of the duck class developers and users.


This is a good example of when the *HAS-A* relationship can be more appropriate than the *IS-A* relationship (don't jump straight to default inheritance!).
This is called *composition*. Instead of _inheriting_ the behavior, we create the desired behavior by _composing_ the duck classes with the proper behavior object.

This leads to the final design principle of this example:
*Favor composition over inheritance*.
Using composition to create systems allows us more flexibility - we can encapsulate a family of algorithms into their own set of classes, and it allows us to *change behavior at runtime* (as long as our "behavior" interface is the right interface for the task at hand).

What if you wanted to create a new system that implemented a *duck call*? In other words, it mimics the quacks of ducks, but it isn't a `Duck`, and therefore doesn't inherit from `Duck`.
As a result of the de-coupled composition technique we used to implement the quack behavior, we just need to pass an instance of the appropriate quack behavior to our duck call class, function or whatever system you use to implement it.

This pattern is called the *Strategy* pattern:
You have a family of algorithms (`Quack`, `NoQuack`, `Squeak`, etc.), and you want them to be encapsulated and treat them as interchangeable.
The *Strategy* pattern allows you to vary these algorithms independently from each other, as well as downstream and upstream changes in API and functionality.

