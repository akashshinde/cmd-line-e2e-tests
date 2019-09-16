from abc import abstractmethod


class BaseCheck:
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    @abstractmethod
    def check(self, input):
        pass