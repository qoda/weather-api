from datetime import datetime
import itertools
import statistics

def calculate_weather_stats(forecast_list):
    """Iterates over the weather data and calculates the max, min, avg and
    median from the values.
    """
    try:
        maximum_values = list(map(lambda x: x['day']['maxtemp_c'], forecast_list))
        minimum_values = list(map(lambda x: x['day']['mintemp_c'], forecast_list))
        average_values = list(map(lambda x: x['day']['avgtemp_c'], forecast_list))
        median_values = list(itertools.chain(maximum_values, minimum_values))
    except KeyError:
        return

    weather_stats = {
        'maximum': max(maximum_values),
        'minimum': min(minimum_values),
        'average': round(sum(average_values) / len(average_values), 1),
        'median': round(statistics.median(median_values), 1)
    }
    return weather_stats
