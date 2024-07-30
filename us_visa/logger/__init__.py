import logging
import os
from from_root import from_root


# Logging Format
logging_str = "[%(asctime)s: %(levelname)s: [%(module)s]: %(message)s]"

# Creating a folder for logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(from_root(), log_dir, "running_logs.log")


logging.basicConfig(
    level=logging.INFO, format=logging_str, handlers=[logging.FileHandler(log_filepath)]
)

logger = logging.getLogger("USVisaPrediction")
