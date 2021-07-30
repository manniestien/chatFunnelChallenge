import app
import pytest
import weather


def test_app_index():
    result = app.hello_world()
    assert 'weather machine' in result


def test_temperature_unknown():
    result = app.temperature(city="Springville")
    assert result == "The temperature in Springville is unknown!"


def test_temperature_provo():
    result = app.temperature(city="Provo")
    assert result == "The temperature in Provo is 72"


def test_temperature_orem():
    result = app.temperature(city="Orem")
    assert result == "The temperature in Orem is 78"


def test_temperature_pg():
    result = app.temperature(city="pleasant grove")
    assert result == "The temperature in pleasant grove is 80"


def test_temperature_pg_caps():
    result = app.temperature(city="Pleasant Grove")
    assert result == "The temperature in Pleasant Grove is 80"


@pytest.mark.parametrize("city,expected", [
    ("provo", 22),
    ("orem", 26),
    ("lindon", 19),
])
def test_celsius(city, expected):
    result = app.temperature_celsius(city=city)
    assert result.endswith(f"({expected} Celsius)")


@pytest.mark.parametrize("ftemp,expected", [
    (19, -7),
    (20, -7),
    (34, 1),
    (66, 19),
])
def test_celsius_conversion(ftemp, expected):
    result = weather.convert_fahrenheit_to_celsius(ftemp)
    assert result == expected
