import os
import aiohttp
class Weather:
    def __init__(self):
        self.URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather?'

    async def get_weather(self, city):
        params = {'q': city,
                  'appid': os.getenv("TOKEN-WEATHER"),
                  'lang': 'ru',
                  "units": 'metric',
                  }

        async with aiohttp.ClientSession() as session:
            async with session.get(self.URL_WEATHER, params=params) as response:
                await session.close()
                return await response.json()

    async def is_valid_city(self, data):
        if data['cod'] == '404':
            return False
        return True

weather = Weather()
