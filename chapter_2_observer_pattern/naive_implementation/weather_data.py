def WeatherData(object):
    def getTemperature(self):
        return 1.0
    def getHumidity(self):
        return 2.0
    def getPressure(self):
        return 3.0

    def measurementsChanged(self):
        # grab the most recent measurements
        # we assume these are already implemented
        self.temp = self.getTemperature()
        self.humidity = self.getHumidity()
        self.pressure = self.getPressure()

        # now update the displays
        self.currentConditionsDisplay.update(self.temp, self.humidity,
                self.pressure)
        self.statisticsDisplay.update(self.temp, self.humidity,
                self.pressure)
        self.forecastDisplay.update(self.temp, self.humidity,
                self.pressure)

