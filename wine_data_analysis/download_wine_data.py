import os
import requests
import pandas as pd


class DownloadWineData:
    def __init__(self, data_download_path, data_file_name):
        self.url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        self.data_download_path = data_download_path
        self.data_file_name = data_file_name

    def __call__(self):
        self.set_cwd()
        self.download_data()
        df = self.load_data()
        return df

    def set_cwd(self):
        os.chdir(self.data_download_path)

    def download_data(self):
        response = requests.get(self.url)
        with open(self.data_file_name, "wb") as f:
            f.write(response.content)

    def load_data(self):
        names = ['class', 'alcohol', 'malic_acid', 'ash', 'ash_alcalinity', 'magnesium', 'phenols_total', 'flavanoids',
                 'phenols_nonflavanoid', 'proanthocyanins', 'color_intensity', 'hue', 'OD280_OD315', 'proline']
        df = pd.read_csv(self.data_file_name, names=names)
        return df
