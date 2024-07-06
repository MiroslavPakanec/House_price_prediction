#!/bin/bash

# Run Experiment

# Check if name parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <name> [-f | --force]"
    exit 1
fi

NAME=$1
FORCE_FLAG=

# Check for optional -f or --force flag
if [ "$2" == "-f" ] || [ "$2" == "--force" ]; then
    FORCE_FLAG=-f
fi

# Prepare experiment directory
EXPERIMENT_DIR=./experiments/$NAME
if [ -d "$EXPERIMENT_DIR" ]; then
    if [ -z "$FORCE_FLAG" ]; then
        echo "Experiment directory $EXPERIMENT_DIR already exists. Use -f or --force flag to overwrite."
        exit 1
    else
        echo "Experiment directory $EXPERIMENT_DIR already exists. Clearing contents."
        rm -rf "$EXPERIMENT_DIR"
        mkdir "$EXPERIMENT_DIR"
    fi
else
    mkdir -p "$EXPERIMENT_DIR"
fi

# Preprocess data
INPUT_DATA_PATH=./data/housing_california.csv
OUTPUT_DATA_PATH=$EXPERIMENT_DIR/housing_california_preprocessed.csv
python ./src/preprocess.py --input_data_path "$INPUT_DATA_PATH" --output_data_path "$OUTPUT_DATA_PATH"

# Split data
PREPROCESSED_DATA_PATH=$EXPERIMENT_DIR/housing_california_preprocessed.csv
SPLIT_OUTPUT_DIR=$EXPERIMENT_DIR
TEST_SIZE=0.2
python ./src/split.py --input_data_path "$PREPROCESSED_DATA_PATH" --output_directory "$SPLIT_OUTPUT_DIR" --test-size $TEST_SIZE

# Train model
TRAIN_DATA_DIRECTORY=$EXPERIMENT_DIR
MODEL_OUTPUT_DIRECTORY=$EXPERIMENT_DIR
python ./src/train.py --train_data_directory "$TRAIN_DATA_DIRECTORY" --output_directory "$MODEL_OUTPUT_DIRECTORY"

# Evaluate model
TEST_DATA_DIRECTORY=$EXPERIMENT_DIR
MODEL_DIRECTORY=$EXPERIMENT_DIR
METRICS_OUTPUT_DIRECTORY=$EXPERIMENT_DIR
python ./src/evaluate.py --test_data_directory "$TEST_DATA_DIRECTORY" --model_directory "$MODEL_DIRECTORY" --output_directory "$METRICS_OUTPUT_DIRECTORY"