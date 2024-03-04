from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.Stage_01_data_injestion import DataIngestionTraningPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>>")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed >>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e