import yaml

# Read YAML file
class YmlReader:
    def __init__(self, path):
        self.path = path
        self.data = None

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
        return self.data
