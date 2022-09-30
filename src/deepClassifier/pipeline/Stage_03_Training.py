from deepClassifier.config.Configuration import ConfigManager
from deepClassifier import logger
from deepClassifier.components import PrepareCallBack,Training

STAGE_NAME = "PrepareBase Model Stage"


try:
    config = ConfigManager()
    prepare_callbacks_config = config.get_prepare_callback_config()
    prepare_callbacks = PrepareCallBack(prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
    
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(
        callback_list=callback_list
    )
    
except Exception as e:
    raise e