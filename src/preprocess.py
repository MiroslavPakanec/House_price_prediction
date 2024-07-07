import os
import argparse
import traceback
import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame
from utils.os_utils import load_csv_file, save_csv_file

def preprocess(input_data_path: str, output_data_path: str) -> None: 
    try:
        logger.info('[Preprocessing...]')
        _validate(input_data_path, output_data_path)
        data: DataFrame = load_csv_file(input_data_path)
        data: DataFrame = get_preprocessed_data(data)
        save_csv_file(output_data_path, data)
        logger.info('[Done.]')
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())

def get_preprocessed_data(data: DataFrame) -> DataFrame:
    logger.info(f'Processing data.')
    data = data.dropna()
    data = _set_ocean_proximity_as_ohe(data)
    data['total_rooms'] = np.log(data['total_rooms'] + 1)
    data['total_bedrooms'] = np.log(data['total_bedrooms'] + 1)
    data['population'] = np.log(data['population'] + 1)
    data['households'] = np.log(data['households'] + 1)
    data['bedroom_ratio'] = data['total_bedrooms'] / data['total_rooms']
    data['household_rooms'] = data['total_rooms'] / data['households']
    data = _convert_boolean_columns(data)
    logger.info(f'Successfully processed data. Shape: {data.shape}')
    return data
        
def _validate(input_data_path: str, output_data_path: str) -> None:
    input_path_exists: bool = os.path.isfile(input_data_path)
    input_path_is_csv: bool = input_data_path.endswith('.csv')
    output_path_is_csv: bool = output_data_path.endswith('.csv')
    if not input_path_is_csv:
        raise ValueError(f'Input data path {input_data_path} is not a CSV file.')
    if not input_path_exists:
        raise ValueError(f'Input data path {input_data_path} does not exist.')
    if not output_path_is_csv:
        raise ValueError(f'Oputput data path {output_data_path} is not a CSV file.')        

def _set_ocean_proximity_as_ohe(data: DataFrame) -> DataFrame:
    ocean_proximity_categories = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
    for category in ocean_proximity_categories:
        if category not in data['ocean_proximity'].unique():
            data[category] = 0

    ocean_proximity_ohe = pd.get_dummies(data['ocean_proximity']) 
    data = data.join(ocean_proximity_ohe)
    data = data.drop(columns=['ocean_proximity'])
    return data

def _convert_boolean_columns(data: DataFrame) -> DataFrame:
    bool_cols = data.select_dtypes(include=['bool']).columns
    data[bool_cols] = data[bool_cols].astype(int)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess raw data and save to a specified output directory.')
    parser.add_argument('-i', '--input_data_path', type=str, required=True, help='Path to the raw input data file (CSV format)')
    parser.add_argument('-o', '--output_data_path', type=str, required=True, help='Path to the output directory and filename (CSV format) to save preprocessed data')
    args = parser.parse_args()
    preprocess(args.input_data_path, args.output_data_path)