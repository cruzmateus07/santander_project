# Change Log

All notable changes to this project will be documented in this file.


# 0.0.1 - 2025-03-15

Project Repo Launched

## Added

* [access_log.zip](access_log.zip) Log data in .zip format
* [assignement.md](assignement.md) Santander Problem Statement (in pt-br)


# 1.0.0 - 2025-03-15

Unzips access_logs, loads into spark dataframe, perform operations based on required analysis

## Added

* [web_server_access_log_analysis.py](web_server_access_log_analysis.py) Base solution
* [requirements.txt](requirements.txt) Requirements for successful run


# 1.0.1 - 2025-03-21

Base solution isolated into a folder, to act as it's on format of distribution if needed.

## Changed

* [main.py](main.py) PATCH web_server_access_log_analysis.py is now called main.py


# 1.1.0 - 2025-03-21

Docker distribution added, all required files where duplicated to docker folder to act as an isolated distribution if needed.

## Added

* [access_log.zip](/docker/access_log.zip) PATCH Log data in .zip format
* [web_server_access_log_analysis.py](/docker/web_server_access_log_analysis.py) PATCH Base solution
* [requirements.txt](/docker/requirements.txt) PATCH Requirements for successful run
* [Dockerfile](/docker/Dockerfile) PATCH Dockerfile for Distribution
* [docker-composer.yml](/docker/docker-composer.yml) PATCH Docker Composer added (using version 3.9)


# 1.2.0 - 2025-03-21

Databricks Community Edition Distribution added, all required files where duplicated to dbx_community_ed folder to act as an isolated distribution if needed.

## Added

* [access_log.zip](/dbx_community_ed/access_log.zip) PATCH Log data in .zip format
* [web_server_access_log_analysis.py](/dbx_community_ed/web_server_access_log_analysis.py) PATCH Base solution adapted to DBX
* [dbx_unzip.ipynb](/dbx_community_ed/dbx_unzip.ipynb) PATCH Databricks Unzip Python Notebook Script

