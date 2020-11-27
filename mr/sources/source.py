"""Abstraction."""

class Source:
    """Abstract data source from which we get time series."""

    def get_time_series(self):
        """
        Should return a Pandas DataFrame ordered from latest to earliest.
        """
        raise NotImplementedError("get_time_series is not implemented")

    # FIXME: Actually cache the value for 30 seconds.
    def time_series(self):
        """
        Return the time series by querying the data source or use the cached
        value.
        """
        self.get_time_series()
