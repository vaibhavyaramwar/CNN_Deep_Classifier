from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classess: int

@dataclass(frozen=True)
class PrepareCallBackConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_file_path:  Path

@dataclass(frozen=True)
class PrepareCallBackConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_file_path:  Path


@dataclass(frozen=True)
class TrainingConfig:
      root_dir: Path
      trained_model_path: Path
      updated_base_model_path: Path
      training_data_path: Path
      params_epoch : int
      param_batch_size: int
      params_is_augmentation : bool
      params_image_size: list