from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Display the subscription menu as both buttons and commands
async def subscription_menu(message: types.Message):
    # Define the subscription menu keyboard buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💼 Subscription Plans"))

    # Send the menu options as a message with buttons
    await message.answer("Subscription Menu", reply_markup=keyboard)

# Registering subscription menu command
async def register_subscription_menu(dp):
    dp.message.register(subscription_menu, Command(commands=["subscription"]))
