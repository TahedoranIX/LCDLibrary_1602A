from .lcd import LCD
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

console_handler = logging.StreamHandler()  # sends output to stderr
console_handler.setFormatter(logging.Formatter("[%(name)s] %(message)s"))
logger.addHandler(console_handler)
