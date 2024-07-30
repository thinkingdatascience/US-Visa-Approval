import logging
import os


# Logging Format
logging_str = "[%(asctime)s: %(levelname)s: [%(module)s]: %(message)s]"

# Creating a folder for logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, "running_logs.log")


logging.basicConfig(
    level=logging.INFO, format=logging_str, handlers=[logging.FileHandler(log_filepath)]
)

logger = logging.getLogger("USVisaPrediction")
