#!/bin/bash

# Train model
TRAIN_DATA_DIRECTORY=./data
OUTPUT_DIRECTORY=./data
python ./src/train.py --train_data_directory "$TRAIN_DATA_DIRECTORY" --output_directory "$OUTPUT_DIRECTORY" --delete-input