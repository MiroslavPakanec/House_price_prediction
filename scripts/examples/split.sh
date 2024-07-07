#!/bin/bash

# Run split python script
INPUT_PATH=./data/housing_california_preprocessed.csv
OUTPUT_DIR=./data
TEST_SIZE=0.2
python ./src/split.py --input_data_path "$INPUT_PATH" --output_directory "$OUTPUT_DIR" --test-size "$TEST_SIZE" --delete-source