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

def get_experiment_directory_path(experiment_name: str) -> str:
    return os.path.join(Environment().EXPERIMENTS_TARGET_PATH, experiment_name)

def get_experiment_preprocessed_filepath(experiment_name: str) -> str:
    experiment_path: str = get_experiment_directory_path(experiment_name)
    return os.path.join(experiment_path, Environment().PREROCESSING_FILENAME)
