from abc import ABC, abstractmethod

# here are the singleton classes
class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass
    @abstractmethod
    def removeObserver(self, observer):
        pass
    @abstractmethod
    def notifyObservers(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)
        # print to stdout what was removed from what
        print("Removed {} from {} subscription".format(type(observer).__name__, type(self).__name__))

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, newTemp, newHumidity, newPressure):
        self.temp = newTemp
        self.humidity = newHumidity
        self.pressure = newPressure
        self.measurementsChanged()
