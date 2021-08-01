def get_temperature_by_city(city):
    if city == "Provo":
        temperature = temperature_data.get(city, 72)
    elif city == "Orem":
        temperature = temperature_data.get(city, 78)
    elif city == "lindon":
        temperature = temperature_data.get(city, 66)
    elif city == "pleasant grove":
        temperature = temperature_data.get(city, 80)
    elif city == "Pleasant Grove":
        temperature = temperature_data.get(city, 80)
    elif city == "Springville":
        temperature = temperature_data.get(city, "unknown!") 
    else: temperature = "Please Specify the route"    
        
    return temperature

def convert_fahrenheit_to_celsius(ftemp):
    return round((ftemp - 32) / 1.8)

def changeCity():
    get_temperature_by_city(city = str.replace('Provo', 'lindon'))


temperature_data = {
    "provo": 72,
    "orem": 78,
    "lindon": 66,
    "pleasant grove": 80,
    "Springville": "unknown!"
}