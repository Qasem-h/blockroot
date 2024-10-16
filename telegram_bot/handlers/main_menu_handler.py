from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Display the main menu as both buttons and commands
async def main_menu(message: types.Message):
    # Define the main menu keyboard buttons
    buttons = [
        [KeyboardButton(text="💰 Add")],
        [KeyboardButton(text="✏️ Edit")],
        [KeyboardButton(text="👤 Watchlists"), KeyboardButton(text="💳 Subscription")]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    # Send the menu options as a message with buttons
    await message.answer("Main Menu", reply_markup=keyboard)

# Registering main menu command
async def register_main_menu(dp):
    dp.message.register(main_menu, Command(commands=["start", "menu"]))
