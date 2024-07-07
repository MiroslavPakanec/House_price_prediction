@echo off

REM Set variables for sample data
set LONGITUDE=-122.22
set LATITUDE=37.79
set HOUSING_MEDIAN_AGE=44
set TOTAL_ROOMS=1487
set TOTAL_BEDROOMS=314
set POPULATION=961
set HOUSEHOLDS=272
set MEDIAN_INCOME=3.5156
set OCEAN_PROXIMITY="NEAR BAY"
set EXPERIMENT=ex_1

REM Construct the command using temporary variables
set COMMAND=python .\src\predict.py ^
    --experiment %EXPERIMENT% ^
    --longitude %LONGITUDE% ^
    --latitude %LATITUDE% ^
    --housing_median_age %HOUSING_MEDIAN_AGE% ^
    --total_rooms %TOTAL_ROOMS% ^
    --total_bedrooms %TOTAL_BEDROOMS% ^
    --population %POPULATION% ^
    --households %HOUSEHOLDS% ^
    --median_income %MEDIAN_INCOME% ^
    --ocean_proximity %OCEAN_PROXIMITY%

REM Execute the command
%COMMAND%