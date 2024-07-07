import os
import argparse
import traceback
import numpy as np
from loguru import logger
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from utils.data_utils import transform
from utils.environment import Environment
from utils.os_utils import delete_file, load_model, load_numpy_array, load_scaler, save_metrics

def evaluate(test_data_directory: str, model_directory: str, output_directory: str, delete_input = False):
    logger.info('[Evaluating...]')
    x_test_path: str = os.path.join(test_data_directory, Environment().NP_X_TEST_FILENAME)
    y_test_path: str = os.path.join(test_data_directory, Environment().NP_Y_TEST_FILENAME)
    model_path: str = os.path.join(model_directory, Environment().MODEL_FILENAME)
    scaler_path: str = os.path.join(model_directory, Environment().SCALER_FILENAME)
    _validate(test_data_directory, x_test_path, y_test_path, model_path, scaler_path)

    x_test: np.ndarray = load_numpy_array(x_test_path)
    y_test: np.ndarray = load_numpy_array(y_test_path)
    model: LinearRegression = load_model(model_path)
    scaler: LinearRegression = load_scaler(scaler_path)
    x_test: np.ndarray = transform(x_test, scaler)

    rmse: float = _get_rmse(model, x_test, y_test)
    r2: float = _get_r2(model, x_test, y_test)
    save_metrics(output_directory, Environment().METRICS_FILENAME, rmse, r2)

    if delete_input:
        delete_file(x_test_path)
        delete_file(y_test_path)
    logger.info('[Done.]')    

def _validate(test_date_directory: str, x_test_path: str, y_test_path: str, model_path: str, scaler_path: str):
    test_directory_exists: bool = os.path.isdir(test_date_directory)
    test_x_exists: bool = os.path.isfile(x_test_path)
    test_y_exists: bool = os.path.isfile(y_test_path)
    model_exists: bool = os.path.isfile(model_path)
    scaler_exists: bool = os.path.isfile(scaler_path)
    if not test_directory_exists:
        raise ValueError(f'Testing data directory at {test_directory_exists} does not exist.')
    if not test_x_exists:
        raise ValueError(f'Testing file {test_x_exists} does not exist.')
    if not test_y_exists:
        raise ValueError(f'Testing file {test_y_exists} does not exist.')
    if not model_exists:
        raise ValueError(f'Model {model_path} does not exist.')
    if not scaler_exists:
        raise ValueError(f'Scaler {scaler_path} does not exist.')
    
def _get_rmse(model: LinearRegression, x_test: np.ndarray, y_test: np.ndarray) -> float:
    logger.info('Calculating RMSE.')
    y_test_pred: np.ndarray = model.predict(x_test)
    rmse: float = np.sqrt(mean_squared_error(y_test, y_test_pred))
    logger.info(f'Calculated RMSE score: {rmse}')
    return rmse

def _get_r2(model: LinearRegression, x_test: np.ndarray, y_test: np.ndarray) -> float:
    logger.info('Calculating R2 score.')
    r2 = model.score(x_test, y_test)
    logger.info(f'Calculated R2 score: {r2}')
    return r2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate model and save metrics.')
    parser.add_argument('-i', '--test_data_directory', type=str, required=True, help='Path to the train data directory (containing relevant numpy files).')
    parser.add_argument('-m', '--model_directory', type=str, required=True, help='Path to the model directory (containing trained model).')
    parser.add_argument('-o', '--output_directory', type=str, required=True, help='Path to the output directory, where evaluation metrics will be saved.')
    parser.add_argument('-d', '--delete-input', action='store_true', help='Delete the test numpy files after evaluating.')
    args = parser.parse_args()
    
    try:
        evaluate(args.test_data_directory, args.model_directory, args.model_directory, args.delete_input)
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())