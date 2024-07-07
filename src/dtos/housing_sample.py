from typing import Literal
from pydantic import BaseModel

class HousingSample(BaseModel):
    latitude: float
    longitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    ocean_proximity: Literal['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']