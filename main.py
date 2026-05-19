from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f"stage {STAGE_NAME} started")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(f"An error occurred in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Prepare Base Model Stage"
try: 
    logger.info(f"stage {STAGE_NAME} started")
    from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
    prepare_base_model=PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(f"An error occurred in stage {STAGE_NAME}: {e}")
    raise e   

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e