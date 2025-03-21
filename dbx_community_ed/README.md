# Web Server Access Log Analysis - Databricks Community Edition Distribution Version
This repo and it's content was developed as a solution for Santander's Hiring Case - described on assignment.md (in pt-br)

A Spark solution to parse a standard Web Server Access Log text file into a Spark DataFrame and futher analyse it's content.

Distributed using Databricks Community Edition


# Setup

## 1. Upload the Log File

* Log into Databricks Community Edition.
* Click in + New on the left side bar and "Add or Upload Data"
* Upload your Access Log file
* Copy the generated DBFS path (e.g. dbfs:/FileStore/tables/access_log.zip)
* If the file was in .zip format, check step 2. If file in .txt jump to step 3

## 2. Unzip file in DBX

* Copy or import dbx_unzip.ipynb file into Databricks Workspace
* Copy the DBFS path aquired in step 1 on the zip_path variable in the first cell
* Run all cells

## 3. Run Access Log Analysis

* Copy or import web_server_access_log_analysis.py into Databricks Workspace
* At line 7, change the access_log_path to the DBFS path you aquired in Step 1, if you uploaded a .txt file. If you uploaded a ZIP file, do nothing.
* Run the script


# Change Log

[CHANGELOG.md](/dbx_community_ed/CHANGELOG.md)
