# Web Server Access Log Analysis - Docker Distribution Version

A Spark solution to parse a standard Web Server Access Log text file into a Spark DataFrame and futher analyse it's content.

Distributed using Docker

# Requirements

[requirements.txt](/docker/requirements.txt)


# Setup

* Postgres Setup - Save web_server_access_log table (Processed logs)

On [docker-composer.yml](/docker/docker-composer.yml) change the info for POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD and POSTGRES_TABLE to match your Postgres Service.


# Execution

Run the shell command bellow to start everything through Docker:
docker-compose up --build


# Used Technologies

* Python 3.13.1
* Python Lib - PySpark 3.5.4
* Docker 3.9
* PostgreSQL - The reasons for using Postgres at this distribution are:
  * Relational database -> After being properly parsed, the logs were in a structured data format favoring a relational db
  * Cloud-friendly -> Since scability is one of the requirements


# Current Features

The solution provides the analysis of a few indicators for the log file provided such as:
  * Top 10 Client IPs based on access numbers
  * Top 6 accessed endpoints (disregarding the ones that are files)
  * Distinct Client IPs
  * How many different days are in the file
  * Request's Volume analysis such as - Total Volume, Max Volume and Min Volume Size, Average Volume Size

An option to save the processed data was provided using Postgres and following the modeling below:

[web_server_access_log_modeling](web_server_access_log_modeling.png)


# Change Log

[CHANGELOG.md](/docker/CHANGELOG.md)
