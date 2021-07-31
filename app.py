from flask import Flask
import weather

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to the weather machine! Try going to http://localhost/temperature/provo to see how it works!'


@app.route('/temperature/<city>')
def temperature(city):
    city_temp = weather.get_temperature_by_city(city)
    
    return f"The temperature in {city} is {city_temp}"


@app.route('/temperature_c/<city>')
def temperature_celsius(city):
    city_temp = weather.get_temperature_by_city()
    return f"The temperature in {city} is {city_temp} ({weather.convert_fahrenheit_to_celsius(city_temp)} Celsius)"


if __name__ == '__main__':
    app.run()