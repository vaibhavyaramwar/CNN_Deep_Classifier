import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utility/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",   
    "setup.py",
    "setup.cfg", # Required if we are creating python packages
    "pyproject.toml", # Required if we are creating python packages
    "tox.ini", # For Local testing
    "research/trials.ipynb",
]

for filepath in list_of_files:
    filePath = Path(filepath)
    filedir,filename = os.path.split(filePath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory : filedir : {filedir} for filename : {filename}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)):
        with open(filePath,"w") as file_obj:
            pass # Craete an Empty file
            logging.info(f"Creating empty File : {filePath}")
    else:
        logging.info(f"{filename} already exists")


