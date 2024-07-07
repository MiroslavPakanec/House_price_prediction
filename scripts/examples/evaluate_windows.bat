@echo off

REM Train model
set TEST_DATA_DIRECTORY=.\data
set MODEL_DIRECTORY=.\data
set OUTPUT_DIRECTORY=.\data
python .\src\evaluate.py --test_data_directory "%TEST_DATA_DIRECTORY%" --model_directory "%MODEL_DIRECTORY%" --output_directory "%OUTPUT_DIRECTORY%"