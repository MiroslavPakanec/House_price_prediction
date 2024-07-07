import joblib
import argparse
import traceback
import numpy as np
import pandas as pd
from loguru import logger
from typing import Literal
from pandas import DataFrame
from pydantic import BaseModel
from preprocess import get_preprocessed_data
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from dtos.housing_sample import HousePriceSample

def predict(sample: HousePriceSample) -> float:
    try:
        logger.info('[Predicting...]')
        sample_dict = sample.dict()
        df: DataFrame = pd.DataFrame([sample_dict])
        df: DataFrame = get_preprocessed_data(df)
        x: np.ndarray = df.to_numpy()

        scaler_path: str = './scaler.joblib'
        model_path: str = './model.joblib'
        scaler: StandardScaler = _load_scaler(scaler_path)
        model: LinearRegression = _load_model(model_path)

        x: np.ndarray = _normilize(x, scaler)
        y: int = _predict_house_price(x, model)
        logger.info(f'Predicted Median House Value: {y}$')
        return y
    except Exception as e:
        logger.error(f'An error occured during the execution of {__file__}')
        logger.error(e)
        # logger.debug(traceback.format_exc())


def _load_scaler(path: str) -> StandardScaler:
    logger.info(f'Loading scaler from {path}')
    scaler: StandardScaler = joblib.load(path)
    return scaler

def _load_model(path: str) -> LinearRegression:
    logger.info(f'Loading model from {path}')
    model: LinearRegression = joblib.load(path)
    return model

def _normilize(data: np.ndarray, scaler: StandardScaler) -> np.ndarray:
    data = scaler.transform(data)
    return data

def _predict_house_price(x: np.ndarray, model: LinearRegression) -> int:
    y_pred: np.ndarray = model.predict(x)
    return int(y_pred[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict a house price.')
    parser.add_argument('-lat', '--latitude', type=float, required=True, help='Latitude of the house.')
    parser.add_argument('-long', '--longitude', type=float, required=True, help='Longitude of the house.')
    parser.add_argument('-age', '--housing_median_age', type=int, required=True, help='Median age of a house within a block; a lower number is a newer building.')
    parser.add_argument('-tr', '--total_rooms', type=int, required=True, help='Total number of rooms within a block.')
    parser.add_argument('-tb', '--total_bedrooms', type=int, required=True, help='Total number of bedrooms within a block.')
    parser.add_argument('-po', '--population', type=int, required=True, help='Total number of people residing within a block.')
    parser.add_argument('-ho', '--households', type=int, required=True, help='Total number of households, a group of people residing within a home unit, for a block.')
    parser.add_argument('-mi', '--median_income', type=float, required=True, help='Median income for households within a block of houses (measured in tens of thousands of US Dollars).')
    parser.add_argument('-op', '--ocean_proximity', type=str, required=True, choices=['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], help='Location of the house w.r.t ocean/sea.')
    args = parser.parse_args()
    sample = HousePriceSample(latitude=args.latitude, longitude=args.longitude,
                              housing_median_age=args.housing_median_age,
                              total_rooms=args.total_rooms, total_bedrooms=args.total_bedrooms,
                              population=args.population, households=args.households,
                              median_income=args.median_income, ocean_proximity=args.ocean_proximity)
    predict(sample)


