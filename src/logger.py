import logging
from datetime import datetime
import os

file_name=f"log_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

log_file_path=os.path.join(logs_path,file_name)

logging.basicConfig(filename=log_file_path,
                    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
