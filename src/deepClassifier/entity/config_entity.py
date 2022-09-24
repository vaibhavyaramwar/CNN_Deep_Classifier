from dataclasses import dataclass
from pathlib import Path
import pathlib

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: pathlib
    source_url: str
    local_data_file: pathlib
    unzip_dir: pathlib
