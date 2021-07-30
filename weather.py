

def get_temperature_by_city(city: str = "Provo"):
    temperature = temperature_data.get(city, 76)
    return temperature


def convert_fahrenheit_to_celsius(ftemp):
    return round((ftemp - 32) / 1.8)


temperature_data = {
    "provo": 72,
    "orem": 78,
    "lindon": 66,
    "pleasant grove": 80
}