import time

from strategies import StrategyResult
from config import Config

if __name__ == "__main__":
    config = Config.load()
    strategies = config.get_strategies()

    while True:
        for strategy in strategies:
            result = strategy.run()

            if result == StrategyResult.ORANGE:
                print("ORANGE")
            elif result == StrategyResult.RED:
                print("RED")


        time.sleep(30)
