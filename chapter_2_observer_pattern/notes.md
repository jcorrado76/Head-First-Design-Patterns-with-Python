= The Observer Pattern =
We have a weather sensor that takes into account weather conditions.
We have a `WeatherData` object that knows how to talk to the sensor.
We want to update three output downstream systems.

We are guaranteed that the `measurementsChanged()` method of the `WeatherData` object will be called whenever the weather measurements have been updated.
We don't know or care how this method is called; we just know that it will be.
We need to implement the body of `measurementsChanged()` method so that it updates the three output systems.

The system must be scalable - so that we can dynamically add additional downstream systems that need to listen for updates.

In our naive implementation, we have the lines:
{{{class="brush: python"
self.currentConditionsDisplay.update(self.temp, self.humidity,
		self.pressure)
self.statisticsDisplay.update(self.temp, self.humidity,
		self.pressure)
self.forecastDisplay.update(self.temp, self.humidity,
		self.pressure)
}}}

In this implementation, we are coding to concrete implementations (`currentConditionsDisplay`, `statisticsDisplay`, `forecastDisplay`), instead of an interface.
So, first of all , we won't be able to dynamically add new downstream elements without having to change this section of the `measurementsChanged()` method.
This could become a large mess of invoking the `update` method of various downstream elements.
In addition, if the signature of `update` ever changes, we'd need to make the changes in every line.

The change that needs to be encapsulated is which downstream element we're trying to invoke `update` on.

The *observer pattern* is a push-based pattern that has a singleton that keeps a running list of downstream elements, and it's the responsibility of the singleton to call the `update` methods on each downstream object.
In addition, there is a register and delete method exposed on the singleton object that the downstream elements can call to subscribe to the data.

We will call this singleton the *Subject*, and the downstream objects the *Observers*.

We will create an abstract interface for the Subject, as well as one for the Observers.

The Subject interface needs:
* abstract `registerObserver()`
* abstract `removeObserver()`
* abstract `notifyObservers()`

A concrete Subject implementation class needs to implement:
* `registerObserver()`
* `removeObserver()`
* `notifyObservers()`
* `getState()`
* `setState()`

The Observer interface only needs a:
* abstract `update()`

Any concrete observer class implementations will have:
* `update()`
* other observer-specific methods

In the Observer Pattern, the subjects and observers are loosely coupled.
They are loosely coupled because the only thing the Subject assumes about a given Observer is that it will implement a specific interface (i.e. `update()`).

Because the Subject only depends on the abstract interface part of a given observer, any developers can add additional concrete observers as they want, as long as they obey the abstract interface.
Changes to a concrete subject or observer will not affect one another, as long as they still meet their obligation to implement their respective interfaces.

This is a design principle:
*Strive for loosely coupled designs between objects that interact*.
Loosely coupled OO systems allow us to minimize dependency between objects, which allows them to handle change better as they won't affect one another.


So, how do we actually *do* this?
For this problem, the `WeatherData` class will be the "subject", and the various downstream elements will be the concrete "observers".

In my implementation of the observer objects, I've added functionality for a single observer to be registered with multiple subscriptions.
In addition, I've added the functionality for the Subject objects to output to stdout when they remove an observer from their subscription.


If you had a more advanced scenario, where there was some business logic involved in terms of how the observers handle input from different subject objects, you would just need to encapsulate that logic inside of their `update()` method.

For example, instead of calling `display()` immediately inside that method, you could call some other function that lazily evaluates whether to fire off the `display()` method, or you could do some computation to determine what should happen next based on the data it's received so far.

I figured it made sense to put a concrete implementation of the constructor for the observer objects in the abstract base class.
This is a specific constructor used to instantiate a display object and immediately subscribe to a subject.



