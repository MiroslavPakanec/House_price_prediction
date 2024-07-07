import traceback
from dtos.experiment_dto import ExperimentDto
from evaluate import evaluate
from loguru import logger
from fastapi import APIRouter
from starlette.responses import JSONResponse
from preprocess import preprocess
from split import split
from train import train
from utils.exceptions import ExperimentAlreadyExists
from utils.path_utils import get_experiment_directory_path, get_experiment_preprocessed_filepath, validate_experiment_does_not_exist

experiment_router = APIRouter()

@experiment_router.post('/run_experiment')
def run_experiment_endpoint(payload: ExperimentDto):
    try:
        test_size: float = payload.test_size
        data_filepath: str = payload.data_filepath
        experiment_name: str = payload.experiment_name
        experiment_directory_path: str = get_experiment_directory_path(experiment_name)
        preprocessed_data_filepath: str = get_experiment_preprocessed_filepath(experiment_name)
        
        validate_experiment_does_not_exist(experiment_name)
        preprocess(data_filepath, preprocessed_data_filepath)
        split(preprocessed_data_filepath, experiment_directory_path, test_size)
        train(experiment_directory_path, experiment_directory_path)
        evaluate(experiment_directory_path, experiment_directory_path, experiment_directory_path)
        return { 'message': 'Successfully run experiment.', 'experiment_name': experiment_name }
    except ExperimentAlreadyExists as e:
        logger.error('[DUPLICATE EXPERIMENT]')
        logger.debug(e)
        return JSONResponse(content={'error': f'Experiment {payload.experiment_name} already exists.'}, status_code=400)
    except Exception as e:
        logger.error('[GENERIC ERROR]')
        logger.debug(e)
        logger.error(traceback.format_exc())
        return JSONResponse(content={'error': 'Server failed to process request'}, status_code=500)