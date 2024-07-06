import os
import joblib
import argparse
import traceback
import numpy as np
from loguru import logger
from sklearn.linear_model import LinearRegression

def train(train_data_directory: str, output_directory: str, delete_input = False) -> None: 
    try:
        x_train_path: str = os.path.join(train_data_directory, 'x_train.npy')
        y_train_path: str = os.path.join(train_data_directory, 'y_train.npy')
        _validate(train_data_directory, x_train_path, y_train_path)
        
        x_train: np.ndarray = _load_numpy_array(x_train_path)
        y_train: np.ndarray = _load_numpy_array(y_train_path)
        model: LinearRegression = _get_trained_model(x_train, y_train)
        _save_model(output_directory, model)
        
        if delete_input:
            _delete_input_files(x_train_path, y_train_path)
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

def _save_model(directory: str, model: LinearRegression) -> None:
    logger.info(f'Saving to {directory}')
    os.makedirs(directory, exist_ok=True)
    model_path: str = os.path.join(directory, 'linear_regression_model.joblib')
    joblib.dump(model, model_path)
    logger.info(f'Successfully saved the model to {model_path}')

def _delete_input_files(x_train_path: str, y_train_path: str) -> None:
    try:
        os.remove(x_train_path)
        os.remove(y_train_path)
        logger.info(f'Successfully deleted files at:')
        logger.info(x_train_path)
        logger.info(y_train_path)
    except OSError as e:
        logger.error(f'Error deleting file at {x_train_path}, {y_train_path}')
        logger.debug(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train linear regression model and save training artifacts.')
    parser.add_argument('-i', '--train_data_directory', type=str, required=True, help='Path to the input train data directory (containing relevant numpy files)')
    parser.add_argument('-o', '--output_directory', type=str, required=True, help='Path to the output directory, where training artifacts will be stored.')
    parser.add_argument('-d', '--delete-input', action='store_true', help='Delete the input files after training.')
    args = parser.parse_args()
    train(args.train_data_directory, args.output_directory, args.delete_input)