# Weather API (v0.1.0)

Simple Weather API which fetches weather data from a specified source, maps the data and outputs agrigated values.

## System Requirments

- Python 3.7+
- Git

## Installation

```bash
git clone git@github.com:qoda/weather-api.git weather-api
cd weather-api/
```

## Run Development Server

```bash
python3 -m venv ve
. ve/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running tests

```bash
python -m pip install requirements.test.txt
coverage run manage.py test weatherapi --settings=weatherapi.settings
coverage report -m
```

## Config

Create a .env file inside the weatherapi/ directory and set the variables as follows:

| Name                       | Type | Default                                                  |
|----------------------------|------|----------------------------------------------------------|
| DEBUG                      | Bool | True                                                     |
| SECRET_KEY                 | Str  | None                                                     |
| WEATHERAPI_URL             | Str  | https://api.weatherapi.com/v1/forecast.json              |
| WEATHERAPI_KEY             | Str  | None                                                     |

## Documentation

Self-generated documentation is available at http://localhost:8000/swagger/
