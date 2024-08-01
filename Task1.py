def aggregate_weather_data(records):
    from collections import defaultdict

    city_data = defaultdict(lambda: {'temperature_sum': 0, 'temperature_count': 0,
                                     'humidity_sum': 0, 'humidity_count': 0})

    for record in records:
        city = record['city']
        if 'temperature' in record:
            city_data[city]['temperature_sum'] += record['temperature']
            city_data[city]['temperature_count'] += 1
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1

    result = {}
    for city, data in city_data.items():
        avg_temp = data['temperature_sum'] / data['temperature_count'] if data['temperature_count'] > 0 else None
        avg_humidity = data['humidity_sum'] / data['humidity_count'] if data['humidity_count'] > 0 else None
        result[city] = {'average_temperature': avg_temp, 'average_humidity': avg_humidity}

    return result

records = [
    {'city': 'New York', 'temperature': 70, 'humidity': 60},
    {'city': 'Los Angeles', 'temperature': 75},
    {'city': 'New York', 'humidity': 65},
    {'city': 'Chicago', 'temperature': 60, 'humidity': 55},
    {'city': 'Los Angeles', 'humidity': 58}
]

print(aggregate_weather_data(records))
