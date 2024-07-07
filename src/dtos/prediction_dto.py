from typing import Optional
from pydantic import BaseModel
from dtos.housing_sample import HousingSample


class PredictionDto(BaseModel):
    sample: HousingSample
    experiment_name: Optional[str] = None
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'sample': {
                        'latitude': -122.22,
                        'longitude': 37.79,
                        'housing_median_age': 44,
                        'total_rooms': 1487,
                        'total_bedrooms': 314,
                        'population': 961,
                        'households': 272,
                        'median_income': 3.5156,
                        'ocean_proximity': 'NEAR BAY'
                    }
                }
            ]
        }
    }