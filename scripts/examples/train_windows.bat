@echo off

REM Train model
set TRAIN_DATA_DIRECTORY=.\experiments\default
set OUTPUT_DIRECTORY=.\experiments\default
python .\src\train.py --train_data_directory "%TRAIN_DATA_DIRECTORY%" --output_directory "%OUTPUT_DIRECTORY%"