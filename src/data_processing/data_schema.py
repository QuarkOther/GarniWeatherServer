class DataSchema:
    def __init__(self, weather_station_id, baromin, tempf, dewptf, humidity, windspeedmph, windgustmph, winddir, rainin,
                 dailyrainin, solarradiation, UV, indoortempf, indoorhumidity):
        self.weather_station_id = weather_station_id
        self.baromin = baromin
        self.tempf = tempf
        self.dewptf = dewptf
        self.humidity = humidity
        self.windspeedmph = windspeedmph
        self.windgustmph = windgustmph
        self.winddir = winddir
        self.rainin = rainin
        self.dailyrainin = dailyrainin
        self.solarradiation = solarradiation
        self.UV = UV
        self.indoortempf = indoortempf
        self.indoorhumidity = indoorhumidity

    def get_data(self):
        return self.__dict__
