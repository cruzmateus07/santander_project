import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


class WebLogAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # PostgreSQL connection details
        postgres_url = "jdbc:postgresql://postgres:5432/logs_db"
        postgres_table = "logs_tb"
        postgres_properties = {
            "user": "postgres_user",
            "password": "password",
            "driver": "org.postgresql.Driver"
        }

        # Read logs from PostgreSQL
        cls.raw_log_df = cls.spark.read.jdbc(
            url=postgres_url, table=postgres_table, properties=postgres_properties)

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
        distinct_ips = self.raw_log_df.select("ip_address").distinct().count()
        self.assertGreater(
            distinct_ips, 0, "No distinct IPs found, something might be wrong")

    def test_duplicate_entries(self):
        """
            Test if the DataFrame contains duplicate entries
        """
        deduplicated_df = self.raw_log_df.dropDuplicates()
        self.assertLess(deduplicated_df.count(), self.raw_log_df.count(
        ), "Duplicates exist in the DataFrame")


if __name__ == "__main__":
    unittest.main()
