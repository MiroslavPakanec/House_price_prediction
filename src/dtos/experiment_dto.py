from typing import Optional
from pydantic import BaseModel
from dtos.housing_sample import HousingSample
from utils.environment import Environment


class ExperimentDto(BaseModel):
    experiment_name: str
    data_filepath: Optional[str] = Environment().DEFAULT_DATA_PATH
    test_size: Optional[float] = Environment().DEFAULT_TEST_SIZE
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'experiment_name': 'default',
                    'data_filepath': Environment().DEFAULT_DATA_PATH,
                    'test_size': Environment().DEFAULT_TEST_SIZE
                }
            ]
        }
    }