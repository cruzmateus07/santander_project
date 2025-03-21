# Change Log

All notable changes to this project will be documented in this file.


# 1.0.0 - 2025-03-15

Unzips access_logs, loads into spark dataframe, perform operations based on required analysis

## Added

* [access_log.zip](/base_solution/access_log.zip) Log data in .zip format
* [web_server_access_log_analysis.py](/base_solution/main.py) Base solution
* [requirements.txt](/base_solution/requirements.txt) Requirements for successful run


# 1.0.1 - 2025-03-21

Base solution isolated into a folder, to act as it's on format of distribution if needed.

## Changed

* [main.py](/base_solution/main.py) PATCH web_server_access_log_analysis.py is now called main.py


# 1.1.0 - 2025-03-21

Unit Tests added to base solution

## Added

* [unit_tests.py](/base_solution/unit_tests.py) PATCH Unit tests for Web Server Access Log Analysis
