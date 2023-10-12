import pytest
from unittest.mock import AsyncMock
from weather.weather import weather
from handlers.client import command_start, send_weather

@pytest.mark.asyncio
async def test_command_start():
    text_mock = 'Приветствую вас в боте Weather Guru!\nЧтобы узнать погоду, напишите название города!'
    message_mock = AsyncMock(text=text_mock)
    await command_start(message=message_mock)
    message_mock.answer.assert_called_with(text_mock)

@pytest.mark.asyncio
async def test_get_weather():
    city = 'Москва'
    text_mock = "{'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'небольшой дождь', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 11.02, 'feels_like': 10.4, 'temp_min': 8.67, 'temp_max': 13.1, 'pressure': 999, 'humidity': 85, 'sea_level': 999, 'grnd_level': 982}, 'visibility': 10000, 'wind': {'speed': 5.96, 'deg': 240, 'gust': 14.52}, 'rain': {'1h': 0.49}, 'clouds': {'all': 100}, 'dt': 1697111191, 'sys': {'type': 2, 'id': 2000314, 'country': 'RU', 'sunrise': 1697082777, 'sunset': 1697121541}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}"
    message_mock = AsyncMock(text=city)
    await weather.get_weather(message_mock)
    message_mock.answer.assert_called_with(text_mock)
