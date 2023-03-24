import pandas as pd
import os

# 폴더 내 모든 csv 파일을 읽어서 하나의 파일로 저장
class CsvMerge:
    def __init__(self, path, encoding='utf-8'):
        self.path = path
        self.files = os.listdir(path)
        self.encoding = encoding
        self.df = pd.DataFrame()

    def merge(self):
        for file in self.files:
            df = pd.read_csv(self.path + '\\' + file)
            self.df = self.df.append(df, ignore_index=True)
        return self.df

    def save(self, filename):
        try:
            self.df.to_csv(f'{self.path}\\{filename}.csv', index=False)
            return True
        except Exception as e:
            print(e)
            return False