import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("telegram_bot")
    return logger
