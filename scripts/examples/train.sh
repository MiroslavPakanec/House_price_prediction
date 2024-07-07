#!/bin/bash

# Train model
TRAIN_DATA_DIRECTORY=./experiments/default
OUTPUT_DIRECTORY=./experiments/default
python ./src/train.py --train_data_directory "$TRAIN_DATA_DIRECTORY" --output_directory "$OUTPUT_DIRECTORY"