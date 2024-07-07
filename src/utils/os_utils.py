
import os
import json
import joblib
import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def save_scaler(directory: str, filename: str, scaler: StandardScaler) -> None:
    logger.info(f'Saving scaler to {directory}')
    os.makedirs(directory, exist_ok=True)
    scaler_path: str = os.path.join(directory, f'{filename}.joblib')
    joblib.dump(scaler, scaler_path)
    logger.info(f'Successfully saved the scaler to {scaler_path}')

def save_model(directory: str, filename: str, model: LinearRegression) -> None:
    logger.info(f'Saving model to {directory}')
    os.makedirs(directory, exist_ok=True)
    model_path: str = os.path.join(directory, f'{filename}.joblib')
    joblib.dump(model, model_path)
    logger.info(f'Successfully saved the model to {model_path}')

def save_numpy_array(directory: str, filename: str, data: np.ndarray) -> None:
    logger.info(f'Saving {filename}.npy to {directory}')
    os.makedirs(directory, exist_ok=True)
    output_data_path: str = os.path.join(directory, f'{filename}.npy')
    np.save(output_data_path, data)
    
def save_metrics(directory: str, filename: str, rmse: float, r2: float) -> None:
    logger.info(f'Saving RMSE to {directory}')
    os.makedirs(directory, exist_ok=True)
    metrics_path: str = os.path.join(directory, f'{filename}.json')
    metrics = {'rmse': rmse, 'r2': r2}
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f)
    logger.info(f'Successfully saved metrics to {metrics_path}')

def save_csv_file(filepath: str, data: DataFrame) -> None:
    logger.info(f'Saving csv data to {filepath}')
    output_data_dir: str = os.path.dirname(filepath)
    os.makedirs(output_data_dir, exist_ok=True)
    data.to_csv(filepath, index=False)
    logger.info(f'Successfully saved csv file to {filepath}.')

def load_scaler(path: str) -> StandardScaler:
    logger.info(f'Loading scaler from {path}')
    scaler: StandardScaler = joblib.load(path)
    return scaler

def load_model(path: str) -> LinearRegression:
    logger.info(f'Loading model from {path}')
    model: LinearRegression = joblib.load(path)
    return model

def load_numpy_array(path: str) -> np.ndarray: 
    logger.info(f'Loading array from {path}')
    data: np.ndarray = np.load(path)
    logger.info(f'Successfully loaded array from {path}. Shape: {data.shape}')
    return data

def load_csv_file(filepath: str) -> DataFrame:
    logger.info(f'Loading csv file from {filepath}')
    data: DataFrame = pd.read_csv(filepath, sep=',')
    logger.info(f'Successfully loaded data from {filepath}. Shape: {data.shape}')
    return data

def delete_file(path: str) -> None:
    try:
        os.remove(path)
        logger.info(f'Successfully deleted file at {path}')
    except OSError as e:
        logger.error(f'Error deleting file at {path}')
        logger.debug(e)

