from configparser import Interpolation
from random import shuffle
import time
import tensorflow as tf
from deepClassifier.entity import TrainingConfig
from pathlib import Path

class Training:

    def __init__(self,config:TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenrator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )

        dataflow_kwargs = dict(

            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.param_batch_size,
            interpolation = "bilinear"
        )

        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenrator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory = self.config.training_data_path,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            training_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2, # slitly tilt image
                zoom_range =  0.2,
                **datagenrator_kwargs
            )
        else:
            training_data_generator = valid_data_generator

        self.train_generator = valid_data_generator.flow_from_directory(
            directory = self.config.training_data_path,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs
        )


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epoch, 
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )


    