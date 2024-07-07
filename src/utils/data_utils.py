import numpy as np
from typing import Tuple
from sklearn.preprocessing import StandardScaler

def transform(data: np.ndarray, scaler: StandardScaler) -> np.ndarray:
    data = scaler.transform(data)
    return data

def fit_transform(data: np.ndarray) -> Tuple[np.ndarray, StandardScaler]:
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data, scaler