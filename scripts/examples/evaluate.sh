#!/bin/bash

# Train model
TEST_DATA_DIRECTORY=./experiments/default
MODEL_DIRECTORY=./experiments/default
OUTPUT_DIRECTORY=./experiments/default
python ./src/evaluate.py --test_data_directory "$TEST_DATA_DIRECTORY" --model_directory "$MODEL_DIRECTORY" --output_directory "$OUTPUT_DIRECTORY"