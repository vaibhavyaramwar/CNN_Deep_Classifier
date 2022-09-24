import logging
from urllib import request
import os 
from zipfile import ZipFile

from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier import utility
from pathlib import Path
from tqdm import tqdm

class DataIngestion:

    def __init__(self,config:DataIngestionConfig):
        self.config = config


    def download_files(self):
        logger.info(f"Downloading of file started for url : {self.config.source_url}")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download Started")
            fileName, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"File Download is Successful and filename : {fileName} \info of file : {headers}")
        else:
            logger.info(f"File Alfready exist in location : {self.config.local_data_file} and having size : {utility.get_size(Path(self.config.local_data_file))}")

    def _get_updated_list_of_files(self,list_of_files):
        logger.info(f"list_of_files : {list_of_files}")
        return [f for f in list_of_files if f.endswith(".jpg") and ('Cat' in f or 'Dog' in f)]

    def _preprocess(self,zf:ZipFile,f:str,working_dir:str):
        target_file_path = os.path.join(working_dir,f)
        logger.info(f"target_file_path  ; {target_file_path }")

        if not os.path.exists(target_file_path):
            zf.extract(f,working_dir)
            logger.info(f"ERxtracting File : {target_file_path}")

        if os.path.getsize(target_file_path) == 0:
            os.remove(target_file_path)
            logger.info(f"Removing File : {target_file_path}")

    def unzip_with_clean(self):
        try:
            with ZipFile(file=self.config.local_data_file,mode="r") as zf:
                logger.info("Unziping the file")
                list_of_files = zf.namelist()
                updated_list_of_files = self._get_updated_list_of_files(list_of_files)
                logger.info(updated_list_of_files)
                for f in tqdm(updated_list_of_files):
                    self._preprocess(zf,f,self.config.unzip_dir)
                logger.info("Unziping the file Successful")
        except Exception as e:
            raise e

