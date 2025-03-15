from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, date_format, max, min, regexp_extract, row_number, split, sum, to_date, when
from pyspark.sql.window import Window
import os
import zipfile


## -------------------- Init -------------------- ##
spark = SparkSession.builder.getOrCreate()

cwd = os.getcwd()
zip_path = f"{cwd}/access_log.zip"
extract_path = f"{cwd}/access_log_unzip/"

# Unzip text file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extract("access_log.txt", extract_path)

# Load text file into spark DataFrame
raw_log_df = spark.read.text(extract_path)

# Given that the log file follows the Web Server Access Log,
# the following regexp pattern can be used to parse the file
log_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(.*?)" (\d{3}) (\d+|-)'


## -------------------- DataFrame Manipulation -------------------- ##
# Extract fields using regex
parsed_log_df = raw_log_df.select(
    regexp_extract('value', log_pattern, 1).alias('ip_address'),
    regexp_extract('value', log_pattern, 2).alias('client_identity'),
    regexp_extract('value', log_pattern, 3).alias('user_id'),
    regexp_extract('value', log_pattern, 4).alias('timestamp'),
    regexp_extract('value', log_pattern, 5).alias('request'),
    regexp_extract('value', log_pattern, 6).alias('status_code'),
    regexp_extract('value', log_pattern, 7).alias('response_size')
)

# Aux columns added, df cached for improved performance on following operations
log_df = parsed_log_df \
    .withColumn("endpoint", split(col("request"), " ")[1]) \
    .withColumn("date", to_date(col("timestamp"), "dd/MMM/yyyy:HH:mm:ss Z")) \
    .withColumn(
        "response_size",
        when(
            col("response_size") != "-",
            col("response_size").cast("int")
        ).otherwise(0)
    ) \
    .withColumn("day_of_week", date_format("date", "EEEE")) \
    .cache()

## -------------------- Answers -------------------- ##
# Create a Window for rank based on count
count_window = Window.orderBy(col("count").desc())

# 1. Top 10 Client IPs based on access numbers.

top_10_ips = (
    log_df.groupBy("ip_address")
    .count()
    .withColumn("rank", row_number().over(count_window))
    .filter(col("rank") <= 10)
    .drop("rank")
)

print("Top 10 Client IPs: \n")
top_10_ips.show()


# 2. Top 6 accessed endpoints, disregarding the ones that are files.
# Filter out file-like paths (assuming extensions like .html, .jpg, etc.)
filtered_endpoints = log_df.filter(~col("endpoint").rlike(r"\.\w+$"))

top_6_endpoints = (
    filtered_endpoints.groupBy("endpoint")
    .count()
    .withColumn("rank", row_number().over(count_window))
    .filter(col("rank") <= 6)
    .drop("rank")
)

print("Top 6 Endpoints mais acessados: \n")
top_6_endpoints.show(truncate=False)


# 3. Distinct Client IPs
distinct_client_ip = log_df.select("ip_address").distinct().count()
print(f"Distinct Client IPs: {distinct_client_ip}")


# 4. How many different days are in the file
distinct_days = log_df.select("date").distinct().count()
print(f"How many different days are in the file: {distinct_days}")


# 5. Based on content size, in each response, return:
# 5.1 Total data volume.
total_volume = log_df.agg(sum("response_size").alias(
    "total_volume")).collect()[0]["total_volume"]
print(f"Total data volume: {total_volume} bytes")

# 5.2 Max data volume in a single response.
max_volume = log_df.agg(max("response_size").alias(
    "max_volume")).collect()[0]["max_volume"]
print(f"Max data volume in a single response: {max_volume} bytes")

# 5.3 Min data volume in a single response.
min_volume = log_df.agg(min("response_size").alias(
    "min_volume")).collect()[0]["min_volume"]
print(f"Min data volume in a single response: {min_volume} bytes")

# 5.4 Average data volume through responses.
avg_volume = log_df.agg(avg("response_size").alias(
    "avg_volume")).collect()[0]["avg_volume"]
print(f"Average data volume through responses: {avg_volume:.2f} bytes")


# 6. Week day with most errors type "HTTP Client Error"?
# Filter for 4xx client errors and count by day of the week
client_errors = log_df.filter((col("status_code").startswith("4")))

error_by_day = (
    client_errors.groupBy("day_of_week")
    .count()
    .withColumn("rank", row_number().over(count_window))
    .filter(col("rank") <= 1)
    .drop("rank")
)

print("Week day with most errors: \n")
error_by_day.show()
