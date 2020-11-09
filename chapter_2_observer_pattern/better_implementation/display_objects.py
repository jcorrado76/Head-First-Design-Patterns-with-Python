from abc import ABC, abstractmethod
from weather_data import Subject
# here are the classes for the downstream systems
class Observer(ABC):
    def __init__(self, weatherData=None):
        """Constructor for the Observers.
        For weatherData, you can pass either an object that is a
        subclass of Subject, or a list of objects that are subclasses
        of Subject.
        This constructor will maintain a running list of the subscriptions
        this observer is subscribed to, and will register with each one
        """
        self.subscriptions = []
        if weatherData is not None:
            if isinstance(weatherData, list):
                self.subscriptions.extend(weatherData)
                for subject in weatherData:
                    assert isinstance(subject, Subject), \
                        "{} must inherit from Subject base class".format(subject)
                    subject.registerObserver(self)
            elif isinstance(weatherData, Subject):
                self.subscriptions.append(weatherData)
                weatherData.registerObserver(self)
            else:
                raise ValueError("Invalid input for Subject")

    def register_subscription(self, weatherData):
        assert isinstance(weatherData, Subject), \
            "{} must inherit from Subject base class".format(weatherData)
        weatherData.registerObserver(self)

    def deregister_subscription(self, weatherData):
        assert isinstance(weatherData, Subject), \
            "{} must inherit from Subject base class".format(weatherData)
        weatherData.removeObserver(self)

    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass

# just a thing interface that will require derived classes to implement a method
# called display
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class CurrentConditionsDisplay(Observer, DisplayElement):
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: {:.1f}F degrees and {:.1f}% humidity".format(self.temperature, self.humidity))

# task: create a Heat Index element. This will be an example of taking the three
# inputs from the WeatherData object, and using a formula to compute a new
# derived quantity, and do some displaying

def heat_index(T, RH):
    """This is just the mathematical function found in the book Heads First
    Design Patterns that is used to compute the heat index

    It takes in the temperature and the relative humidity, and returns a float
    value that is the heat index
    """
    return 16.923 + (1.85212e-1 * T)  \
        + (5.37941 * RH) - (1.00254e-1 * T * RH) \
        + (9.41695e-3 * T**2) + (7.28898e-3 * RH**2) \
        + (3.45372e-4 * T**2 * RH) - (8.14971e-4  * T * RH**2) \
        + (1.02102e-5 * T**2 * RH**2) - (3.8646e-5 * T**3) \
        + (2.91583e-5 * RH**3) + (1.42721e-6 * T**3 * RH) \
        + (1.97483e-7 * T * RH**3) - (2.18429e-8 * T**3 * RH**2) \
        + (8.43296e-10 * T**2 * RH**3) - (4.81975e-11 * T**3 * RH**3)

class HeatIndexDisplay(Observer, DisplayElement):
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def compute_heat_index(self):
        self.heatindex = heat_index(self.temperature, self.humidity)

    def display(self):
        self.compute_heat_index()
        print("Heat index is {:.5f}".format(self.heatindex))
