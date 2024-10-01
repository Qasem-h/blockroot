import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import asyncio  # Import asyncio to run asynchronous code
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Adjust the path to include the project root
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

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

# Create router for command registration
router = Router()

# Import handlers after initializing dp
from telegram_bot.handlers.user_handler import start_bot
from telegram_bot.handlers.wallet_handler import add_user_wallet, list_user_wallets, remove_user_wallet
from telegram_bot.handlers.subscription_handler import subscribe_user
from telegram_bot.handlers.gas_alert_handler import add_gas_alert, list_gas_alerts, remove_gas_alert

# Register user and subscription handlers
router.message.register(start_bot, Command(commands=["start"]))
router.message.register(subscribe_user, Command(commands=["subscribe"]))

# Define separate handler for adding a wallet
@router.message(Command(commands=["add_wallet"]))
async def handle_add_wallet(message: types.Message):
    args = message.text.split()[1:]
    if len(args) < 2:
        await message.answer("Please provide both a blockchain and a wallet address.\nUsage: /add_wallet <blockchain> <address>")
        return
    blockchain = args[0]
    address = args[1]
    # No need to pass blockchain and address here, they are handled in add_user_wallet itself
    await add_user_wallet(message)

# Define separate handler for listing wallets
@router.message(Command(commands=["list_wallets"]))
async def handle_list_wallets(message: types.Message):
    await list_user_wallets(message)

# Define separate handler for removing a wallet
@router.message(Command(commands=["remove_wallet"]))
async def handle_remove_wallet(message: types.Message):
    args = message.text.split()[1:]
    if len(args) < 1:
        await message.answer("Please provide the wallet ID to remove.\nUsage: /remove_wallet <wallet_id>")
        return
    try:
        wallet_id = int(args[0])
    except ValueError:
        await message.answer("Invalid wallet ID. Please provide a valid integer.")
        return
    await remove_user_wallet(message, wallet_id)

# Define separate handlers for gas alerts
@router.message(Command(commands=["add_gas_alert"]))
async def handle_add_gas_alert(message: types.Message):
    args = message.text.split()[1:]
    if len(args) < 1:
        await message.answer("Please provide a gas price threshold.\nUsage: /add_gas_alert <threshold>")
        return
    try:
        threshold = float(args[0])
    except ValueError:
        await message.answer("Invalid threshold value. Please provide a valid number.")
        return
    await add_gas_alert(message, threshold)

@router.message(Command(commands=["list_gas_alerts"]))
async def handle_list_gas_alerts(message: types.Message):
    await list_gas_alerts(message)

@router.message(Command(commands=["remove_gas_alert"]))
async def handle_remove_gas_alert(message: types.Message):
    args = message.text.split()[1:]
    if len(args) < 1:
        await message.answer("Please provide the gas alert ID to remove.\nUsage: /remove_gas_alert <alert_id>")
        return
    try:
        alert_id = int(args[0])
    except ValueError:
        await message.answer("Invalid alert ID. Please provide a valid integer.")
        return
    await remove_gas_alert(message, alert_id)

# Include router in dispatcher
dp.include_router(router)

# Main function to run the bot
async def main():
    print("Bot is starting...")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())  # Use asyncio.run() to run the bot's async code
