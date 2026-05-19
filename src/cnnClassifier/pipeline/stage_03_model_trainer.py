from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        logger.info("Initializing ModelTrainingPipeline...")

    def main(self):
        try:
            logger.info("Fetching training configuration...")
            config = ConfigurationManager()
            training_config = config.get_training_config()

            logger.info("Initializing Training class...")
            training = Training(config=training_config)

            logger.info("Loading base model...")
            training.get_base_model()

            logger.info("Preparing data generators...")
            training.train_valid_generator()

            logger.info("Starting model training...")
            training.train()

            logger.info("Model training completed successfully.")
        except Exception as e:
            logger.exception("An error occurred in ModelTrainingPipeline.main():")
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
