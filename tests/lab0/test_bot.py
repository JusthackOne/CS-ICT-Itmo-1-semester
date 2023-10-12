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