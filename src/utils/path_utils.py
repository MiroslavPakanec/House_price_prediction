import os
from typing import Tuple
from utils.environment import Environment


def get_model_path(experiment_name: Tuple[str, None]) -> str:
    if experiment_name is None:
        return Environment().MODEL_PATH
    return os.path.join('./experiments', experiment_name, Environment().MODEL_FILENAME)

def get_scaler_path(experiment_name: Tuple[str, None]) -> str:
    if experiment_name is None:
        return Environment().SCALER_PATH
    return os.path.join('./experiments', experiment_name, Environment().SCALER_FILENAME)