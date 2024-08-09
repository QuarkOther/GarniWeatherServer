#/weatherstation/updateweatherstation.php?ID=01&PASSWORD=&action=updateraww&realtime=1&rtfreq=5&dateutc=now&baromin=29.90&tempf=81.8&dewptf=60.2&humidity=48&windspeedmph=1.5&windgustmph=1.5&winddir=300&rainin=0.0&dailyrainin=0.0&solarradiation=756.83&UV=5.9&indoortempf=78.4&indoorhumidity=54


class DataSplit:
    """
    A class to split raw weather station data into a dictionary.

    Attributes:
    ----------
    raw_string_data : str
        The raw weather station data as a string.
    """
    def __init__(self, raw_data_input):
        """
        Constructs all the necessary attributes for the DataSplit object.

        Parameters:
        ----------
        raw_data_input : str
            The raw weather station data as a string.
        """
        self.raw_string_data = raw_data_input

    def get_data(self):
        """
        Returns the split data as a dictionary.

        Returns:
        -------
        dict
            A dictionary containing the split weather station data.
        """
        return self.split_raw_data()

    def split_raw_data(self):
        """
        Splits the raw weather station data into a dictionary.

        Returns:
        -------
        dict
            A dictionary containing the split weather station data.
        """
        split_raw_data = self.raw_string_data.split("&")
        data_dict = {}
        for item in split_raw_data:
            if '=' in item:
                key, value = item.split('=', 1)
                data_dict[key] = value
        return data_dict
