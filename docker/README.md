# Web Server Access Log Analysis - Docker Distribution Version

A Spark solution to parse a standard Web Server Access Log text file into a Spark DataFrame and futher analyse it's content.

Distributed using Docker

# Requirements

[requirements.txt](/docker/requirements.txt)


# Setup

* Postgres Setup - Save web_server_access_log table (Processed logs)

On [main.py](main.py) at lines 10 to 15, Postgres information need to be provided to properly save the processed logs into it

If wrong information is provided, the code will successfully run through the analysis, however the table won't be saved.


# Used Technologies

* Python 3.13.1
* Python Lib - PySpark 3.5.4
* Docker 3.9
* PostgreSQL - The reasons for using Postgres at this distribution are:
  * Relational database -> After being properly parsed, the logs were in a structured data format favoring a relational db
  * Cloud-friendly -> Since scability is one of the requirements

# Current Features

The solution, with 3 different distribution options, provides the analysis of a few indicators for the log file provided such as:
  * Top 10 Client IPs based on access numbers
  * Top 6 accessed endpoints (disregarding the ones that are files)
  * Distinct Client IPs
  * How many different days are in the file
  * Request's Volume analysis such as - Total Volume, Max Volume and Min Volume Size, Average Volume Size

An option to save the processed data was provided using Postgres and following the modeling below:

[web_server_access_log_modeling](web_server_access_log_modeling.png)


# Change Log

[CHANGELOG.md](/docker/CHANGELOG.md)
