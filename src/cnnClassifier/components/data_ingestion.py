import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
                os.makedirs("artifacts/data_ingestion", exist_ok=True)

                # Use source_URL from config instead of undefined dataset_url
                file_id = self.config.source_URL.split("/")[-2]
                prefix = 'https://drive.google.com/file/d/'
                gdown.download(prefix + file_id+"/view?usp=sharing", output=str(self.config.local_data_file))
            else:
                logger.info(f"File already exists at {self.config.local_data_file}")
        except Exception as e:
            logger.exception(f"An error occurred during file download: {e}")

    def unzip_and_get_size(self):
        try:
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)

            data_size = get_size(self.config.unzip_dir)
            logger.info(f"Unzipped data size: {data_size}")
        except Exception as e:
            logger.exception(f"An error occurred during unzip: {e}")
