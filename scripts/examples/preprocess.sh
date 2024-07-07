#!/bin/bash

# Run preprocessing python script
INPUT_PATH="./data/housing_california.csv"
OUTPUT_PATH="./experiments/default/housing_california_preprocessed.csv"
python ./src/preprocess.py --input_data_path "$INPUT_PATH" --output_data_path "$OUTPUT_PATH"