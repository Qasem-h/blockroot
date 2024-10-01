from database.connection import engine
from database.base import Base
import sys
import os

# Adjust the path to include the project root
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


from modules.accounts.models import User
from modules.wallets.models import Wallet
from modules.alerts.models import GasAlert
from modules.subscription.models import Subscription

# Create all tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
