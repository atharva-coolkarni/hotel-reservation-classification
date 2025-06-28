import os
import sys
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml


logger = get_logger(__name__)
def read_yaml(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"YAML file not found at {file_path}")
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            logger.info(f"Successfully read YAML file: {file_path}")
            return config
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise CustomException(f"Failed to read YAML file: {file_path}", e)