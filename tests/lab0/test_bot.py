import pytest


from aiogram_tests import MockedBot
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE

from aiogram import Bot, Dispatcher, types


# Please, keep your bot tokens on environments, this code only example
bot = Bot('123456789:AABBCCDDEEFFaabbccddeeff-1234567890')
dp = Dispatcher()


@pytest.mark.asyncio
async def test_echo():
    request = MockedBot(MessageHandler(echo))
    calls = await request.query(message=MESSAGE.as_object(text="Hello, Bot!"))
    answer_message = calls.send_messsage.fetchone()
    assert answer_message.text == "Hello, Bot!"