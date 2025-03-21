# Web Server Access Log Analysis
This repo and it's content was developed as a solution for Santander's Hiring Case - described on assignment.md (in pt-br)

A Spark solution to parse a standard Web Server Access Log text file into a Spark DataFrame and futher analyse it's content.


# Distributions

This Solution has 3 different distributions available:
* [base_solution](base_solution/) -> Manual setup on User's Machine
* [dbx_community_ed](dbx_community_ed/) -> Databricks Community Edition Distribution
* [docker](docker/) -> Docker Distribution

Please, refer to each README.md files in each distribution folder for details on Setup, Requirements and Development.


# Current Features

The solution, with 3 different distribution options, provides the analysis of a few indicators for the log file provided such as:
  * Top 10 Client IPs based on access numbers
  * Top 6 accessed endpoints (disregarding the ones that are files)
  * Distinct Client IPs
  * How many different days are in the file
  * Request's Volume analysis such as - Total Volume, Max Volume and Min Volume Size, Average Volume Size

For both Docker and Databricks Community Edition distributions, an option to save the processed data was provided.

At Docker, Postgres. At DBX Community Ed., the Delta Lake. However, both tables follow the same modeling below:

[web_server_access_log_modeling](web_server_access_log_modeling.png)


# Author's Info

This entire Repository was created and developed by:
* Mateus Cruz
* cruzmateus07@gmail.com
* http://www.linkedin.com/in/cruzmateus


# Change Log

[CHANGELOG.md](CHANGELOG.md)
