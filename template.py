import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

list_of_files=[
    f"src/__init__.py",
    f"src/configuration/__init__.py",
    f"src/configuration/gcloud_syncer.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_evaluation.py",
    f"src/components/model_pusher.py",
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",
    f"src/entity/artifact_entity.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/train_pipeline.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/ml/__init__.py",
    f"src/ml/model.py",
    f"src/logger.py",
    f"src/exception.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    ".dockerignore"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)
    
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory {file_dir} for file {file_name}")
        
    if not (os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as file:
            pass
            logging.info(f"created empty file {filepath}")
    else:
        logging.info(f"{file_name} file already exists")