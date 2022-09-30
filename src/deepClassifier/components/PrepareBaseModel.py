from deepClassifier.entity import PrepareBaseModelConfig
import tensorflow as tf
from pathlib import Path 

class PrepareBaseModel:

    def __init__(self,config:PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top= self.config.params_include_top, 
            # Use only CNN layer VGG16 and exclude fully connected layer of VGG16 if its False
        )

        self.save_model(self.config.base_model_path,self.model)

    @staticmethod
    def _prepare_full_model(model,classess,freeze_all,freeze_till,learning_rate_1):
        
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classess,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(optimizer="SGD" ,
                            loss = "categorical_crossentropy",metrics=["accuracy"])

        full_model.summary()
        return full_model


    def update_base_model(self):
        prepare_full_model = self._prepare_full_model(
                                model = self.model,
                                classess = self.config.params_classess,
                                freeze_all = True,
                                freeze_till = None,
                                learning_rate_1 = self.config.params_learning_rate
                            )

        self.save_model(path=self.config.updated_base_model_path,model=prepare_full_model)

    @staticmethod
    def save_model(path:Path,model):
        model.save(path)