import os
import requests
import pandas as pd


class DownloadWineData:
    def __init__(self, data_download_path, data_file_name):
        """Download wine data.

        Parameters
        ----------
        data_download_path : str
            Local working directory where data will be stored.
        data_file_name : str
            Name of file to which data will be saved.

        Returns
        -------
        None.
        """
        self.url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        self.data_download_path = data_download_path
        self.data_file_name = data_file_name

    def __call__(self):
        self.set_cwd()
        self.download_data()
        df = self.load_data()
        return df

    def set_cwd(self):
        """Set current working directory to the local path where the data will be stored.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        os.chdir(self.data_download_path)

    def download_data(self):
        """Download wine data from url to the specified local path.

        Parameters
        ----------
        None.

        Returns
        -------
        None.
        """
        response = requests.get(self.url)
        with open(self.data_file_name, "wb") as f:
            f.write(response.content)

    def load_data(self):
        """Load wine data from saved file.

        Parameters
        ----------
        None.

        Returns
        -------
        df : pandas.core.frame.DataFrame
            Downloaded data set with 178 observations and 14 variables ('class', 'alcohol', 'malic_acid', 'ash',
            'ash_alcalinity', 'magnesium', 'phenols_total', 'flavanoids', 'phenols_nonflavanoid', 'proanthocyanins',
            'color_intensity', 'hue', 'OD280_OD315', 'proline').
        """
        names = ['class', 'alcohol', 'malic_acid', 'ash', 'ash_alcalinity', 'magnesium', 'phenols_total', 'flavanoids',
                 'phenols_nonflavanoid', 'proanthocyanins', 'color_intensity', 'hue', 'OD280_OD315', 'proline']
        df = pd.read_csv(self.data_file_name, names=names)
        return df
