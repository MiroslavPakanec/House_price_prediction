@echo off

REM Train model
set TRAIN_DATA_DIRECTORY=.\data
set OUTPUT_DIRECTORY=.\data
python .\src\train.py --train_data_directory "%TRAIN_DATA_DIRECTORY%" --output_directory "%OUTPUT_DIRECTORY%"