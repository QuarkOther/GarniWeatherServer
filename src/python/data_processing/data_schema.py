class DataSchema:
    """
    A class to represent the schema of weather station data and convert it to metric units.

    Attributes:
    ----------
    weather_station_id : str
        The ID of the weather station.
    baromin : float
        The barometric pressure in inches of mercury.
    tempf : float
        The temperature in degrees Fahrenheit.
    dewptf : float
        The dew point temperature in degrees Fahrenheit.
    humidity : int
        The humidity percentage.
    windspeedmph : float
        The wind speed in miles per hour.
    windgustmph : float
        The wind gust speed in miles per hour.
    winddir : int
        The wind direction in degrees.
    rainin : float
        The rainfall in inches.
    dailyrainin : float
        The daily rainfall in inches.
    solarradiation : float
        The solar radiation in watts per square meter.
    UV : float
        The UV index.
    indoortempf : float
        The indoor temperature in degrees Fahrenheit.
    indoorhumidity : int
        The indoor humidity percentage.
    """
    def __init__(self, input_data_dict):
        """
        Constructs all the necessary attributes for the DataSchema object.

        Parameters:
        ----------
        input_data_dict : dict
            A dictionary containing the weather station data.
        """
        self.weather_station_id = input_data_dict['/weatherstation/updateweatherstation.php?ID']
        self.baromin = float(input_data_dict['baromin'])
        self.tempf = float(input_data_dict['tempf'])
        self.dewptf = float(input_data_dict['dewptf'])
        self.humidity = int(input_data_dict['humidity'])
        self.windspeedmph = float(input_data_dict['windspeedmph'])
        self.windgustmph = float(input_data_dict['windgustmph'])
        self.winddir = int(input_data_dict['winddir'])
        self.rainin = float(input_data_dict['rainin'])
        self.dailyrainin = float(input_data_dict['dailyrainin'])
        self.solarradiation = float(input_data_dict['solarradiation'])
        self.UV = float(input_data_dict['UV'])
        self.indoortempf = float(input_data_dict['indoortempf'])
        self.indoorhumidity = int(input_data_dict['indoorhumidity'])
        self.to_metric()

    def get_data(self):
        """
        Returns the data as a dictionary.

        Returns:
        -------
        dict
            A dictionary containing the weather station data.
        """
        return self.__dict__

    def to_metric(self):
        """
        Converts the imperial units to metric units.
        """
        self.baromin = self.baromin * 33.863
        self.tempf = (self.tempf - 32) * 5 / 9
        self.dewptf = (self.dewptf - 32) * 5 / 9
        self.windspeedmph = self.windspeedmph * 1.60934
        self.windgustmph = self.windgustmph * 1.60934
        self.rainin = self.rainin * 25.4
        self.dailyrainin = self.dailyrainin * 25.4
        self.solarradiation = self.solarradiation * 0.2146
        self.indoortempf = (self.indoortempf - 32) * 5 / 9
