from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Display the watchlists menu as both buttons and commands
async def profile_menu(message: types.Message):
    # Define the profile menu keyboard buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("➕ Add Watchlist"), KeyboardButton("❌ Remove Watchlist"))
    keyboard.add(KeyboardButton("👁 Show All Watchlists"))

    # Send the menu options as a message with buttons
    await message.answer("Watchlist Management Menu", reply_markup=keyboard)

# Registering profile menu command
async def register_profile_menu(dp):
    dp.message.register(profile_menu, Command(commands=["profile"]))
