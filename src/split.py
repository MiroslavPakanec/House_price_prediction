import os
import argparse
import traceback
from typing import Tuple
import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def split(input_data_path: str, output_directory: str, test_size: float, delete_input = False) -> None: 
    try:
        logger.info('[Spliting dataset...]')
        _validate(input_data_path, test_size)
        data: DataFrame = _load_input_data(input_data_path)
        x_train, y_train, x_test, y_test = _get_split_data(data, test_size)
        _save_numpy_array(output_directory, 'x_train.npy', x_train)
        _save_numpy_array(output_directory, 'y_train.npy', y_train)
        _save_numpy_array(output_directory, 'x_test.npy', x_test)
        _save_numpy_array(output_directory, 'y_test.npy', y_test)
        if delete_input:
            _delete_input_file(input_data_path)
        logger.info('[Done.]')
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())

def _validate(input_data_path: str, test_size: float) -> None:
    input_path_exists: bool = os.path.isfile(input_data_path)
    input_path_is_csv: bool = input_data_path.endswith('.csv')
    is_test_size_valid: bool = 0 <= test_size < 1
    if not input_path_is_csv:
        raise ValueError(f'Input data path {input_data_path} is not a CSV file.')
    if not input_path_exists:
        raise ValueError(f'Input data path {input_data_path} does not exist.')  
    if not is_test_size_valid:
        raise ValueError(f'Test size ({test_size}) must be between 0 and 1 (non-inclusive).')  

def _load_input_data(input_data_path: str) -> DataFrame:
    logger.info(f'Loading preprocessed input data from {input_data_path}')
    data: DataFrame = pd.read_csv(input_data_path, sep=',')
    logger.info(f'Successfully loaded preprocessed input data. Shape: {data.shape}')
    return data

def _save_numpy_array(directory: str, filename: str, data: np.ndarray) -> None:
    logger.info(f'Saving {filename} to {directory}')
    os.makedirs(directory, exist_ok=True)
    output_data_path: str = os.path.join(directory, filename)
    np.save(output_data_path, data)

def _get_split_data(data: DataFrame, test_size: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    logger.info(f'Spliting data (train size: {(1-test_size)*100}%, test_size: {test_size * 100}%).')
    xs: DataFrame = data.drop(['median_house_value'], axis=1)
    xs: np.ndarray = xs.to_numpy()
    xs: np.ndarray = _normilize(xs)
    ys = data['median_house_value']
    ys = ys.to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(xs, ys, test_size=test_size)
    logger.info('Successfuly split preprocessed data.')
    logger.info(f'Train X shape: {x_train.shape}')
    logger.info(f'Train Y shape: {y_train.shape}')
    logger.info(f'Test X shape: {x_test.shape}')
    logger.info(f'Test Y shape: {y_test.shape}')
    return x_train, y_train, x_test, y_test

def _delete_input_file(input_data_path: str) -> None:
    try:
        os.remove(input_data_path)
        logger.info(f'Successfully deleted file at {input_data_path}')
    except OSError as e:
        logger.error(f'Error deleting file at {input_data_path}')
        logger.debug(e)

def _normilize(data: np.ndarray) -> np.ndarray:
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split processed data and results to an output directory.')
    parser.add_argument('-i', '--input_data_path', type=str, required=True, help='Path to the preprocessed input data file (numpy file)')
    parser.add_argument('-o', '--output_directory', type=str, required=True, help='Directory to save the output train and test files')
    parser.add_argument('-s', '--test-size', type=float, required=True, default=0.2, help='Size of the test set (value should be between 0 and 1)')
    parser.add_argument('-d', '--delete-input', action='store_true', help='Delete the input file after splitting.')
    args = parser.parse_args()
    split(args.input_data_path, args.output_directory, args.test_size, args.delete_input)