@echo off

REM Run split python script
set INPUT_PATH=.\data\housing_california_preprocessed.csv
set OUTPUT_DIR=.\data
set TEST_SIZE=0.2
python .\src\split.py --input_data_path "%INPUT_PATH%" --output_directory "%OUTPUT_DIR%" --test-size %TEST_SIZE% --delete-input