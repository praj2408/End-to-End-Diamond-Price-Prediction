
import pandas as pd 
import numpy as np
import sys
import os
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path



class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")



class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion initiated")
        
        try:
            
            data = pd.read_csv(Path(os.path.join("notebooks/data/gemstone.csv")))
            logging.info("Reading the dataset Completed")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw dataset in artifacts directory")
            
            logging.info("Performing train test split...")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train test split completed successfully")
            
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info("Data Ingestion completed successfully")
        
        except Exception as e:
            logging.info("Exception during occured at data ingestion stage")
            raise CustomException(e, sys)