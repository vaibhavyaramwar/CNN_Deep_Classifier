from deepClassifier.config.Configuration import ConfigManager
from deepClassifier.components.DataIngestion import DataIngestion
from deepClassifier import logger
from pathlib import Path

STAGE_NAME = "Data Ingestion Stage"


def main():
    config = ConfigManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_files()
    data_ingestion.unzip_with_clean()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>> Stage {STAGE_NAME} Started <<<<<")
        main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
