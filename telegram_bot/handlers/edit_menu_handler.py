from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Display the edit menu as both buttons and commands
async def edit_menu(message: types.Message):
    # Define the edit menu keyboard buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Edit Coin"), KeyboardButton("👛 Edit Wallet"))
    keyboard.add(KeyboardButton("🏊 Edit Pool"), KeyboardButton("⛽ Edit Gas Prices"))

    # Send the menu options as a message with buttons
    await message.answer("Edit Menu", reply_markup=keyboard)

# Registering edit menu command
async def register_edit_menu(dp):
    dp.message.register(edit_menu, Command(commands=["edit"]))
