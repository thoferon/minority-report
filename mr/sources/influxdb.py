"""Integration with InfluxDB as a data source."""

import pandas as pd

from influxdb import DataFrameClient

from .source import Source

class InfluxDB(Source):
    """
    Run a query against InfluxDB and build a DataFrame.

    The configuration must have the form:
    {
        "database": "name",
        "query": "SELECT something FROM something"
    }

    The query should return a single column.
    """

    def __init__(self, config):
        self.client = DataFrameClient("localhost", 8086, "", "", config["database"])
        self.query = config["query"]

    # FIXME: Error handling
    def get_time_series(self):
        response = self.client.query(self.query)
        key = list(response.keys())[0]
        return response[key]
