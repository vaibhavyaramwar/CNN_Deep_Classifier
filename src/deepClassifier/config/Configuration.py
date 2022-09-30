from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utility import read_yaml_file, create_directories
from deepClassifier.entity import DataIngestionConfig,PrepareBaseModelConfig,PrepareCallBackConfig,TrainingConfig

from pathlib import Path
import os

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

        
    def get_prepare_basemodel_config(self) -> PrepareBaseModelConfig:
        try:
            config = self.config.prepare_base_model
            param_config = self.param
            create_directories([config.root_dir])
            prepare_Base_Model_Config =   PrepareBaseModelConfig(
                root_dir = Path(config.root_dir),
                base_model_path = Path(config.base_model_path),
                updated_base_model_path = Path(config.updated_base_model_path),
                params_image_size = param_config.IMAGE_SIZE,
                params_learning_rate = param_config.LEARNING_RATE,
                params_include_top = param_config.INCLUDE_TOP,
                params_weights = param_config.WEIGHTS,
                params_classess = param_config.CLASSESS
            )
            return prepare_Base_Model_Config
        except Exception as e:
            raise e

        
    def get_prepare_callback_config(self) -> PrepareCallBackConfig:
        try:
            config = self.config.prepare_callbacks
            param_config = self.param
            checkpoint_model_dir = os.path.dirname(config.checkpoint_model_file_path)
            create_directories([Path(config.tensorboard_root_log_dir),Path(checkpoint_model_dir)])
            prepare_call_backConfig =   PrepareCallBackConfig(
                                            root_dir = Path(config.root_dir),
                                            tensorboard_root_log_dir = Path(config.tensorboard_root_log_dir),
                                            checkpoint_model_file_path = Path(config.checkpoint_model_file_path)
                                        )
            return prepare_call_backConfig
        except Exception as e:
            raise e

    def get_training_config(self) -> TrainingConfig:
        try:
            config = self.config.training
            create_directories([Path(config.root_dir)])

            trainingConfig = TrainingConfig(
                root_dir = Path(config.root_dir),
                trained_model_path = Path(config.trained_model_path),
                updated_base_model_path = Path(self.config.prepare_base_model.updated_base_model_path),
                training_data_path = Path(os.path.join(self.config.data_ingestion.unzip_dir,"PetImages")),
                params_epoch = self.param.EPOCHS,
                param_batch_size = self.param.BATCH_SIZE,
                params_is_augmentation = self.param.AUGUMENTATION,
                params_image_size = self.param.IMAGE_SIZE
            )

            return trainingConfig
        except Exception as e:
            raise e
    