import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Adjust the path to include the project root

# Load environment variables from the .env file
load_dotenv()

# Fetch Telegram API token from .env
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

if not API_TOKEN:
    raise ValueError("No API token provided. Please set TELEGRAM_API_TOKEN in your .env file.")

# Initialize Bot and Dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Import handlers for different menus
from telegram_bot.handlers.main_menu_handler import main_menu, register_main_menu
from telegram_bot.handlers.add_menu_handler import add_menu
from telegram_bot.handlers.edit_menu_handler import edit_menu
from telegram_bot.handlers.profile_menu_handler import profile_menu
from telegram_bot.handlers.subscription_menu_handler import subscription_menu

# Import handlers for specific functionalities (wallets, pools, coins)
from telegram_bot.handlers.wallet_handler import router as wallet_router
from telegram_bot.handlers.pool_handler import router as pool_router
from telegram_bot.handlers.coin_handler import router as coin_router

# Register handlers for main menus
dp.message.register(main_menu, Command(commands=["start", "menu"]))
dp.message.register(add_menu, Command(commands=["add"]))
dp.message.register(edit_menu, Command(commands=["edit"]))
dp.message.register(profile_menu, Command(commands=["profile"]))
dp.message.register(subscription_menu, Command(commands=["subscription"]))

# Register the main menu
register_main_menu(dp)

# Register additional routers for specific functionalities
dp.include_router(wallet_router)
dp.include_router(pool_router)
dp.include_router(coin_router)

# Main function to run the bot
async def main():
    print("Bot is starting...")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
