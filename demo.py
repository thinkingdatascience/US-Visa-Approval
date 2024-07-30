from us_visa.logger import logging
from box.exceptions import BoxValueError

logging.info("Welcome to our custom log")

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise e
