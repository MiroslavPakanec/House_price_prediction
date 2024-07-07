import traceback
from loguru import logger
from fastapi import APIRouter
from starlette.responses import JSONResponse
from dtos.prediction_dto import PredictionDto
from predict import predict

inference_router = APIRouter()

@inference_router.post('/predict')
def predict_endpoint(payload: PredictionDto):
    try:
        predicted_price: int = predict(payload.sample, payload.experiment_name)
        return { 'price': predicted_price, 'currency': 'United States dollar' }
    except Exception as e:
        logger.error('[GENERIC ERROR]')
        logger.debug(e)
        # logger.error(traceback.format_exc())
        return JSONResponse(content={'error': 'Server failed to process request'}, status_code=500)