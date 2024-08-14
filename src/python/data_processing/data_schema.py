from future.backports.datetime import datetime


class DataSchema:
    """
    A class to represent the schema of weather station data and convert it to metric units.

    Attributes:
    ----------
    weather_station_id : str
        The ID of the weather station.
    password : str
        The password of the weather station.
    action : str
        The action of the weather station.
    realtime : str
        The real time of the weather station.
    rtfreq : str
        The real time frequency of the weather station.
    dateutc : datetime
        The date and time in Coordinated Universal Time (UTC).
    datelocal : datetime
        The date and time in local time.
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
        self.password = input_data_dict['PASSWORD']
        self.action = input_data_dict['action']
        self.realtime = input_data_dict['realtime']
        self.rtfreq = input_data_dict['rtfreq']
        self.dateutc = datetime.utcnow()
        self.datelocal = datetime.now()
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
        self.dateutc = str('"' + self.dateutc.strftime("%Y-%m-%d %H:%M:%S")+ '"')
        self.datelocal = str('"' +self.datelocal.strftime("%Y-%m-%d %H:%M:%S")+ '"')
        if self.password == '':
            self.password = "password"
        self.action = str('"' + self.action + '"')
        self.baromin = self.baromin * 33.863
        self.tempf = (self.tempf - 32) * 5 / 9
        self.dewptf = (self.dewptf - 32) * 5 / 9
        self.windspeedmph = self.windspeedmph * 1.60934
        self.windgustmph = self.windgustmph * 1.60934
        self.rainin = self.rainin * 25.4
        self.dailyrainin = self.dailyrainin * 25.4
        self.solarradiation = self.solarradiation * 0.2146
        self.indoortempf = (self.indoortempf - 32) * 5 / 9

    def get_sql_columns(self):
        # Mapping of Python types to SQL types
        python_to_sql = {
            int: "INTEGER",
            float: "FLOAT",
            str: "TEXT",
            bool: "BOOLEAN",
            bytes: "BLOB"
        }

        # List to hold the columns
        columns = []

        # Iterate over the attributes and get their types
        for attr, value in self.__dict__.items():
            sql_type = python_to_sql.get(type(value), "TEXT")  # Default to TEXT if type is unknown
            columns.append(f"{attr} {sql_type}")

        return str(columns).replace("'", '').replace('[', '').replace(']', '')

    def get_write_columns(self):
        return ', '.join(self.__dict__.keys())

    def get_write_values(self):
        return ', '.join([str(value) for value in self.__dict__.values()])
