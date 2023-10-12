import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TOKEN-BOT'))
dp = Dispatcher(bot)