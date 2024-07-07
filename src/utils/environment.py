from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

def singleton(_class):
    instances = {}
    def get(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]
    return get

@singleton
class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')

    HOST_IP: str
    CONTAINER_PORT: int
    COMPOSE_PROJECT_NAME: str

    MODEL_PATH: str
    SCALER_PATH: str
    MODEL_FILENAME: str
    SCALER_FILENAME: str
    METRICS_FILENAME: str
    NP_X_TRAIN_FILENAME: str
    NP_Y_TRAIN_FILENAME: str
    NP_X_TEST_FILENAME: str
    NP_Y_TEST_FILENAME: str