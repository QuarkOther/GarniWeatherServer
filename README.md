```markdown
# GarniWeatherServer

A program that reads weather data sent from the Garni weather station (http) on port 80 and pushes it to a MySQL database.

## Features

- Reads weather data from Garni weather station.
- Parses and processes the weather data.
- Converts data to metric units.
- Stores the processed data in a MySQL database.
- Prepares data for visualization in Grafana.

## Requirements

- Python 3.12
- MySQL
- Docker

## Installation

### Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
### RUN with docker-compose:
    ```sh
    docker-compose up -d
    ```

#### Build the Docker image:
    ```sh
    docker build -t garni-weather-server .
    ```

#### Run the Docker container:
    ```sh
    docker run -d -p 80:80 --name garni-weather-server garni-weather-server
    ```

## Configuration

- Ensure your MySQL database is running and accessible.
- Update the configuration files in the `conf/` directory as needed.
 - specifically: IP address of the pc running the server

## Usage

- The server will start reading data from the Garni weather station on port 80.
- Data will be processed and stored in the MySQL database.

## TODO

- Prepare Grafana dashboard for the data from MySQL database.

## License

This project is licensed under the MIT License.
```
