@echo off

REM Run split python script
set INPUT_PATH=.\experiments\default\housing_california_preprocessed.csv
set OUTPUT_DIRECTORY=.\experiments\default
set TEST_SIZE=0.2
python .\src\split.py --input_data_path "%INPUT_PATH%" --output_directory "%OUTPUT_DIRECTORY%" --test-size %TEST_SIZE%