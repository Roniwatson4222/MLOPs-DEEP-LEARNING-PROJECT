from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion

from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_and_get_size()
            logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
        except Exception as e:
            logger.exception(f"An error occurred in stage {STAGE_NAME}: {e}")   


if __name__ == "__main__":
    obj = DataIngestionTrainingPipeline()
    obj.main()