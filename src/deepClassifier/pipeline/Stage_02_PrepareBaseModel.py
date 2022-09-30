from deepClassifier.config.Configuration import ConfigManager
from deepClassifier.components.PrepareBaseModel import PrepareBaseModel
from deepClassifier import logger

STAGE_NAME = "PrepareBase Model Stage"


try:
    config = ConfigManager()
    prepareBaseModel = PrepareBaseModel(config.get_prepare_basemodel_config())
    prepareBaseModel.get_base_model()
    prepareBaseModel.update_base_model()
except Exception as e:
    raise e