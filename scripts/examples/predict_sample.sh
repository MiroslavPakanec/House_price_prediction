#!/bin/sh

# Set variables for sample data
LONGITUDE=-122.22
LATITUDE=37.79
HOUSING_MEDIAN_AGE=44
TOTAL_ROOMS=1487
TOTAL_BEDROOMS=314
POPULATION=961
HOUSEHOLDS=272
MEDIAN_INCOME=3.5156
OCEAN_PROXIMITY="NEAR BAY"

# Construct the command using temporary variables
COMMAND="python ./src/predict.py \
    --longitude $LONGITUDE \
    --latitude $LATITUDE \
    --housing_median_age $HOUSING_MEDIAN_AGE \
    --total_rooms $TOTAL_ROOMS \
    --total_bedrooms $TOTAL_BEDROOMS \
    --population $POPULATION \
    --households $HOUSEHOLDS \
    --median_income $MEDIAN_INCOME \
    --ocean_proximity \"$OCEAN_PROXIMITY\""

# Execute the command
eval $COMMAND