# Change Log

All notable changes to this project will be documented in this file.


# 0.0.1 - 2025-03-15

Project Repo Launched

## Added

* [base_solution/access_log.zip](/base_solution/access_log.zip) Log data in .zip format
* [assignement.md](assignement.md) Santander Problem Statement (in pt-br)


# 1.0.0 - 2025-03-15

Unzips access_logs, loads into spark dataframe, perform operations based on required analysis

## Added

* [base_solution/web_server_access_log_analysis.py](/base_solution/main.py) Base solution
* [base_solution/requirements.txt](/base_solution/requirements.txt) Requirements for successful run


# 1.0.1 - 2025-03-21

Base solution isolated into a folder, to act as it's on format of distribution if needed.

## Changed

* [base_solution/main.py](/base_solution/main.py) PATCH web_server_access_log_analysis.py is now called main.py


# 1.1.0 - 2025-03-21

Docker distribution added, all required files where duplicated to docker folder to act as an isolated distribution if needed.

## Added

* [docker/access_log.zip](/docker/access_log.zip) PATCH Log data in .zip format
* [docker/web_server_access_log_analysis.py](/docker/main.py) PATCH Base solution
* [docker/requirements.txt](/docker/requirements.txt) PATCH Requirements for successful run
* [docker/Dockerfile](/docker/Dockerfile) PATCH Dockerfile for Distribution
* [docker/docker-composer.yml](/docker/docker-composer.yml) PATCH Docker Composer added (using version 3.9)


# 1.2.0 - 2025-03-21

Databricks Community Edition Distribution added, all required files where duplicated to dbx_community_ed folder to act as an isolated distribution if needed.

## Added

* [dbx_community_ed/access_log.zip](/dbx_community_ed/access_log.zip) PATCH Log data in .zip format
* [dbx_community_ed/web_server_access_log_analysis.py](/dbx_community_ed/main.py) PATCH Base solution adapted to DBX
* [dbx_community_ed/dbx_unzip.ipynb](/dbx_community_ed/dbx_unzip.ipynb) PATCH Databricks Unzip Python Notebook Script


# 1.2.1 - 2025-03-21

Processed Logs Modeling Proposal added (Solution for both Docker and DBX Community Ed. distributions).

On Docker Distribution, logic to save processed logs into Postgres table added - following the proposed and presented modeling at [README.md](/docker/README.md)

## Added

* [web_server_access_log_modeling](web_server_access_log_modeling.png) PATCH Processed Logs Modeling representation

## Changed

* [docker/main.py](/docker/main.py) PATCH web_server_access_log_analysis.py renamed to main.py | Saving processed dataframe to Postgres logic added


# 1.2.2 - 2025-03-21

Fix apllied to docker to bring Postgres config to it.

## Changed

* [docker/main.py](/docker/main.py) PATCH Postgres info now inherited from Docker
* [docker/Dockerfile](/docker/Docker) PATCH Forced access_log.zip into fixed path for extraction
* [docker/docker-composer.yml](/docker/docker-composer.yml) PATCH Added Postgres config


# 1.3.0 - 2025-03-21

Logic to save processed log data into the data lake, following the provided modeling.

## Changed

* [dbx_community_ed/main.py](/dbx_community_ed/main.py) PATCH Renamed web_server_access_log_analysis.py to main.py | Added try logic for saving the processed data in the data lake


# 1.4.0 - 2025-03-21

Unit Tests added to all distributions

## Added

* [unit_tests.py](/base_solution/unit_tests.py) PATCH Unit tests for Web Server Access Log Analysis Base Solution
* [unit_tests.py](/dbx_community_ed/unit_tests.py) PATCH Unit tests for solution distributed by Databricks Community Edition
* [unit_tests.py](/docker/unit_tests.py) PATCH Unit tests for solution distributed by Docker
