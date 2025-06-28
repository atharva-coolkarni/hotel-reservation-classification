import os
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.file_path = FILE_PATH
        self.config = config["data_ingestion"]
        self.train_test_ratio = self.config["train_ratio"]
        
        os.makedirs(RAW_DIR, exist_ok=True)
        
        logger.info("DataIngestion initialized with file path: %s", self.file_path)
        
    def split_data(self):
        """
        Splits the dataset into training and testing sets.
        """
        try:
            # Read the dataset
            logger.info("Loading dataset from %s", self.file_path)
            df = pd.read_csv(self.file_path)
            logger.info("Dataset loaded successfully from %s", self.file_path)
            
            # Split the dataset
            train_df, test_df = train_test_split(df, train_size=self.train_test_ratio, random_state=42)
            logger.info("Data split into training and testing sets with ratio: %s", self.train_test_ratio)
            
            # Save the datasets
            train_file_path = os.path.join(RAW_DIR, "train.csv")
            test_file_path = os.path.join(RAW_DIR, "test.csv")
            train_df.to_csv(train_file_path, index=False)
            test_df.to_csv(test_file_path, index=False)
            
            logger.info("Training data saved to %s and testing data saved to %s", train_file_path, test_file_path)
            
        except Exception as e:
            logger.error("Error during data splitting")
            raise CustomException(f"Data ingestion failed: {str(e)}", sys)
        
    def run(self):
        """
        Runs the data ingestion process.
        """
        try:
            logger.info("Starting data ingestion process")
            self.split_data()            
        except Exception as e:
            logger.error("CustomException ",str(e))
            raise CustomException(f"Data ingestion failed: {str(e)}", sys)
        finally:
            logger.info("Data ingestion process completed successfully")
    
if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()