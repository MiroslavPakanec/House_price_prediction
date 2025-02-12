import os
import argparse
import traceback
import numpy as np
from loguru import logger
from sklearn.linear_model import LinearRegression
from utils.data_utils import fit_transform
from utils.environment import Environment
from utils.os_utils import delete_file, save_model, save_scaler

def train(train_data_directory: str, output_directory: str, delete_input = False) -> None: 
    try:
        logger.info('[Training...]')
        x_train_path: str = os.path.join(train_data_directory, Environment().NP_X_TRAIN_FILENAME)
        y_train_path: str = os.path.join(train_data_directory, Environment().NP_Y_TRAIN_FILENAME)
        _validate(train_data_directory, x_train_path, y_train_path)
        
        x_train: np.ndarray = _load_numpy_array(x_train_path)
        y_train: np.ndarray = _load_numpy_array(y_train_path)
        
        x_train, scaler = fit_transform(x_train)
        model: LinearRegression = _get_trained_model(x_train, y_train)
        save_model(output_directory, Environment().MODEL_FILENAME, model)
        save_scaler(output_directory, Environment().SCALER_FILENAME, scaler)

        if delete_input:
            delete_file(x_train_path)
            delete_file(y_train_path)
        logger.info('[Done.]')
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())

def _validate(train_data_directory: str, x_train_path: str, y_train_path: str) -> None:
    train_directory_exists: bool = os.path.isdir(train_data_directory)
    train_x_exists: bool = os.path.isfile(x_train_path)
    train_y_exists: bool = os.path.isfile(y_train_path)
    if not train_directory_exists:
        raise ValueError(f'Training data directory at {train_data_directory} does not exist.')
    if not train_x_exists:
        raise ValueError(f'Training file {x_train_path} does not exist.')
    if not train_y_exists:
        raise ValueError(f'Training file {y_train_path} does not exist.')
    
def _load_numpy_array(path: str) -> np.ndarray: 
    logger.info(f'Loading array from {path}')
    data: np.ndarray = np.load(path)
    logger.info(f'Successfully loaded array from {path}. Shape: {data.shape}')
    return data

def _get_trained_model(x_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
    logger.info(f'Training model.')
    model = LinearRegression()
    model.fit(x_train, y_train)
    logger.info(f'Successfully trained linear regression model.')
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train linear regression model and save training artifacts.')
    parser.add_argument('-i', '--train_data_directory', type=str, required=True, help='Path to the input train data directory (containing relevant numpy files)')
    parser.add_argument('-o', '--output_directory', type=str, required=True, help='Path to the output directory, where training artifacts will be stored.')
    parser.add_argument('-d', '--delete-input', action='store_true', help='Delete the train numpy files after training.')
    args = parser.parse_args()
    train(args.train_data_directory, args.output_directory, args.delete_input)