from src.DiamondPricePrediction.components.data_ingestion import DataIngestion

import os, sys

from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException

import pandas as pd

obj = DataIngestion()

obj.initiate_data_ingestion()




