import unittest
import os
import sys

from src.python.data_processing.data_split import DataSplit

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(PROJECT_PATH)

from src.python.common.config_load import LoadEnvVars
from src.python.common import config_load


class UnitTests(unittest.TestCase):

    @staticmethod
    def config_load_test():
        LoadEnvVars('src/test/resources/test.conf')
        test_conf_var = config_load.os.getenv('TEST_CONF_VAR')
        print("test_conf_var: ", test_conf_var)
        assert test_conf_var == '10', f"should be 10, got: " + test_conf_var

    @staticmethod
    def data_splitter_test():
        raw_data = "/weatherstation/updateweatherstation.php?ID=01&PASSWORD=&action=updateraww&realtime=1&rtfreq=5&dateutc=now&baromin=29.90&tempf=81.8&dewptf=60.2&humidity=48&windspeedmph=1.5&windgustmph=1.5&winddir=300&rainin=0.0&dailyrainin=0.0&solarradiation=756.83&UV=5.9&indoortempf=78.4&indoorhumidity=54"
        data_splitter = DataSplit(raw_data)
        data_dict = data_splitter.get_data()
        expected_dict = {
            "ID": "01",
            "PASSWORD": "",
            "action": "updateraww",
            "realtime": "1",
            "rtfreq": "5",
            "dateutc": "now",
            "baromin": "29.90",
            "tempf": "81.8",
            "dewptf": "60.2",
            "humidity": "48",
            "windspeedmph": "1.5",
            "windgustmph": "1.5",
            "winddir": "300",
            "rainin": "0.0",
            "dailyrainin": "0.0",
            "solarradiation": "756.83",
            "UV": "5.9",
            "indoortempf": "78.4",
            "indoorhumidity": "54"
        }
        assert data_dict == expected_dict, f"Expected {expected_dict}, but got {data_dict}"

    @staticmethod
    def http_get_message_test():
        import requests
        url = "http://example.com/weatherstation/updateweatherstation.php?ID=01&PASSWORD=&action=updateraww&realtime=1&rtfreq=5&dateutc=now&baromin=29.90&tempf=81.8&dewptf=60.2&humidity=48&windspeedmph=1.5&windgustmph=1.5&winddir=300&rainin=0.0&dailyrainin=0.0&solarradiation=756.83&UV=5.9&indoortempf=78.4&indoorhumidity=54"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print("HTTP GET request successful with status code 200")


if __name__ == '__main__':
    UnitTests.config_load_test()
    UnitTests.data_splitter_test()
    UnitTests.http_get_message_test()
