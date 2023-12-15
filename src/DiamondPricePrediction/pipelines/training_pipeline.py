from src.DimondPricePrediction.components.data_ingestion import DataIngestion

import os, sys

from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException

import pandas as pd

obj = DataIngestion()

obj.initiate_data_ingestion()




