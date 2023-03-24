from libs.csv_merge import CsvMerge
from libs.yml_read import YmlReader


class Main:
    def __init__(self):
        self.data = YmlReader('config/config.yml').read()

    def run(self):
        if self.data['config']['type'] == 'csv':
            c = CsvMerge(self.data['config']['path'])
            c.merge()
            c.save(self.data['config']['output'])


if __name__ == '__main__':
    Main().run()
