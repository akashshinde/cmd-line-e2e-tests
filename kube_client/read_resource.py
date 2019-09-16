import yaml

class ReadResource:
    def __init__(self):
        pass

    def read(self, content):
        dict = yaml.safe_load(content)
        return dict
