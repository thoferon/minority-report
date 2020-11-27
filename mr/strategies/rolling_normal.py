"""Anomaly detection based on a rolling normal distribution."""

import statistics

from .strategy import Strategy, StrategyResult

class RollingNormal(Strategy):
    """
    This strategy takes the mean and standard deviation of all but the last
    measurement and calculates the probability of observing a measurement
    greater than or equal to the last measurement of the series.

    If it's in [0.01, 0.05), it returns StrategyResult.ORANGE and if it's below
    0.01, it returns StrategyResult.RED.

    If the data source returns several columns, it only considers the first one.
    """

    def __init__(self, source, config):
        super().__init__(source)

    def run(self):
        df = self.time_series()
        ts = df[df.keys()[0]]

        current = ts[0]
        past = ts[1:]

        dist = statistics.NormalDist(past.mean(), past.std())
        cdf  = dist.cdf(current)

        if cdf > 0.99:
            return StrategyResult.RED
        elif cdf > 0.95:
            return StrategyResult.ORANGE
        else:
            return StrategyResult.GREEN
