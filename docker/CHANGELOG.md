# Change Log

All notable changes to this project will be documented in this file.


# 1.0.0 - 2025-03-21

Unzips access_logs, loads into spark dataframe, perform operations based on required analysis.

Docker Distribution added

## Added

* [access_log.zip](/docker/access_log.zip) PATCH Log data in .zip format
* [web_server_access_log_analysis.py](/docker/main.py) PATCH Base solution
* [requirements.txt](/docker/requirements.txt) PATCH Requirements for successful run
* [Dockerfile](/docker/Dockerfile) PATCH Dockerfile for Distribution
* [docker-composer.yml](/docker/docker-composer.yml) PATCH Docker Composer added (using version 3.9)


# 1.1.0 - 2025-03-21

Logic to save processed logs into Postgres table added - following the proposed and presented modeling at [README.md](/docker/README.md)

## Changed

* [main.py](/docker/main.py) PATCH web_server_access_log_analysis.py renamed to main.py | Saving processed dataframe to Postgres logic added


# 1.1.1 - 2025-03-21

Fix apllied to docker to bring Postgres config to it.

## Changed

* [main.py](/docker/main.py) PATCH Postgres info now inherited from Docker
* [Dockerfile](/docker/Docker) PATCH Forced access_log.zip into fixed path for extraction
* [docker-composer.yml](/docker/docker-composer.yml) PATCH Added Postgres config