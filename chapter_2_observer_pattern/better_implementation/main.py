if __name__ == "__main__":
    from weather_data import WeatherData
    from display_objects import CurrentConditionsDisplay, HeatIndexDisplay


    weather_data_instance = WeatherData()
    # register the downstream consumer with the singleton by passing the
    # WeatherData instance into the constructor
    conditions_display = CurrentConditionsDisplay(weather_data_instance)
    heat_index_display = HeatIndexDisplay(weather_data_instance)

    temp = 80 # degrees F
    humidity = 65 # percent
    pressure = 30.4

    # we pass new values into the singleton, and any downstream consumers are
    # automatically udpated
    weather_data_instance.setMeasurements(temp, humidity, pressure)

    temp = 82 # degrees F
    humidity = 70 # percent
    pressure = 29.2
    weather_data_instance.setMeasurements(temp, humidity, pressure)

    temp = 78 # degrees F
    humidity = 90 # percent
    pressure = 29.2
    weather_data_instance.setMeasurements(temp, humidity, pressure)

    conditions_display.deregister_subscription(weather_data_instance)
    temp = 78 # degrees F
    humidity = 90 # percent
    pressure = 29.2
    weather_data_instance.setMeasurements(temp, humidity, pressure)
