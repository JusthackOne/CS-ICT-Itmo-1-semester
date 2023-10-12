from aiogram import types, Dispatcher
from create_bot import bot
from weather.weather import weather
from weather.weatherform import formweather


# -------------Старт бота---------------------
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую вас в боте Weather Guru!\nЧтобы узнать погоду, напишите название города!')

# Get weather
# @dp.message_handler()
async def send_weather(message: types.Message):
    data = await weather.get_weather(message.text)
    print(data)
    if await weather.is_valid_city(data):
        text, photo = await formweather.get_weather_text(data)

        await bot.send_photo(chat_id=message.chat.id,
                             photo=photo,
                             caption=text,
                             parse_mode='HTML')
        return
    await message.reply('Проверьте название населённого пункта')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(send_weather, content_types=[types.ContentType.TEXT,])

