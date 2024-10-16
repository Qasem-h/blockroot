from aiogram import types

async def settings_handler(message: types.Message):
    await message.answer("Settings Menu:\n - Language\n - Scam Filter\n - Contact Us")
