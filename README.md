# Apple Health Data Analysis

This project aims to use the Apple Health data from the Apple watch and Withings smart scale to do analysis how the health markers change quantitively based on my dietary changes

## Overview
* Apple Health on an iPhone is a teasuretrove of data especially if pared with devices like Apple Watch and smart scale
* Exporting this data is very archaic, we do get an massive XML file (> 1 GB) which we need to wrestle with to make is useful for our needs
* We decode this XML file in raw_data into more friendly JSON and do a very basic filtering based off of
    * Datatime > midnight 2024-12-31
    * Selecting only the following metrics
        * BodyMass
        * LeanBodyMass
        * BodyFatPercentage
        * HeartRate
        * RestingHeartRate
        * WalkingHeartRateAverage
        * HeartRateVariabilitySDNN
* This gives us a more managable 21 MB line seprated JSON file in bronze_data
* This line seprated JSON data is futher refined by dropping unessary columns and spliting the data for each metric into it's own CSV file
* These CSV data is then futher refined by
    * using mean value of the metric for an entire day
    * interpolating missing values
    * adding 'on diet' metric
* In future iteration I could
    * quantify the changes in other metircs w.r.t.'on diet'
    * add more metrics from raw data for analysis
    * do more advanced aggrigation of metrics instead of current simple average for daily intervals

## Setup steps
* Make sure `python3` and `poetry` are installed in your system
* Run `poetry install --no-root` to install the dependencies

## Running project scripts
* Export the Apple Health data and unzip it
* Copy the **export.xml** from Apple Health export to `raw_data/export.xml`
* Run `poetry run python raw_data_to_bronze_data.py`
* Run `poetry run jupyter notebook`
* Run all the code blocks in the notebook `bronze_data_to_silver.ipynb`
* Run all the code blocks in the notebook `silver_data_to_gold.ipynb`
