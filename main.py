from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        logger.info("Starting Training Pipeline")

        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)

        data_ingestion = DataIngestion(dataingestionconfig)

        logger.info("Initiating Data Ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logger.info("Data Ingestion Completed")

        print(dataingestionartifact)

    except NetworkSecurityException as e:
        logger.error(str(e))
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
