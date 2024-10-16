from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Display the add menu as both buttons and commands
async def add_menu(message: types.Message):
    # Define the add menu keyboard buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Add Coin"), KeyboardButton("👛 Add Wallet"))
    keyboard.add(KeyboardButton("🏊 Add Pool"), KeyboardButton("⛽ Add Gas Prices"))

    # Send the menu options as a message with buttons
    await message.answer("Add Menu", reply_markup=keyboard)

# Registering add menu command
async def register_add_menu(dp):
    dp.message.register(add_menu, Command(commands=["add"]))
