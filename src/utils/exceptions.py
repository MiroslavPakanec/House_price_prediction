from fastapi import HTTPException

class ExperimentAlreadyExists(HTTPException):
    def __init__(self, experiment_name: str, status_code: int = 400):
        super().__init__(detail=f'Experiment with name {experiment_name} already exists.', status_code=status_code)