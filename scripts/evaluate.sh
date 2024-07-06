#!/bin/bash

# Train model
TEST_DATA_DIRECTORY=./data
MODEL_DIRECTORY=./data
OUTPUT_DIRECTORY=./data
python ./src/evaluate.py --test_data_directory "$TEST_DATA_DIRECTORY" --model_directory "$MODEL_DIRECTORY" --output_directory "$OUTPUT_DIRECTORY"