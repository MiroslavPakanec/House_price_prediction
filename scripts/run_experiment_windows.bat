@echo off
REM Run Experiment

REM Handle parameters: [name] [-Force]
if "%1"=="" (
    echo "Usage: run_experiment.bat <name>"
    exit /b 1
)

set NAME=%1
set FORCE_FLAG=
if "%2"=="-Force" (
    set FORCE_FLAG=-Force
)

REM Prepare experiment directory
set EXPERIMENT_DIR=.\experiments\%NAME%
if exist "%EXPERIMENT_DIR%" (
    if "%FORCE_FLAG%"=="" (
        echo "Experiment directory %EXPERIMENT_DIR% already exists. Use -Force flag to overwrite."
        exit /b 1
    ) else (
        echo "Experiment directory %EXPERIMENT_DIR% already exists. Clearing contents."
        rmdir /s /q "%EXPERIMENT_DIR%"
        mkdir "%EXPERIMENT_DIR%"
    )
) else (
    mkdir "%EXPERIMENT_DIR%"
)

REM Preprocess data
set INPUT_DATA_PATH=.\data\housing_california.csv
set OUTPUT_DATA_PATH=%EXPERIMENT_DIR%\housing_california_preprocessed.csv
python .\src\preprocess.py --input_data_path "%INPUT_DATA_PATH%" --output_data_path "%OUTPUT_DATA_PATH%"

REM Split data
set PREPROCESSED_DATA_PATH=%EXPERIMENT_DIR%\housing_california_preprocessed.csv
set SPLIT_OUTPUT_DIR=%EXPERIMENT_DIR%
set TEST_SIZE=0.2
python .\src\split.py --input_data_path "%PREPROCESSED_DATA_PATH%" --output_directory "%SPLIT_OUTPUT_DIR%" --test-size %TEST_SIZE%

REM Train model
set TRAIN_DATA_DIRECTORY=%EXPERIMENT_DIR%
set MODEL_OUTPUT_DIRECTORY=%EXPERIMENT_DIR%
python .\src\train.py --train_data_directory "%TRAIN_DATA_DIRECTORY%" --output_directory "%MODEL_OUTPUT_DIRECTORY%"

REM Evaluate model
set TEST_DATA_DIRECTORY=%EXPERIMENT_DIR%
set MODEL_DIRECTORY=%EXPERIMENT_DIR%
set METRICS_OUTPUT_DIRECTORY=%EXPERIMENT_DIR%
python .\src\evaluate.py --test_data_directory "%TEST_DATA_DIRECTORY%" --model_directory "%MODEL_DIRECTORY%" --output_directory "%METRICS_OUTPUT_DIRECTORY%"