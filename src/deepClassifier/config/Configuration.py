from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utility import read_yaml_file, create_directories
from deepClassifier.entity import DataIngestionConfig


class ConfigManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, param_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml_file(config_file_path)
        self.param = read_yaml_file(param_file_path)
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            create_directories([config.root_dir])
            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_url,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir,
            )
            return data_ingestion_config
        except Exception as e:
            raise e
