#/weatherstation/updateweatherstation.php?ID=01&PASSWORD=&action=updateraww&realtime=1&rtfreq=5&dateutc=now&baromin=29.90&tempf=81.8&dewptf=60.2&humidity=48&windspeedmph=1.5&windgustmph=1.5&winddir=300&rainin=0.0&dailyrainin=0.0&solarradiation=756.83&UV=5.9&indoortempf=78.4&indoorhumidity=54


class DataSplit:
    def __init__(self, raw_data_input):
        self.data = raw_data_input
        self.split_raw_data()

    def get_data(self):
        return dict(self.data)

    def split_raw_data(self):
        split_raw_data = self.data.split("&")
        self.data = split_raw_data
