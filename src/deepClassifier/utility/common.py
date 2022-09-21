from cmath import e
import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from pathlib import Path
from deepClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any

@ensure_annotations
def read_yaml_file(file_path) -> ConfigBox:
    '''
        reads yaml file and returns
            Args:
                path_to_yaml (str): path like input
            Raises:
                ValueError: if yaml file is empty
                e: empty file
            Returns:
                ConfigBox: ConfigBox type
    
    '''
    try:
        with open(file_path) as file_obj:
            yaml_file = yaml.safe_load(file_obj)
            logger.log(f"yaml file : {file_path} loaded Successfully")
            return ConfigBox(yaml_file)
    except BoxValueError as bv:
        logger.log("Value Error , yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    '''
        iterate the path list and create directories for given path

        Args:
            path_to_directories (list): list of path of directories
            ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    '''
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logger.info(f"Created Directory at Path : {path}")
    except Exception as e:
        raise e

@ensure_annotations
def save_json(path:Path,data:dict):
    """
        save json data
        Args:
            path (Path): path to json file
            data (dict): data to be saved in json file
    """
    try:
        with open(path,"w") as file_data:
            json.dump(data,file_data,indent=4)

        logger.info(f"Json file saved at path : {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_json(path:Path) ->ConfigBox:

    '''
    load json files data
        Args:
            path (Path): path to json file
        Returns:
            ConfigBox: data as class attributes instead of dict
    '''

    try:
        with open(path,"r") as file_obj:
            content = json.loads(path)
        
        logger.info(f"Json file loaded Successfully : {path}")
        return ConfigBox(content)
    except Exception as e:
        raise e


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"