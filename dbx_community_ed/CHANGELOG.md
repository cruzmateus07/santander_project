# Change Log - Databricks Community Edition Distribution Version

All notable changes to this project will be documented in this file.


# 1.0.0 - 2025-03-21

Databricks Community Edition distribution added, all required files where duplicated to docker folder to act as an isolated distribution.

## Added

* [access_log.zip](/dbx_community_ed/access_log.zip) PATCH Log data in .zip format
* [web_server_access_log_analysis.py](/dbx_community_ed/main.py) PATCH Base solution adapted to DBX
* [dbx_unzip.ipynb](/dbx_community_ed/dbx_unzip.ipynb) PATCH Databricks Unzip Python Notebook Script


# 1.1.0 - 2025-03-21

Logic to save processed log data into the data lake, following the provided modeling.

## Changed

* [main.py](/dbx_community_ed/main.py) PATCH Renamed web_server_access_log_analysis.py to main.py | Added try logic for saving the processed data in the data lake
