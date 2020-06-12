import logging

from app.constants import LOG_LEVEL


# Console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)

logging.basicConfig(level=LOG_LEVEL, handlers=[console_handler])
