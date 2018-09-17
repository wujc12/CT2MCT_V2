class BaseDataLoader:
    def __init__(self):
        self.opt = None

    def initialize(self, opt):
        self.opt = opt

    @staticmethod
    def load_data():
        return None
