#!/bin/bash

# Run split python script
INPUT_PATH=./experiments/default/housing_california_preprocessed.csv
OUTPUT_DIR=./experiments/default
TEST_SIZE=0.2
python ./src/split.py --input_data_path "$INPUT_PATH" --output_directory "$OUTPUT_DIR" --test-size "$TEST_SIZE"