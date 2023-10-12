import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot('6322657273:AAGdxgG-h8t71yfZhIa7vi39ouvGSASD-Vs')
dp = Dispatcher(bot)