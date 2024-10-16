from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard():
    # Main menu buttons
    buttons = [
        [KeyboardButton(text="Add"), KeyboardButton(text="Edit")],
        [KeyboardButton(text="Watchlists"), KeyboardButton(text="Subscription")],
        [KeyboardButton(text="Settings")]
    ]
    
    # Create the keyboard markup
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
