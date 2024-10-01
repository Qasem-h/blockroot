from loguru import logger
import sys

def init_logging(log_level: str):
    """Initialize logging configuration."""
    logger.remove()
    logger.add(sys.stderr, level=log_level)
    logger.info("Logging is set to level: {}", log_level)
