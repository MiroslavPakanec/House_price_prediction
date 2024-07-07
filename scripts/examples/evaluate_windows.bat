@echo off

REM Train model
set TEST_DATA_DIRECTORY=.\experiments\default
set MODEL_DIRECTORY=.\experiments\default
set OUTPUT_DIRECTORY=.\experiments\default
python .\src\evaluate.py --test_data_directory "%TEST_DATA_DIRECTORY%" --model_directory "%MODEL_DIRECTORY%" --output_directory "%OUTPUT_DIRECTORY%"