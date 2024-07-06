import os
import json
import joblib
import argparse
import traceback
import numpy as np
from loguru import logger
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def evaluate(test_date_directory: str, model_directory: str, output_directory: str):
    try:
        logger.info('[Evaluating...]')
        x_test_path: str = os.path.join(test_date_directory, 'x_test.npy')
        y_test_path: str = os.path.join(test_date_directory, 'y_test.npy')
        model_path: str = os.path.join(model_directory, 'linear_regression_model.joblib')
        _validate(test_date_directory, x_test_path, y_test_path, model_path)

        x_test: np.ndarray = _load_numpy_array(x_test_path)
        y_test: np.ndarray = _load_numpy_array(y_test_path)
        model: LinearRegression = _load_model(model_path)
        
        rmse: float = _get_rmse(model, x_test, y_test)
        r2: float = _get_r2(model, x_test, y_test)
        _save_metrics(output_directory, rmse, r2)
        logger.info('[Done.]')
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())
    

def _validate(test_date_directory: str, x_test_path: str, y_test_path: str, model_path: str):
    test_directory_exists: bool = os.path.isdir(test_date_directory)
    test_x_exists: bool = os.path.isfile(x_test_path)
    test_y_exists: bool = os.path.isfile(y_test_path)
    model_exists: bool = os.path.isfile(model_path)
    if not test_directory_exists:
        raise ValueError(f'Testing data directory at {test_directory_exists} does not exist.')
    if not test_x_exists:
        raise ValueError(f'Testing file {test_x_exists} does not exist.')
    if not test_y_exists:
        raise ValueError(f'Testing file {test_y_exists} does not exist.')
    if not model_exists:
        raise ValueError(f'Model {model_path} does not exist.')
    
def _load_numpy_array(path: str) -> np.ndarray: 
    logger.info(f'Loading array from {path}')
    data: np.ndarray = np.load(path)
    logger.info(f'Successfully loaded array from {path}. Shape: {data.shape}')
    return data

def _load_model(path: str) -> LinearRegression:
    logger.info(f'Loading model from {path}')
    model: LinearRegression = joblib.load(path)
    return model

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

def _save_metrics(directory: str, rmse: float, r2: float) -> None:
    logger.info(f'Saving RMSE to {directory}')
    os.makedirs(directory, exist_ok=True)
    metrics_path: str = os.path.join(directory, 'metrics.json')
    metrics = {'rmse': rmse, 'r2': r2}
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f)
    logger.info(f'Successfully saved metrics to {metrics_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate model and save metrics.')
    parser.add_argument('-i', '--test_data_directory', type=str, required=True, help='Path to the train data directory (containing relevant numpy files).')
    parser.add_argument('-m', '--model_directory', type=str, required=True, help='Path to the model directory (containing trained model).')
    parser.add_argument('-o', '--output_directory', type=str, required=True, help='Path to the output directory, where evaluation metrics will be saved.')
    args = parser.parse_args()
    evaluate(args.test_data_directory, args.model_directory, args.model_directory)