from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    # Create the main menu buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Add"), KeyboardButton("✏️ Edit"))
    keyboard.add(KeyboardButton("👤 Watchlists"), KeyboardButton("💳 Subscription"))
    return keyboard

def get_add_menu():
    # Create the add menu buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Add Coin"), KeyboardButton("👛 Add Wallet"))
    keyboard.add(KeyboardButton("🏊 Add Pool"), KeyboardButton("⛽ Add Gas Prices"))
    return keyboard

def get_edit_menu():
    # Create the edit menu buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Edit Coin"), KeyboardButton("👛 Edit Wallet"))
    keyboard.add(KeyboardButton("🏊 Edit Pool"), KeyboardButton("⛽ Edit Gas Prices"))
    return keyboard


def get_profile_menu():
    # Create the profile management menu buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("➕ Add Watchlist"), KeyboardButton("❌ Remove Watchlist"))
    keyboard.add(KeyboardButton("👁 Show All Watchlists"))
    return keyboard

def get_subscription_menu():
    # Create the subscription menu buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💼 Subscription Plans"))
    return keyboard
