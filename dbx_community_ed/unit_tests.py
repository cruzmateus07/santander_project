import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


class WebLogAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.master(
            "local").appName("Test").getOrCreate()

        cls.access_log_path_delta = "dbfs:/mnt/web_server_access_log"  # Databricks Path
        cls.raw_log_df = cls.spark.read.format("delta").load(
            cls.access_log_path_delta)  # Delta Lake path for saved table

        # Log pattern
        cls.log_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(.*?)" (\d{3}) (\d+|-)'

    def test_log_parsing(self):
        """
            Test if logs are correctly parsed into structured format
        """
        required_columns = ["ip_address", "user_id",
                            "status_code", "timestamp", "request"]
        missing_columns = [
            col for col in required_columns if col not in self.raw_log_df.columns]
        self.assertEqual(len(missing_columns), 0,
                         f"Missing expected columns: {missing_columns}")

    def test_distinct_ips_count(self):
        """
            Test counting distinct client IPs
        """
        distinct_ips = self.raw_log_df.select(
            col("value").substr(1, 15).alias("ip_address")
        ).distinct().count()
        self.assertGreater(
            distinct_ips, 0, "No distinct IPs found, something might be wrong")

    def test_duplicate_entries(self):
        """
            Test if the DataFrame contains duplicate entries
        """
        deduplicated_df = self.raw_log_df.dropDuplicates()
        self.assertLess(deduplicated_df.count(), self.raw_log_df.count(
        ), "Duplicates exist in the DataFrame")


suite = unittest.TestLoader().loadTestsFromTestCase(WebLogAnalysisTests)
unittest.TextTestRunner().run(suite)
