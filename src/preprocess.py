import os
import argparse
import traceback
import numpy as np
import pandas as pd
from loguru import logger
from pandas import DataFrame

def preprocess(input_data_path: str, output_data_path: str) -> None: 
    try:
        data: DataFrame = _load_input_data(input_data_path)
        data: DataFrame = _get_preprocessed_data(data)
        _save_preprocessed_data(output_data_path, data)
        logger.info('[Done.]')
    except Exception as e:
        logger.info(e)
        logger.debug(traceback)
        logger.debug(e)
        
def _load_input_data(input_data_path: str) -> DataFrame:
    logger.info(f'Loading raw input data from {input_data_path}')
    data: DataFrame = pd.read_csv(input_data_path, sep=',')
    logger.info(f'Successfuly loaded raw input data. Shape: {data.shape}')
    return data

def _save_preprocessed_data(output_data_path: str, data: DataFrame) -> None:
    logger.info(f'Saving processed data to {output_data_path}')
    output_data_dir: str = os.path.dirname(output_data_path)
    os.makedirs(output_data_dir, exist_ok=True)
    data.to_csv(output_data_path, index=False)
    logger.info(f'Successfuly saved processed data.')

def _get_preprocessed_data(data: DataFrame) -> DataFrame:
    logger.info(f'Processing data.')
    data = data.dropna()
    data = _set_ocean_proximity_as_ohe(data)
    data['total_rooms'] = np.log(data['total_rooms'] + 1)
    data['total_bedrooms'] = np.log(data['total_bedrooms'] + 1)
    data['population'] = np.log(data['population'] + 1)
    data['households'] = np.log(data['households'] + 1)
    data['bedroom_ratio'] = data['total_bedrooms'] / data['total_rooms']
    data['household_rooms'] = data['total_rooms'] / data['households']
    logger.info(f'Successfuly processed data. Shape: {data.shape}')
    return data

def _set_ocean_proximity_as_ohe(data: DataFrame) -> DataFrame:
    ocean_proximity_ohe = pd.get_dummies(data['ocean_proximity']) 
    data = data.join(ocean_proximity_ohe)
    data = data.drop(columns=['ocean_proximity'])
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess raw data and save to a specified output directory.')
    parser.add_argument('-i', '--input_data_path', type=str, required=True, help='Path to the raw input data file (CSV format)')
    parser.add_argument('-o', '--output_data_path', type=str, required=True, help='Path to the output directory and filename (CSV format) to save preprocessed data')
    args = parser.parse_args()
    preprocess(args.input_data_path, args.output_data_path)