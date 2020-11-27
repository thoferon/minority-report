from strategies import Strategy

class Config:
    def __init__(self):
        pass

    def get_strategies(self):
        return []

    @classmethod
    def load(cls):
        # FIXME: Read config from JSON file

        return cls()
