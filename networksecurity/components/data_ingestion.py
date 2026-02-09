from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import pandas as pd
import numpy as np
import pymongo
import os
import sys
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
import certifi

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if not MONGO_DB_URL:
    raise ValueError("MONGO_DB_URL not found in environment variables")

# TLS certificate for MongoDB Atlas
ca = certifi.where()


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=ca,
                serverSelectionTimeoutMS=5000
            )

            # Validate MongoDB connection
            self.mongo_client.admin.command("ping")
            logger.info("Connected to MongoDB Atlas successfully")

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            # Drop MongoDB ObjectId
            if "_id" in df.columns:
                df = df.drop(columns=["_id"])

            # Replace "na" strings with NaN
            df.replace({"na": np.nan}, inplace=True)

            logger.info("Exported MongoDB collection to DataFrame")
            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)

            os.makedirs(dir_path, exist_ok=True)

            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logger.info("Feature store data saved successfully")

            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
            )

            train_dir = os.path.dirname(self.data_ingestion_config.training_file_path)
            test_dir = os.path.dirname(self.data_ingestion_config.testing_file_path)

            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False,
                header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False,
                header=True
            )

            logger.info("Train-test split completed successfully")

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

            logger.info("Data ingestion completed successfully")
            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
