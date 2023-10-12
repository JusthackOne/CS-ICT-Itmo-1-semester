import datetime
import pytz
from tzwhere import tzwhere


class FormWeather:
    async def get_weather_photo(self, temp):
        if temp >= 20:
            return 'photos/20.jpg'
        if temp >= 10:
            return 'photos/10.jpg'
        if temp >= 0:
            return 'photos/0.jpg'
        if temp >= -10:
            return 'photos/-10.jpg'
        return 'photos/-20.jpg'

    async def get_weather_text(self, data):
        photo_link = await self.get_weather_photo(int(data['main']['temp']))
        photo = open(photo_link, 'rb')
        description = data['weather'][0]['description']

        tz = tzwhere.tzwhere()
        timezon = tz.tzNameAt(float(data['coord']['lat']), float(data['coord']['lon']))
        timezone = pytz.timezone(timezon)
        time = datetime.datetime.now(timezone).strftime("%d-%m %H:%M")

        temp = str( int( data["main"]["temp"] ) )
        pressure = str(int(float(data["main"]["pressure"]) / 1.33317))
        humidity = data["main"]["humidity"]
        visibility = data["visibility"]
        speed = data["wind"]["speed"]

        text = (f'🟢 Погода на <u>{time}</u> по местному времени - <b>{description}</b>\n\n'
                f'Температура: <i>{temp}°C</i>\n'
                f'Давление: <i>{pressure} мм рт. ст</i>\n'
                f'Влажность: <i>{humidity}%</i>\n'
                f'Видимость: <i>{visibility} м</i>\n'
                f'Скорость ветра: <i>{speed} м/с</i>\n'
                )

        if 'rain' in data:
            rain = data['rain']['1h']
            text += f'Дождь: <i>{rain} мм</i>\n'
        if 'snow' in data:
            snow = data['snow']['1h']
            text += f'Дождь: <i>{snow} мм</i>\n'

        return text, photo

formweather = FormWeather()