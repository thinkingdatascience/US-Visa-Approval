import yaml
import dill
import numpy as np
import os
from pandas import DataFrame

import sys
from us_visa.logger import logging
from us_visa.exception import USVisaException


# Read YAML file
def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info(f" File loaded with filepath: {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USVisaException(e, sys)


# Write YAML file
def write_yaml_file(file_path: str, content: object, replace: bool = False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "w") as yaml_file:
            yaml.dump(content, yaml_file)

    except Exception as e:
        raise USVisaException(e, sys)


# Load Numpy array file
def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, "rb") as np_file:
            return np.load(np_file)
    except Exception as e:
        raise USVisaException(e, sys)


# Save Numpy array file
def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as np_file:
            np.save(np_file, array)
    except Exception as e:
        raise USVisaException(e, sys)


# Load Object
def load_object(file_path: str) -> object:
    logging.info("Entered the load object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
            logging.info("Exited the load object method of utils")
            return obj
    except Exception as e:
        raise USVisaException(e, sys)


# Save Object
def save_object(file_path: str, obj: object):
    logging.info("Entered the save object method of utils")
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            logging.info("Exited the save object method of utils")

    except Exception as e:
        raise USVisaException(e, sys)


# Drop Columns
def drop_columns(data: DataFrame, columns: list) -> DataFrame:

    logging.info("Entered drop column method of utils")

    try:
        data = data.drop(columns=columns, axis=1)
        logging.info("Exited drop column method of utils")
        return data

    except Exception as e:
        raise USVisaException(e, sys)
