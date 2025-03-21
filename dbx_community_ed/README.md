# Web Server Access Log Analysis - Databricks Community Edition Distribution Version
This repo and it's content was developed as a solution for Santander's Hiring Case - described on assignment.md (in pt-br)

A Spark solution to parse a standard Web Server Access Log text file into a Spark DataFrame and futher analyse it's content.

Distributed using Databricks Community Edition


# Setup

## 1. Upload the Log File

* Log into Databricks Community Edition.
* Click in + New on the left side bar and "Add or Upload Data"
* Upload [access_log.zip](/dbx_community_ed/access_log.zip)
* Copy the generated DBFS path (e.g. dbfs:/FileStore/tables/access_log.zip)
* If the file was in .zip format, check step 2. If file in .txt jump to step 3

## 2. Unzip file in DBX

* Copy or import [dbx_unzip.ipynb](/dbx_community_ed/dbx_unzip.ipynb) file into Databricks Workspace
* Copy the DBFS path aquired in step 1 on the zip_path variable in the first cell

## 3. Run Access Log Analysis

* Copy or import [main.py](/dbx_community_ed/main.py) into Databricks Workspace
* At line 7, change the access_log_path to the DBFS path you aquired in Step 1, if you uploaded a .txt file. If you uploaded a ZIP file, do nothing.


# Execution

* 1. Crete Cluster:
  * Go to Compute on the left side bar
  * Create Compute
  * Select at least 12.2 LTS for Databricks Runtime Version (Used to develop this code)
  * Driver type should be the Community Optimized, since this is being used on Databricks Community Edition
  * The Cluster should start upon creation, if that's not the case, start the cluster

* 2. Attach Cluster to notebook:
  * Go to dbx_unzip notebook you copied/imported to Databricks
  * On the top right, select the cluster you just created that should be already starting, and attach it to the notebook
  * The same process needs to be peformed on main.py later

* 3. Run notebooks:
  * Run all cells, after proper setup, on dbx_unzip notebook
  * After dbx_unzip finishes running completely, go to main.py and run the notebook (if you copied as is, should be one cell, otherwise - run all cells)

# Used Technologies

* Databricks - Cluster Specs:
  * Databricks Runtime Version 12.2 LTS (Includes Apache Spark 3.3.2)


# Current Features

The solution provides the analysis of a few indicators for the log file provided such as:
  * Top 10 Client IPs based on access numbers
  * Top 6 accessed endpoints (disregarding the ones that are files)
  * Distinct Client IPs
  * How many different days are in the file
  * Request's Volume analysis such as - Total Volume, Max Volume and Min Volume Size, Average Volume Size

An option to save the processed data was provided using the Data Lake integration and following the modeling below:

[web_server_access_log_modeling](web_server_access_log_modeling.png)


# Change Log

[CHANGELOG.md](/dbx_community_ed/CHANGELOG.md)
