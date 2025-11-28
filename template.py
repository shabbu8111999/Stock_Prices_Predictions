import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "stocks_project"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/config.py",
    f"{project_name}/data_loader.py",
    f"{project_name}/features.py",
    f"{project_name}/model_ml.py",
    f"{project_name}/model_dl.py",
    f"{project_name}/realtime.py",
    "setup.py",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")