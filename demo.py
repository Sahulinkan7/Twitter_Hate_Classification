from src.logger import logging
import os,sys
from src.exception import CustomException
logging.info(f"hello")

try:
    c=3/0
except Exception as e:
    logging.error(f"error is {CustomException(e,sys)}")
    raise CustomException(e,sys)