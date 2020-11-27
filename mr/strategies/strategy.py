"""Abstraction."""

from enum import Enum

class Strategy:
    """
    Given a time series, a strategy is a way of deciding whether or not we need
    to start panicking.
    """

    def __init__(self, source):
        self.source = source

    def run(self):
        """Run the strategy and return the decision (StrategyResult)."""
        raise NotImplementedError("run is not implemented")

    def time_series(self):
        return self.source.time_series()

class StrategyResult(Enum):
    GREEN = 1
    ORANGE = 2
    RED = 3
