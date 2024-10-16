import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetching URL values from .env for future use
WEBSITE_URL = os.getenv("WEBSITE_URL")
YOUTUBE_URL = os.getenv("YOUTUBE_URL")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
