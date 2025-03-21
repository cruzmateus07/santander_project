# Change Log

All notable changes to this project will be documented in this file.


# 1.0.0 - 2025-03-15

Unzips access_logs, loads into spark dataframe, perform operations based on required analysis

## Added

* [access_log.zip](access_log.zip) Log data in .zip format
* [web_server_access_log_analysis.py](web_server_access_log_analysis.py) Base solution
* [requirements.txt](requirements.txt) Requirements for successful run


# 1.0.1 - 2025-03-21

Base solution isolated into a folder, to act as it's on format of distribution if needed.

## Changed

* [main.py](main.py) PATCH web_server_access_log_analysis.py is now called main.py