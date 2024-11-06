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
